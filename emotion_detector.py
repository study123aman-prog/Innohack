def detect_emotion(text):
    if not text or len(text.strip()) < 3:
        return None

    text = text.lower()

    emergency = [
        "emergency", "danger", "fire",
        "evacuate", "immediately", "help"
    ]

    warning = [
        "warning", "careful", "hot",
        "alert", "risk"
    ]

    for w in emergency:
        if w in text:
            return {
                "emotion": "Emergency",
                "icon": "🚨",
                "color": "#ff4d4d"
            }

    for w in warning:
        if w in text:
            return {
                "emotion": "Warning",
                "icon": "⚠️",
                "color": "#ffa500"
            }

    return {
        "emotion": "Neutral",
        "icon": "🟩",
        "color": "#2ecc71"
    }
