import whisper
import tempfile
import soundfile as sf

model = whisper.load_model("base")

# OFFLINE (file upload)
def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

# LIVE (audio chunks)
def speech_to_text_live(audio_chunk, sample_rate=16000):
    if audio_chunk is None or len(audio_chunk) == 0:
        return ""

    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        sf.write(tmp.name, audio_chunk, sample_rate)
        result = model.transcribe(tmp.name, fp16=False)
        return result["text"]
