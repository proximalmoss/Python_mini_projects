import pyttsx3

engine = pyttsx3.init()
names = ["Hamiz", "arpit balls", "Javed", "Ritika", "John", "Shah rukh Khan", "I"]

engine.say("shoutout to")
engine.runAndWait()

for name in names:
    engine.say(name)
    engine.runAndWait()