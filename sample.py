


import requests
import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser



engine =pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)
recognizer=sr.Recognizer()
def cmd():
    with sr.Microphone()as source:
        pro="Hi Sir."
        print(pro)
        engine.say(pro)
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        ask="What Can i do for you!!! "
        print(ask)
        engine.say(ask)
        engine.runAndWait()
        recordedaudio=recognizer.listen(source, timeout=3.00)
        engine.say(None)
    try:
        command=recognizer.recognize_google(recordedaudio)
        print(command)
    except Exception as ex:
        print(ex)
    
    if 'launch' in command:
        a='Launching codeclub.....'
        engine.say(a)
        engine.runAndWait()
        programme="D:\magicians\The.Magicians.2015.S05E10.Purgatory.720p.WEB-HD.x264.300MB-Pahe.in.mkv"
        webbrowser.open(programme)
        engine.runAndWait
        engine.stop

        


    if 'play' in command:
        b='opening youtube....'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(command)
        

    if 'exit' in command:
            engine.say("Thanks for giving me your time")
            exit()

while True:
    cmd()
    