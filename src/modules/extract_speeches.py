import speech_recognition as sr
import moviepy as mp


class Speech_Extractor:

    def __init__(self) -> None:
        pass

    def convert(filename):
        clip = mp.VideoFileClip(filename)
        clip.audio.write_audiofile(r""+filename+"_audio.wav")
        return r""+filename+"_audio.wav"
    
    def speech_to_txt(filename):
        rec = sr.Recognizer()
        audio = sr.AudioFile(filename)
        audio_file = None
        with audio as source:
            audio_file = rec.record(source)

        result = rec.recognize_google(audio_file)

        return result
        