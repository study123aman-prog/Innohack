import cv2
from mediapipe.python.solutions import hands as mp_hands_module
from mediapipe.python.solutions import drawing_utils as mp_drawing

# Initialize Hands detector
hands = mp_hands_module.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def sign_to_text_live(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands_module.HAND_CONNECTIONS)
        return "✋ Hand Sign Detected"
    return ""
