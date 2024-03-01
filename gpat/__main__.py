import argparse
import os
import sys

from GPAT.gpat.detect import detect_and_track
from GPAT.gpat.pose_estimate_from_tracking_data import \
    pose_estimate_from_tracking_data
from GPAT.gpat.utils.config import read_config


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
        args_parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()