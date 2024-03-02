import argparse
import os
import sys

from gpat.utils.gpat2fpat import gpat2fpat


def main():
    description = "GPAT: Golf Player Analysis Tool"
    args_parser = argparse.ArgumentParser(description=description)
    
    subparsers = args_parser.add_subparsers(dest="command")
    
    fpat_parser = subparsers.add_parser("fpat", help="convert GPAT format to FPAT format")
    fpat_parser.add_argument("-i", "--input", type=str, required=True, help="input directory path")
    
    args = args_parser.parse_args()
    if args.command == "fpat":
        gpat2fpat(input_path=args.input)
    else:
        args_parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()