from transformers import pipeline
import re
import nltk
import pandas as pd
from tabulate import tabulate
import textwrap

# Download necessary NLTK resources
nltk.download('punkt')

# Function to load the zero-shot classification model
def load_model():
    import torch
    # Use GPU if available, otherwise use CPU
    device = 0 if torch.cuda.is_available() else -1
    # Load the zero-shot classification pipeline
    classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3", device=device)
    return classifier

# Function to preprocess the input text
def preprocess_text(text):
    # Remove extra whitespace and special characters
    text = re.sub(r"\s+", " ", text.strip())
    text = re.sub(r"[^\w\s.,]", "", text)
    # Split text into sentences
    sentences = nltk.sent_tokenize(text)
    # Filter out sentences that are too short
    sentences = [sentence.strip() for sentence in sentences if len(sentence.strip()) > 5]
    return sentences

# Function to analyze risks in sentences using the classifier
def analyze_risks(sentences, risk_categories, batch_size=1):
    print(f"Analyzing risks for sentences: {sentences}")
    classifier = load_model()
    risks = []

    # Process sentences in batches for efficiency
    for i in range(0, len(sentences), batch_size):
        batch = sentences[i : i + batch_size]
        print(f"Processing batch: {batch}")
        # Get classification results from the model
        results = classifier(batch, candidate_labels=risk_categories)

        # Process each sentence and its classification result
        for sentence, result in zip(batch, results):
            if isinstance(result, dict) and "scores" in result:
                # Get the highest score from the classification result
                highest_score = max(result["scores"])
                # Only consider it a risk if the score exceeds 0.6
                if highest_score > 0.6:
                    # Get the category corresponding to the highest score
                    risk_category = result["labels"][result["scores"].index(highest_score)]
                    risks.append({"sentence": sentence, "category": risk_category, "score": highest_score})
            else:
                print(f"Unexpected result format for sentence '{sentence}': {result}")
    return risks

# Function to display detected risks
def display_risks(risks):
    if not risks:
        print("No risks detected.")
        return

    print("\nDetected Risks:")
    # Print each detected risk in a formatted way
    for idx, risk in enumerate(risks, start=1):
        print(f"Risk {idx}:")
        print(f"  - Sentence: {risk['sentence']}")
        print(f"  - Category: {risk['category']}")
        print(f"  - Confidence Score: {risk['score']:.2f}")

# Function to display results for a specific file
def display_results(file_name, risks):
    print(f"\n--- Results for File: {file_name} ---")
    display_risks(risks)

# Function to save results as a Pandas DataFrame
def save_results_as_dataframe(results):
    return pd.DataFrame(results)

# Helper function to wrap text for better formatting
def wrap_text(text, width=50):
    return "\n".join(textwrap.wrap(text, width))

# Function to print a summary table of all detected risks
def print_summary_table(results):
    if not results:
        print("\n--- Summary of All Detected Risks ---")
        print("No risks detected in any files.")
    else:
        # Define table headers
        table_headers = ["File Name", "Sentence", "Category", "Confidence Score"]

        # Prepare table data with wrapped sentences
        table_data = [
            [
                result["File Name"],
                wrap_text(result["Sentence"], width=50),  # Wrap text for better display
                result["Category"],
                result["Confidence Score"]
            ]
            for result in results
        ]

        # Print the formatted table using the `tabulate` library
        print("\n--- Summary of All Detected Risks ---")
        print(tabulate(table_data, headers=table_headers, tablefmt="fancy_grid"))