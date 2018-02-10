import speech_recognition as sr
import os
import json
def main(audio_file):
    print("entering stt")
    r = sr.Recognizer()
    text = "Sorry Google Voice did not understand"
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  # read the entire audio file
    try:
        text = r.recognize_google(audio)
        lowerText = str.lower(text)
        print("Google Voice Recognition thinks you said \n'" + lowerText + "'")
        return lowerText
    except sr.UnknownValueError:
        print("Google Voice Recognition could not understand audio")
        return ""