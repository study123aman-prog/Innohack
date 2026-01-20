import streamlit as st
from streamlit_webrtc import webrtc_streamer

import live_state
from live_processors import (
    audio_frame_callback,
    video_frame_callback
)

st.set_page_config(layout="wide")
st.title("🧠 Live Emotion-Aware Assistive Communication Platform")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎥 Live Camera (Hand Signs)")
    webrtc_streamer(
        key="video",
        video_frame_callback=video_frame_callback,
        media_stream_constraints={"video": True, "audio": False},
    )

with col2:
    st.subheader("🎤 Live Microphone")
    webrtc_streamer(
        key="audio",
        audio_frame_callback=audio_frame_callback,
        media_stream_constraints={"video": False, "audio": True},
    )

st.divider()
st.subheader("📝 Live Captions")

if live_state.latest_speech:
    emotion = live_state.latest_emotion or {
        "emotion": "Neutral",
        "icon": "🟩",
        "color": "#2ecc71"
    }

    st.markdown(
        f"""
        <div style="
            padding:20px;
            background-color:{emotion['color']};
            color:white;
            font-size:22px;
            border-radius:12px;
        ">
        {emotion['icon']} <b>{emotion['emotion']}</b><br><br>
        {live_state.latest_speech}<br><br>
        {live_state.latest_sign}
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Listening and watching...")
