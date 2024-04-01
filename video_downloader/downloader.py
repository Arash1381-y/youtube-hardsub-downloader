from yt_dlp import YoutubeDL
import os

class YoutubeDowloader:

    def __init__(self, opt=None) -> None:
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

        self.opt = opt
        self.yt_dlp = YoutubeDL(self.opt)



    def download(self, urls):
        self.yt_dlp.download(urls)
        
