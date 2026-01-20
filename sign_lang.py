
import cv2
import mediapipe as mp
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import os
import pickle

DATASET_DIR = r"C:\Users\DHRUV\OneDrive\Desktop\InnoHack\ISL_Dataset"  
MODEL_FILE = "isl_model.pkl"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True)

def extract_landmarks_from_dataset():
    print("\nProcessing Indian Sign Language Dataset")

    X, y = [], []

    for gesture in os.listdir(DATASET_DIR):
        gesture_path = os.path.join(DATASET_DIR, gesture)

        if not os.path.isdir(gesture_path):
            continue

        print(f"Processing gesture: {gesture}")

        for img_file in os.listdir(gesture_path):
            img_path = os.path.join(gesture_path, img_file)

            image = cv2.imread(img_path)
            if image is None:
                continue

            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                landmarks = []
                for lm in result.multi_hand_landmarks[0].landmark:
                    landmarks.extend([lm.x, lm.y, lm.z])

                if len(landmarks) == 63:
                    X.append(landmarks)
                    y.append(gesture.lower())

    X = np.array(X)
    y = np.array(y)

    print(f"Extracted {len(X)} samples from ISL dataset")
    return X, y

def train_model():
    print("\nTraining model on ISL data")

    X, y = extract_landmarks_from_dataset()

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X, y)

    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    print("ISL model trained and saved")

def recognize_gesture():
    print("\nReal-time ISL recognition (ESC to exit)")

    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)

    cap = cv2.VideoCapture(0)
    hands_live = mp_hands.Hands()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands_live.process(rgb)

        if result.multi_hand_landmarks:
            landmarks = []
            for lm in result.multi_hand_landmarks[0].landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            if len(landmarks) == 63:
                prediction = model.predict(
                    np.array(landmarks).reshape(1, -1)
                )[0]

                cv2.putText(
                    frame,
                    f"ISL: {prediction}",
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

        cv2.imshow("Indian Sign Language Recognition", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    train_model()
    recognize_gesture()