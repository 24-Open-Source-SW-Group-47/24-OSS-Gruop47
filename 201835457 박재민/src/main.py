import os
from preprocess import process_file
from analyze import analyze_risks, display_risks

def main():
    input_folder = "./insert_data"
    risk_categories = [
        "financial risk",
        "legal liability",
        "contractual obligation",
        "data privacy issue",
        "compliance risk"
    ]

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        print(f"Processing file: {file_name}")
        try:
            sentences = process_file(file_path)
            risks = analyze_risks(sentences, risk_categories)
            display_risks(risks)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()