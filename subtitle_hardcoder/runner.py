import sys
import argparse
from hardcode_sub import HardcodeSubGen

parser = argparse.ArgumentParser(description="Youtube Subtitile Hardcoder Script")
parser.add_argument('input_video_path', help="input video path")
parser.add_argument('input_subtitle_path', help="input subtitle path")
parser.add_argument('output_video_path', help="output video path")


def run():
    args = parser.parse_args() 
    input_video = args.input_video_path
    input_sub = args.input_subtitle_path
    output_video = args.output_video_path

    print(input_video)
    print(input_sub)
    print(output_video)

    h = HardcodeSubGen(input_video=input_video, input_sub=input_sub, output_video=output_video)
    h.hardcode_sub()

run()