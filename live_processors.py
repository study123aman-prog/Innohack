import av
import numpy as np
import cv2

from speech_to_text import speech_to_text_live
from sign_to_text import sign_to_text_live
from emotion_detector import detect_emotion
import live_state

def audio_frame_callback(frame: av.AudioFrame):
    audio = frame.to_ndarray()
    audio = audio.astype("float32")

    text = speech_to_text_live(audio)
    if text:
        live_state.latest_speech = text
        live_state.latest_emotion = detect_emotion(text)

    return frame

def video_frame_callback(frame: av.VideoFrame):
    img = frame.to_ndarray(format="bgr24")

    sign = sign_to_text_live(img)
    if sign:
        live_state.latest_sign = sign

    if sign:
        cv2.putText(
            img, sign, (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 0), 2
        )

    return av.VideoFrame.from_ndarray(img, format="bgr24")
