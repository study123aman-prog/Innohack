import pyttsx3

engine=pyttsx3.init()
engine.setProperty("rate", 150)

def txt_to_speech(text):
    engine.say(text)
    engine.runAndWait()

if _name_ == "_main_":
    print("Speaking now...")
    txt_to_speech("Hello, this is a text to speech test")