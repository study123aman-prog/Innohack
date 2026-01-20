import whisper

# Load model (small is fast, base is balanced)
model = whisper.load_model("base")

# Transcribe audio file
result = model.transcribe("sample_audio.wav")

print("Recognized Text:")
print(result["text"])
