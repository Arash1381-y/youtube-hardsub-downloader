import sys
from hardcode_sub import HardcodeSubGen

def run():
    args = sys.argv[1:]
    input_video = args[0]
    input_sub = args[1]
    output_video = args[2]

    h = HardcodeSubGen(input_video=input_video, input_sub=input_sub, output_video=output_video)
    h.hardcode_sub()