from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator

class SrtItem:
    def __init__(self, index, start, end, text) -> None:
        self.index = index
        self.start = start
        self.end = end
        self.text = text


    def __str__(self) -> str:
        return f"""
{self.index}
{self.start} --> {self.end}
{self.text}
        """


class SubtitleGenerator:

    def __init__(self, src_lang="en", dst_lang="fa", video_id=None, translator=None, srt_filname=None) -> None:
        self.src_lang = src_lang
        self.dst_lang = dst_lang
        self.video_id = video_id
        self.srt_filename = srt_filname
        self.translator = translator

    
    def __does_sub_exist(self):
        # try to search for existing subtitiles
        # if there is any perisan or english subtitile then we can 
        # fetch them in the nex step
        transcript_list = YouTubeTranscriptApi.list_transcripts(self.video_id)
        try:
            transcript = transcript_list.find_transcript(['fa', 'en'])
            return transcript, True
        except:
            return None, False




    def get_subtitle(self):
        transcript, ok = self.__does_sub_exist()
        if not ok:
            # TODO: use OpenAI voice recognizer if there is no sub
            raise RuntimeError("No Subtitle Available")

        transcript_content = transcript.fetch()

        srt_obj_list = []
        lang = transcript.language_code
        index = 1
        for obj in transcript_content:
            start = convert_sec_to_srt(obj["start"])
            end = convert_sec_to_srt(obj["start"] + obj["duration"])
            if lang == 'fa':
                text = obj["text"]
            else:
                text = self.translate_text(obj["text"])

            s = SrtItem(index=index, start=start, end=end, text=text) 
            srt_obj_list.append(s)
            index += 1
        

        return srt_obj_list
    

    def save_subtitle(self, filename=None):
        if not filename and not self.srt_filename:
            raise ValueError("Output file has no name")

        dest_file = self.srt_filename if self.srt_filename is not None else filename
        srt_items = self.get_subtitle()

        with open(dest_file, "w") as f:
            for item in srt_items:
                f.write(str(item) + "\n")
        f.close()

    def translate_text(self, text):
        return self.translator.translate(text, src=self.src_lang, dest=self.dst_lang).text


def convert_sec_to_srt(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


TEST_ID = "PaxVCsnox_4&t=5s"
translator = Translator()
sg = SubtitleGenerator(video_id=TEST_ID, srt_filname="out.srt", translator=translator)
sg.save_subtitle()