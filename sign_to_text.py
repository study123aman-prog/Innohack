import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def sign_to_text_live(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        return "✋ Hand Sign Detected"
    return ""
