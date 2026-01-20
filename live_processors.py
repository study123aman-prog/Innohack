import av
import cv2
import numpy as np
import mediapipe as mp
import whisper
from emotion_detector import detect_emotion

# Load models once
whisper_model = whisper.load_model("base")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

latest_transcript = ""
latest_emotion = {}

def audio_frame_callback(frame: av.AudioFrame):
    global latest_transcript, latest_emotion

    audio = frame.to_ndarray()
    audio = audio.astype(np.float32)

    # Save small chunk
    whisper_result = whisper_model.transcribe(audio, fp16=False)
    latest_transcript = whisper_result["text"]

    if latest_transcript:
        latest_emotion = detect_emotion(latest_transcript)

    return frame


def video_frame_callback(frame: av.VideoFrame):
    img = frame.to_ndarray(format="bgr24")
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        cv2.putText(
            img,
            "Hand Sign Detected",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

    return av.VideoFrame.from_ndarray(img, format="bgr24")
