import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()
listener=sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('leastning...')
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        print(command)
        engine.say(command)
        engine.runAndWait()
except:
    pass