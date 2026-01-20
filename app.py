import streamlit as st
import tempfile
from speech_to_text import speech_to_text
from emotion_detector import detect_emotion

st.set_page_config(page_title="Emotion-Aware Assistive Platform")

st.title("🧠 Emotion-Aware Assistive Communication Platform")

st.write(
    "Real-time captions enriched with emotional and urgency awareness "
    "for deaf and hard-of-hearing users."
)

audio = st.file_uploader("Upload Speech Audio", type=["wav", "mp3"])

if audio:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio.read())
        transcript = speech_to_text(tmp.name)

    emotion_data = detect_emotion(transcript)

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:10px;
            background-color:{emotion_data['color']};
            color:white;
            font-size:22px;
        ">
        {emotion_data['icon']} <b>{emotion_data['emotion']}</b><br><br>
        {transcript}<br><br>
        Confidence: {emotion_data['confidence']}
        </div>
        """,
        unsafe_allow_html=True
    )
