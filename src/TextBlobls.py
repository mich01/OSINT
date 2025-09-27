from textblob import TextBlob
# Analyze the sentiment of OSINT data
text = "I LOVE this product!"
sentiment = TextBlob(text).sentiment
# Display the sentiment polarity and subjectivity
print("Polarity:", sentiment.polarity)
print("Subjectivity:", sentiment.subjectivity)
