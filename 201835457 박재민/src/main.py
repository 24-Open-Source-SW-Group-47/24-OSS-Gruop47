import os
from preprocess import process_file
from analyze import analyze_risks, display_risks

def main():
    input_folder = "./insert_data"
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