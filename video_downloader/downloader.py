from yt_dlp import YoutubeDL
import os

class YoutubeDowloader:

    def __init__(self, opt) -> None:

        self.opt = opt
        self.yt_dlp = YoutubeDL(self.opt)



    def download(self, urls):
        self.yt_dlp.download(urls)
        test = self.yt_dlp.extract_info()
        print(test)
