import os
import re
from PyPDF2 import PdfReader
from docx import Document
import nltk 

# Download necessary NLTK data files
nltk.download('punkt') 
nltk.download('punkt_tab')

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)  # Initialize PDF reader
    text = ""
    for page in reader.pages:  # Iterate through each page in the PDF
        text += page.extract_text()  # Extract text from the page
    print(f"Extracted text from PDF:\n{text}")  # Debug: Print extracted text
    return text

# Function to extract text from a DOCX file
def extract_text_from_docx(file_path):
    """Extract text from a DOCX file."""
    document = Document(file_path)  # Open the DOCX file
    text = ""
    for paragraph in document.paragraphs:  # Iterate through paragraphs
        text += paragraph.text + "\n"  # Add each paragraph to the text
    return text

# Function to extract text from a TXT file
def extract_text_from_txt(file_path):
    """Read and return text from a TXT file."""
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()  # Read the entire file
    return text

# Determine file format and call the appropriate text extraction function
def extract_text(file_path):
    """Extract text from a file based on its format (PDF, DOCX, TXT)."""
    ext = os.path.splitext(file_path)[1].lower()  # Get the file extension
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)  # Call PDF extraction
    elif ext == ".docx":
        return extract_text_from_docx(file_path)  # Call DOCX extraction
    elif ext == ".txt":
        return extract_text_from_txt(file_path)  # Call TXT extraction
    else:
        raise ValueError(f"Unsupported file format: {ext}")  # Raise an error for unsupported formats

# Function to preprocess text (e.g., clean, split into sentences)
def preprocess_text(text):
    """Clean and split the input text into sentences."""
    text = re.sub(r"\s+", " ", text.strip())  # Remove extra whitespace
    text = re.sub(r"[^\w\s.,]", "", text)  # Remove special characters
    sentences = nltk.sent_tokenize(text)  # Split text into sentences
    sentences = [sentence.strip() for sentence in sentences if len(sentence.strip()) > 5]  # Remove very short sentences
    print(f"Preprocessed sentences: {sentences}")  # Debug: Print preprocessed sentences
    return sentences

# Process a file: Extract text and preprocess it
def process_file(file_path):
    """Extract text from a file and preprocess it into structured sentences."""
    text = extract_text(file_path)  # Extract text from the file
    print(f"Raw text: {text[:200]}")  # Debug: Print the first 200 characters of raw text
    processed_sentences = preprocess_text(text)  # Preprocess the extracted text
    print(f"Processed sentences (type): {type(processed_sentences)}")  # Debug: Print type of processed data
    print(f"Processed sentences: {processed_sentences}")  # Debug: Print processed sentences
    return processed_sentences