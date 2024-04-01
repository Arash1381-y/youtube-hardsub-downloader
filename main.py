import sys
import re
import subprocess


SUB_DOWNLOADER = "./sub_downloader"

def main():
    link = sys.argv[1]
    source_lang = "en"
    dest_lang = "fa"

    # run the sub downloader
    cmd = f'source ./sub_downloader/venv/bin/activate; python3 ./sub_downloader/runner.py {link} --sl {source_lang} --dl {dest_lang}; deactivate'
    p1 = subprocess.run(cmd, shell=True, executable='/bin/bash') 

    #run the video downloader
    cmd = f'source ./video_downloader/venv/bin/activate; python3 ./video_downloader/runner.py {link} -p ./videos/; deactivate;'
    p2 = subprocess.call(cmd, shell=True, executable='/bin/bash')
    
    #run the video downloader
    cmd = f'source ./subtitle_hardcoder/venv/bin/activate; python3 ./subtitle_hardcoder/runner.py ./videos/out.mp4 ./subs/out_sub.srt ./vidoes/hard_sub.mp4; deactivate'
    p3 = subprocess.call(cmd, shell=True, executable='/bin/bash')

main()
