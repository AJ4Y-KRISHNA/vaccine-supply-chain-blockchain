import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F


# Load multilingual BERT sentiment model
MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)


def analyze_sentiment(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    scores = F.softmax(outputs.logits, dim=1)
    rating = torch.argmax(scores) + 1

    # Convert 1-5 rating to sentiment label
    rating_value = rating.item()

    if rating_value <= 2:
        sentiment = "Negative"
    elif rating_value == 3:
        sentiment = "Neutral"
    else:
        sentiment = "Positive"

    confidence = scores[0][rating_value - 1].item()

    return sentiment, confidence