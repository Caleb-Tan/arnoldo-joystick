import sys
import pyttsx3

engine = pyttsx3.init()

def speak(phrases, wpm):
    print (phrases)
    engine.setProperty("rate", wpm)
    for phrase in phrases:
        engine.say(phrase)
    engine.runAndWait() 

speak(sys.argv[1].split(","), int(sys.argv[2]))