import argparse
import os
import sys

from gpat.detect import detect_and_track
from gpat.pose_estimate_and_track import pose_estimate_and_track
from gpat.pose_estimate_from_tracking_data import \
    pose_estimate_from_tracking_data
from gpat.utils.config import read_config
from gpat.utils.extensions import MEDIA_EXTENSIONS
from gpat.utils.gpat2fpat import gpat2fpat


def main():
    # 設定ファイルの読み込み
    config = read_config()
    pose_model = os.path.expanduser(config["model-setting"]["pose_model"])
    pose_checkpoint = os.path.expanduser(config["model-setting"]["pose_checkpoint"])
    det_model = os.path.expanduser(config["model-setting"]["det_model"])
    det_checkpoint = os.path.expanduser(config["model-setting"]["det_checkpoint"])
    
    # プログラム全体の説明を設定
    description = "GPAT: Golf Player Analysis Tool"
    args_parser = argparse.ArgumentParser(description=description)
    
    args_parser.add_argument("-i", "--input", type=str, required=True, help="input video file path")
    args_parser.add_argument("-o", "--output", type=str, default=os.getcwd(), help="output directory path")
    args_parser.add_argument("-pm", "--pose-model", type=str, default=pose_model, help="pose model path")
    args_parser.add_argument("-pc", "--pose-config", type=str, default=pose_checkpoint, help="pose config path")
    args_parser.add_argument("-dm", "--det-model", type=str, default=det_model, help="detection model path")
    args_parser.add_argument("-dc", "--det-config", type=str, default=det_checkpoint, help="detection config path")
    args_parser.add_argument("-f", "--fpat", type=bool, default=False, help="convert GPAT data to FPAT data")

    # サブコマンドを追加するためのパーサを作成
    subparsers = args_parser.add_subparsers(dest="command")

    # 'first'コマンドの設定
    first_parser = subparsers.add_parser("first", help="human detection and tracking")
    first_parser.add_argument("-i", "--input", type=str, required=True, help="input video file path")
    first_parser.add_argument("-o", "--output", type=str, default=os.getcwd(), help="output directory path")
    first_parser.add_argument("-m", "--det-model", type=str, default=det_model, help="detection model path")
    first_parser.add_argument("-c", "--det-config", type=str, default=det_checkpoint, help="detection config path")
    
    # 'second'コマンドの設定
    second_parser = subparsers.add_parser("second", help="pose estimation from tracking data")
    second_parser.add_argument("-i", "--input", type=str, required=True, help="input video file path")
    second_parser.add_argument("-t", "--tracking_data", type=str, required=True, help="tracking data file path")
    second_parser.add_argument("-o", "--output", type=str, default=os.getcwd(), help="output directory path")
    second_parser.add_argument("-m", "--pose-model", type=str, default=pose_model, help="pose model path")
    second_parser.add_argument("-c", "--pose-config", type=str, default=pose_checkpoint, help="pose config path")
    
    # 引数を解析
    args = args_parser.parse_args()
    if args.command == "first":
        detect_and_track(
            video_path=args.input,
            output_path=args.output,
            model_path=args.det_model,
            config_path=args.det_config
        )
    elif args.command == "second":
        pose_estimate_from_tracking_data(
            video_path=args.input,
            tracking_data_path=args.tracking_data,
            model_path=args.pose_model,
            config_path=args.pose_config,
            output_path=args.output
        )
    else:
        if os.path.isfile(args.input):
            pose_estimate_and_track(
                video_path=args.input,
                output_path=args.output,
                pose_model=args.pose_model,
                pose_checkpoint=args.pose_config,
                det_model=args.det_model,
                det_checkpoint=args.det_config
            )
            video_name = os.path.basename(args.input).split('.')[0]
            gpat2fpat(os.path.join(args.output, video_name, "data"))
        elif os.path.isdir(args.input):
            for file_ in os.listdir(args.input):
                ex = file_.split('.')[-1]
                if os.path.isdir(os.path.join(args.input, file_)):
                    continue  # ignore directory
                if ex in MEDIA_EXTENSIONS:
                    pose_estimate_and_track(
                        video_path=os.path.join(args.input, file_),
                        output_path=args.output,
                        pose_model=args.pose_model,
                        pose_checkpoint=args.pose_config,
                        det_model=args.det_model,
                        det_checkpoint=args.det_config
                    )
                    video_name = os.path.basename(file_).split('.')[0]
                    gpat2fpat(os.path.join(args.output, video_name, "data"))

if __name__ == "__main__":
    main()