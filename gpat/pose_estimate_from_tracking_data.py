import os
import sys
import warnings

warnings.filterwarnings('ignore')

import cv2
import mmcv
import mmengine
import numpy as np
import pandas as pd
import torch

from GPAT.gpat.utils.utils import get_file_name
from mmpose.apis import inference_topdown
from mmpose.apis import init_model as init_pose_estimator
from mmpose.registry import VISUALIZERS
from mmpose.structures import merge_data_samples


def pose_estimate_from_tracking_data(
    video_path: str,
    tracking_data_path: str,
    model_path: str,
    config_path: str,
    output_path: str,
    track_id: int = 1,
    kpt_thr : float = 0.3,
    radius: int = 5,
    alpha: float = 0.8,
    thickness: int = 1,
    skeleton_style: str = 'mmpose',
    draw_heatmap = False,
    show_kpt_idx = False,
    show = False,
    show_interval : int = 0,
    draw_bbox = False,
) -> None:
    # Set the device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')

    # Load the model
    pose_estimator = init_pose_estimator(model_path, config_path, device=device)
    pose_estimator.cfg.visualizer.radius = radius
    pose_estimator.cfg.visualizer.alpha = alpha
    pose_estimator.cfg.visualizer.line_width = thickness
    
    # Make the output directory
    video_name = get_file_name(video_path)
    output_path = os.path.join(output_path, video_name)
    os.makedirs(output_path, exist_ok=True)
    
    img_dir = os.path.join(output_path, 'img')
    os.makedirs(img_dir, exist_ok=True)
    
    # Set the visualizer
    visualizer = VISUALIZERS.build(pose_estimator.cfg.visualizer)
    visualizer.set_dataset_meta(pose_estimator.dataset_meta, skeleton_style=skeleton_style)
        
    # Read the tracking data and video
    df = pd.read_csv(tracking_data_path)
    track_df = df[df['track_id'] == track_id].copy()
    cap = cv2.VideoCapture(video_path)
    
    frame_idx = 0
    min_frame = track_df['frame'].min()
    max_frame = track_df['frame'].max()
    
    while True:
        ret, img = cap.read()
        frame_idx += 1
        print(f'Processing frame: {frame_idx}/{max_frame}', end='\r')
        
        if not ret:
            break
        if frame_idx < min_frame:
            continue
        if frame_idx > max_frame:
            break
        
        x1, y1, x2, y2 = track_df[track_df['frame'] == frame_idx][['x1', 'y1', 'x2', 'y2']].values[0]
        bboxes = np.array([[x1, y1, x2, y2]])

        pose_results = inference_topdown(pose_estimator, img, bboxes)
        data_samples = merge_data_samples(pose_results)
        
        if isinstance(img, str):
            img = mmcv.imread(img, channel_order='rgb')
        elif isinstance(img, np.ndarray):
            img = mmcv.bgr2rgb(img)

        # visualize the results
        if visualizer is not None:
            visualizer.add_datasample(
                'result',
                img,
                data_sample=data_samples,
                draw_gt=False,
                draw_heatmap=draw_heatmap,
                draw_bbox=draw_bbox,
                show_kpt_idx=show_kpt_idx,
                skeleton_style=skeleton_style,
                show=show,
                wait_time=show_interval,
                kpt_thr=kpt_thr)
        
        cv2.imwrite(
            os.path.join(img_dir, f'{video_name}_{frame_idx}.jpg'),
            cv2.cvtColor(visualizer.get_image(), cv2.COLOR_RGB2BGR),
        )
    
    cap.release()
    print('\nDone')

if __name__ == '__main__':
    from GPAT.gpat.utils.config import get_config_value
    model_path = get_config_value('model-setting', 'pose_model')
    config_path = get_config_value('model-setting', 'pose_checkpoint')
    
    pose_estimate_from_tracking_data(
        video_path = "/home/ohwada/golf/2023_11_01/user1/d1/1/cam2_1_300_600.mp4",
        tracking_data_path = "/home/ohwada/GSAT/cam2_1_300_600/tracking_data.csv",
        model_path = model_path,
        config_path = config_path,
        output_path = os.getcwd(),
    )