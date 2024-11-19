# Image-Based Text Localization

This project is a team project for 24-Open Source Software and is being conducted using ``Hugging Face`` and ``OpenCV``.

The topic is ``Image-Based Text Localization``, aiming to create an open-source solution that helps users determine the location where an image was captured, even in the absence of metadata. The project extracts text from the image, analyzes it, and utilizes the extracted information to identify the image's location.


## 1. Project Overview
- **Feature Definition**
    - Extra text from images (OCR)
    - Analyze text
    - Determine the image's location
- **Technology Stack**
    - ``Python``
    - ``OpenCV``
    - ``Tesseract OCR``
    - ``HuggingFace Transformers``

## 2. Module Development

### 2.1. Extract Text from Images
**Tesseract OCR Configuration:** Implement OCR using PyTesseract after installing Tesseract. Use OpenCV for image preprocessing (e.g., noise reduction, grayscale conversion).

``` python
import cv2
import pytesseract

def extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text
```

### 2.2 Text Analysis
**Text Analysis using HuggingFace Transformers:**
- Sentiment analysis model: ``distilbert-base-uncased-finetuned-sst-2-english``
- Summarization model: ``t5-small``

``` python
from transformers import pipeline

def analyze_text(text):
    sentiment_analyzer = pipeline("sentiment-analysis")
    summary_generator = pipeline("summarization")
    sentiment = sentiment_analyzer(text)
    summary = summary_generator(text, max_length=50, min_length=10, do_sample=False)
    return sentiment, summary
```

### 2.3 Extract Image Location Information
**Extract GPS Information from Image Metadata:** Use Pillow or Exifread to read the GPS data from an image's metadata.

``` python
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_gps_info(image_path):
    img = Image.open(image_path)
    exif_data = img._getexif()
    if not exif_data:
        return None
    gps_info = {}
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        if tag_name == "GPSInfo":
            for key, val in value.items():
                gps_tag = GPSTAGS.get(key, key)
                gps_info[gps_tag] = val
    return gps_info
```

## 3. Test Image

## 4. Project Structure
The project is managed with a modular structure:

```
├── src/
│   ├── ocr.py         # Module for text extraction
│   ├── nlp.py         # Module for NLP analysis
│   ├── gps.py         # Module for location tracking
│   └── main.py        # Integration and execution script
├── tests/             # Unit test code
├── README.md          # Project description
├── requirements.txt   # Required packages
└── setup.py           # Installation script
```

## 5. User Guide
### 5.1 Installation Guide
Provide detailed steps on how to set up and install the project, including:

### 5.2 MIT License
- The project is distributed under the **MIT License**.
- Include the full license text in a ``LICENSE file`` within the repository.
- Mention key points, such as:
    - Free use, modification, and distribution
    - No warranty or liability

### 5.3 Example Data and Execution Instructions

### 5.4 Issue Tracker and Pull Request Policy
- **Issue Tracker**: Encourage users to report bugs or suggest new features via the repository's issue tracker on GitHub.
- **Pull Request Policy**:
    - Contributors should follow coding guidelines and provide detailed descriptions of changes.
    - Ensure proper testing before submitting pull requests.
    - All contributions will be reviewed before merging.