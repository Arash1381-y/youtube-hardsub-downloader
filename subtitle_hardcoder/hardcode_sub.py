import ffmpeg

class HardcodeSubGen:
    def __init__(self, input_video, input_sub, output_video) -> None:
        self.input_video = input_video 
        self.input_sub = input_sub
        self.output_video = output_video


    def hardcode_sub(self):
        video = ffmpeg.input(self.input_video)
        audio = video.audio
        ffmpeg.concat(video.filter("subtitles", self.input_sub), audio, v=1, a=1).output(self.output_video).run()
        ffmpeg.input(self.input_video)