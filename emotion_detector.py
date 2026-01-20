def detect_emotion(text):
    text = text.lower()

    emergency_keywords = ["immediately", "evacuate", "danger", "emergency", "fire"]
    warning_keywords = ["careful", "warning", "hot", "alert"]

    for word in emergency_keywords:
        if word in text:
            return {
                "emotion": "Emergency",
                "icon": "🚨",
                "color": "red",
                "confidence": 0.9
            }

    for word in warning_keywords:
        if word in text:
            return {
                "emotion": "Warning",
                "icon": "⚠️",
                "color": "orange",
                "confidence": 0.75
            }

    return {
        "emotion": "Neutral",
        "icon": "🟩",
        "color": "green",
        "confidence": 0.6
    }
