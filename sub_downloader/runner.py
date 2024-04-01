"""
Sub Downloader Runner Script
 
Download transcript in given language. If the specific language is not 
recognized then google translate will be used for translating into the
desired language
"""
 
import os
import re
import argparse
from subtitle_gen import SubtitleGenerator
from googletrans import Translator
 
 
parser = argparse.ArgumentParser(description="Youtube Subtitile Downloader Script")
parser.add_argument('-source-language', '--sl', default="en", help="source language of the video")
parser.add_argument('-dest-language', '--dl', default="fa", help="destination language of the subtitle")
parser.add_argument('link', help="youtube link of the video")
parser.add_argument('-filename', default="out", help="subtitile filename")
parser.add_argument('-keep-orginal', '--k', default=True, help="keep orginal subtitle if translation is used")
parser.add_argument('-orginal-suffix', '--os', default="_org", help="suffix of the orgianl subtitle file")
parser.add_argument('-path', '--p', default=f"{os.getcwd()}/subs/", help="subtitle file output path")

def run():
    args = parser.parse_args() 
    # TODO: use args for given variable 

    video_id = get_video_id(args.link)
    source_lang = args.sl
    dest_lang = args.dl
    path = args.p
    filename = args.filename
    keep_orginal = args.k
    suffix = args.os

    translator = Translator()
    sg = SubtitleGenerator(video_id=video_id, src_lang=source_lang, dst_lang=dest_lang, translator=translator)
    sg.save_subtitle(path, filename, keep_orginal, suffix)
 

def get_video_id(url):
    # Regular expression pattern to match the video ID
    pattern = r'(?<=v=)[\w-]+'
    match = re.search(pattern, url)
    if match:
        return match.group(0)
    else:
        return None

run()