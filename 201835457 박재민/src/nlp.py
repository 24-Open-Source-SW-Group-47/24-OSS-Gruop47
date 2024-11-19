from transformers import pipeline

def analyze_text(text):
    sentiment_analyzer = pipeline("sentiment-analysis")
    summary_generator = pipeline("summarization")
    sentiment = sentiment_analyzer(text)
    summary = summary_generator(text, max_length=50, min_length=10, do_sample=False)
    return sentiment, summary