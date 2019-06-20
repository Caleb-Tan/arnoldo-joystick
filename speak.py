import sys
import pyttsx3

def say(s):
    engine.say(s)
    engine.runAndWait() #blocks

engine = init_engine()
print(sys.argv)
# say(str(sys.argv[1]))