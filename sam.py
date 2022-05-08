import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser



engine =pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()
def cmd():
    with sr.Microphone()as source:
        print("Hi all!! How you all are doing ??, Please wait till  boot ..........")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print("Ask me anything!!! ")
        recordedaudio=recognizer.listen(source)

    try:
        command=recognizer.recognize_google(recordedaudio)
    except Exception as ex:
        print(ex)
    
    if "Chrome" in command:
        a="Opening chrome........."
        engine.say(a)
        engine.runAndWait()
        webbrowser.open("google.com")

    if 'play' in command:
        b='opening youtube....'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(command)