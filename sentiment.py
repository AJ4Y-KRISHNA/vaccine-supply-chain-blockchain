from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    
    stars = int(result['label'][0])

    if stars >= 4:
        sentiment = "Positive"
    elif stars == 3:
        sentiment = "Neutral"
    else:
        sentiment = "Negative"

    return {
        "Sentiment": sentiment,
        "Confidence": round(result['score'], 3),
        "Stars": stars
    }