from sentiment import analyze_sentiment

text1 = "The vaccine is very effective and safe."
text2 = "यह टीका बिल्कुल अच्छा नहीं है"

print("English Sentiment:")
print(analyze_sentiment(text1))

print("Hindi Sentiment:")
print(analyze_sentiment(text2))