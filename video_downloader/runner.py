"""
Video Downloader Runner Script

download the youtube vidoe
"""
import argparse
from downloader import YoutubeDowloader

parser = argparse.ArgumentParser(description="Youtube Video Hardcoder Script")
parser.add_argument("URL")
parser.add_argument("-path")

def run():
    args = parser.parse_args() 
    url = args.URL 
    path = args.path
    opt = {
          'outtmpl': {
                'default': path + "/" + "/%(title)s.%(ext)s"
          }
    }
    downloader = YoutubeDowloader(opt)
    downloader.download(url)

run()

"""
if opt is None:
        current_path = os.getcwd()
        # Define the paths dictionary
        paths = {
            'home': f'{current_path}',
        }

        outtmpl = {
            'default': 'videos/%(title)s.%(ext)s',
        }

        opt = {
            'paths': paths,
            'outtmpl': outtmpl
        }
    
    # TODO: use opt 
"""