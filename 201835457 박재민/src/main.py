import os
from preprocess import process_file
from analyze import analyze_risks, display_results, print_summary_table

def main():
    # Define the input folder containing files to be processed
    input_folder = "./insert_data"
    
    # List of predefined risk categories for classification
    risk_categories = [
        "budget overruns",
        "penalty clauses",
        "currency exchange fluctuations",
        "unanticipated costs",
        "breach of contract",
        "regulatory non-compliance",
        "data breach penalties",
        "intellectual property violations",
        "gdpr violations",
        "iso standards non-compliance",
        "tax filing delays",
        "environmental regulation breaches",
        "unencrypted data storage",
        "unauthorized data access",
        "failure to anonymize customer data",
        "supply chain disruptions",
        "workforce management issues",
        "system downtime or failures",
        "lack of contingency planning",
        "negative media coverage",
        "customer trust erosion",
        "product recalls",
        "ransomware attacks",
        "insider threats",
        "phishing attempts",
        "weak password policies",
        "workplace hazards",
        "non-compliance with occupational safety standards",
        "pandemic preparedness",
        "poor market positioning",
        "competitor advancements",
        "failure to adapt to market changes",
        "climate change impact",
        "natural disasters",
        "failure to implement sustainability measures",
        "bribery and corruption",
        "conflicts of interest",
        "discrimination or harassment allegations",
        "misinterpretation of terms",
        "ambiguity in scope of work",
        "termination penalties",
        "overestimation of roi",
        "market volatility",
        "misallocation of resources",
        "employee turnover",
        "inadequate training programs",
        "legal disputes with employees"
    ]

    # Initialize a list to store results from all files
    all_results = []

    # Iterate over each file in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)  # Get the full path of the file
        print(f"\nProcessing file: {file_name}")
        try:
            # Extract and preprocess text from the file
            sentences = process_file(file_path)
            # Analyze the extracted sentences for risks
            risks = analyze_risks(sentences, risk_categories)

            # Append detected risks along with file details to the results list
            for risk in risks:
                all_results.append({
                    "File Name": file_name,
                    "Sentence": risk["sentence"],
                    "Category": risk["category"],
                    "Confidence Score": f"{risk['score']:.2f}"
                })
            # Display results for the current file
            display_results(file_name, risks)
        except ValueError as e:
            # Handle errors such as unsupported file formats
            print(f"Error processing file {file_name}: {e}")

    # Print a summary table of all detected risks from all files
    print_summary_table(all_results)

if __name__ == "__main__":
    # Entry point of the program
    main()