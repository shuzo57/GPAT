import argparse
import os
import sys

from gpat.utils.files import FileName
from gpat.utils.gpat2fpat import gpat2fpat
from gpat.utils.motion_analysis_tool import plot_3d_motion


def main():
    description = "GPAT: Golf Player Analysis Tool"
    args_parser = argparse.ArgumentParser(description=description)
    
    subparsers = args_parser.add_subparsers(dest="command")
    
    fpat_parser = subparsers.add_parser("fpat", help="convert GPAT format to FPAT format")
    fpat_parser.add_argument("-i", "--input", type=str, required=True, help="input directory path")
    
    viz_parser = subparsers.add_parser("viz", help="visualize the 3D motion data")
    viz_parser.add_argument("-i", "--input", type=str, required=True, help="input 3D motion data path")
    
    args = args_parser.parse_args()
    if args.command == "fpat":
        if os.path.isdir(args.input):
            gpat2fpat(args.input)
        else:
            print(f"Invalid input path: {args.input}")
            sys.exit(1)
    elif args.command == "viz":
        if os.path.isdir(args.input):
            threed_data_path = os.path.join(args.input, FileName.threed_position)
            plot_3d_motion(threed_data_path)
        else:
            print(f"Invalid input path: {args.input}")
            sys.exit(1)
    else:
        args_parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()