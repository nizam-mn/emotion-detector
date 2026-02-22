
"""
Emotion Detection Module
"""

def emotion_detector(text_to_analyze):
    """
    Detect emotions from text input and return scores with dominant emotion.
    """

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return None

    text = text_to_analyze.lower()

    emotions = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0
    }

    if "happy" in text or "joy" in text:
        emotions["joy"] = 0.9
    elif "angry" in text:
        emotions["anger"] = 0.9
    elif "sad" in text:
        emotions["sadness"] = 0.9
    elif "fear" in text:
        emotions["fear"] = 0.9
    elif "disgust" in text:
        emotions["disgust"] = 0.9
    else:
        emotions["joy"] = 0.5  # default neutral

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
