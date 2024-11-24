import os
import re
from PyPDF2 import PdfReader
from docx import Document
import nltk 
nltk.download('punkt') 
nltk.download('punkt_tab')

def extract_text_from_pdf(file_path):
    """PDF 파일에서 텍스트 추출"""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    print(f"Extracted text from PDF:\n{text}")
    return text

def extract_text_from_docx(file_path):
    """DOCX 파일에서 텍스트 추출"""
    document = Document(file_path)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_txt(file_path):
    """TXT 파일에서 텍스트 읽기"""
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def extract_text(file_path):
    """파일 형식에 따라 적절한 텍스트 추출 함수 호출"""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def preprocess_text(text):
    """텍스트 전처리: 공백 정리 및 문장 분리"""
    text = re.sub(r"\s+", " ", text.strip())  # 공백 정리
    text = re.sub(r"[^\w\s.,]", "", text)  # 특수문자 제거
    sentences = nltk.sent_tokenize(text)  # 문장 분리
    sentences = [sentence.strip() for sentence in sentences if len(sentence.strip()) > 5]  # 너무 짧은 문장 제거
    print(f"Preprocessed sentences: {sentences}")  # 디버깅용 출력
    return sentences

def process_file(file_path):
    """파일에서 텍스트를 추출하고 전처리"""
    text = extract_text(file_path)  # 파일 형식에 따른 텍스트 추출
    print(f"Raw text: {text[:200]}")  # 원본 텍스트 일부 출력
    processed_sentences = preprocess_text(text)  # 전처리 적용
    print(f"Processed sentences (type): {type(processed_sentences)}")
    print(f"Processed sentences: {processed_sentences}")  # 디버깅용 출력
    return processed_sentences
