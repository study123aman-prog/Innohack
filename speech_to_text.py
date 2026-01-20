import whisper 
import numpy as np 
import sounddevice as sd 

# Load Whisper model
model = whisper.load_model("base")

def record_audio(duration=5, fs=16000):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return np.squeeze(audio)

def speech_to_txt():
    audio = record_audio()
    result = model.transcribe(audio, fp16=False)
    return result["text"]

# Corrected main check
if __name__ == "__main__":
    print("Recording... Speak now.")
    text = speech_to_txt()
    print("Transcribed Text:")
    print(text)
