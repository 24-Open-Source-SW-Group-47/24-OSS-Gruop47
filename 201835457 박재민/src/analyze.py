from transformers import pipeline
import re
import nltk

nltk.download('punkt')

def load_model():
    import torch
    device = 0 if torch.cuda.is_available() else -1  # GPU 사용 가능하면 0, 아니면 -1(CPU)
    classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3", device=device)
    return classifier

def preprocess_text(text):
    """텍스트 전처리: 공백 정리 및 문장 분리"""
    text = re.sub(r"\s+", " ", text.strip())  # 공백 정리
    text = re.sub(r"[^\w\s.,]", "", text)  # 특수문자 제거
    sentences = nltk.sent_tokenize(text)  # 문장 분리
    sentences = [sentence.strip() for sentence in sentences if len(sentence.strip()) > 5]  # 너무 짧은 문장 제거
    return sentences

def analyze_risks(sentences, risk_categories, batch_size=1):
    """문장을 배치로 처리하여 리스크 문구 탐지"""
    print(f"Analyzing risks for sentences: {sentences}")  # 입력 데이터 확인
    classifier = load_model()
    risks = []

    for i in range(0, len(sentences), batch_size):
        batch = sentences[i : i + batch_size]
        print(f"Processing batch: {batch}")  # 배치 확인
        results = classifier(batch, candidate_labels=risk_categories)

        for sentence, result in zip(batch, results):
            if isinstance(result, dict) and "scores" in result:
                highest_score = max(result["scores"])  # 가장 높은 점수 추출
                if highest_score > 0.8:  # 임계값 80% 이상일 때만 리스크로 간주
                    risk_category = result["labels"][result["scores"].index(highest_score)]
                    risks.append({"sentence": sentence, "category": risk_category, "score": highest_score})
            else:
                print(f"Unexpected result format for sentence '{sentence}': {result}")
    
    return risks



def display_risks(risks):
    """리스크 분석 결과 출력"""
    if not risks:
        print("No risks detected.")
        return

    print("\nDetected Risks:")
    for risk in risks:
        print(f"- Sentence: {risk['sentence']}")
        print(f"  Category: {risk['category']}")
        print(f"  Confidence Score: {risk['score']:.2f}")