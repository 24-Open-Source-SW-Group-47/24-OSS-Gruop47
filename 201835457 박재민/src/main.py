from src.ocr import extract_text
from src.nlp import analyze_text
from src.gps import extract_gps_info

def main(image_path):
    text = extract_text(image_path)
    if not text:
        print("No text detected in the image.")
        return
    sentiment, summary = analyze_text(text)
    gps_info = extract_gps_info(image_path)

    print("Extracted Text:", text)
    print("Sentiment Analysis:", sentiment)
    print("Summary:", summary)
    print("GPS Information:", gps_info or "No location data found.")

if __name__ == "__main__":
    main("path/to/image.jpg")