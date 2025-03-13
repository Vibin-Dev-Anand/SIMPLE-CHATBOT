from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    sentiment: str

def get_mood(input_text: str, threshold_positive: float, threshold_negative: float) -> Mood:
    sentiment = TextBlob(input_text).sentiment.polarity
    
    if sentiment >= threshold_positive:
        return Mood("positive")
    elif sentiment <= threshold_negative:
        return Mood("negative")
    else:
        return Mood("neutral")

if __name__ == "__main__":
    text = input("Enter text: ")
    
    threshold_positive = 0.3  # Adjust this threshold as needed
    threshold_negative = -0.5  # Adjust this threshold as needed
    
    mood = get_mood(text, threshold_positive, threshold_negative)
    print(f"Sentiment: {mood.sentiment}")
