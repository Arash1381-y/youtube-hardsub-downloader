"""
Sub Downloader Runner Script
 
Download transcript in given language. If the specific language is not 
recognized then google translate will be used for translating into the
desired language
"""
 
import sys
from subtitle_gen import SubtitleGenerator
from googletrans import Translator
 
 
def run():
    args = sys.argv[1:]
    video_id = args[0]
    source_lang = args[1]
    dest_lang = args[2]
    translator = Translator()
    sg = SubtitleGenerator(video_id=video_id, src_lang=source_lang, dst_lang=dest_lang, translator=translator)
    sg.save_subtitle(filename="sub", keep_orginal=True)
 
run()