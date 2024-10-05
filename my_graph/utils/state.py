from typing import Optional, TypedDict

class MoodClassifierState(TypedDict, total=False):
    message: str
    mood: str
    mood_based_description: str