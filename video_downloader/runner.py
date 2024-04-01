"""
Video Downloader Runner Script

download the youtube vidoe
"""

import sys
from downloader import YoutubeDowloader

def run():
    args = sys.argv[1:]
    url = args[0] 
    downloader = YoutubeDowloader()
    downloader.download(url)

run()