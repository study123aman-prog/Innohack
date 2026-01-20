import streamlit as st
from speech_to_text import speech_to_text
from sign_to_text import sign_to_text
import tempfile

st.set_page_config(page_title="AI Assistive Framework", layout="centered")

st.title("🤖 AI Assistive Framework for Deaf & Hard-of-Hearing")

st.write("Choose a mode of communication:")

option = st.radio(
    "Select Input Type",
    ("Speech to Text", "Hand Sign to Text")
)

# ---------------- SPEECH TO TEXT ----------------
if option == "Speech to Text":
    st.subheader("🎤 Speech to Text")
    audio_file = st.file_uploader("Upload an audio file (.wav)", type=["wav", "mp3"])

    if audio_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(audio_file.read())
            text = speech_to_text(tmp.name)
            st.success("Recognized Text:")
            st.write(text)

# ---------------- SIGN TO TEXT ----------------
elif option == "Hand Sign to Text":
    st.subheader("✋ Hand Sign to Text")

    if st.button("Start Camera"):
        result = sign_to_text()
        st.success("Output:")
        st.write(result)
