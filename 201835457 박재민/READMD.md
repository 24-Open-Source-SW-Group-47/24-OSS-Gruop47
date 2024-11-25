# Risk Analysis Tool

This project provides a comprehensive solution for analyzing risk-related content from various file formats ``(PDF, DOCX, TXT)``. It leverages advanced text extraction, ``natural language processing (NLP) `` techniques, and ``zero-shot classification`` models to identify and categorize potential risks. The tool is modular and extensible, making it suitable for diverse use cases.

![Project Overview](image/Example1_(compliance_risks_result).png)
![Workflow](image/Example2_(financial_risks).png)
![Risk Detection](image/Example3_(legal_risks).png)
![Output Example](image/result.png)


## 1. Project Overview

### 1.1 Features
- **Document Processing**: Extracts text from multiple file formats (PDF, DOCX, TXT).
- **Text Analysis**: Identifies and categorizes risk-related content using NLP models.
- **Risk Categorization**: Supports predefined risk categories and allows for zero-shot classification for dynamic categorization.
- **Result Visualization**: Outputs risk analysis in a tabular format for better readability.

### 1.2 Technology Stack
- **Python**
- **Libraries**:
    - ``PyPDF2``, ``python-docx`` for document handling
    - ``transformers`` for NLP models
    - ``tabulate``, ``pandas`` for result visualization
    - ``nltk`` for text preprocessing

### 1.3 Project Workflow
Here is an overview of the workflow and results:

#### Example 1: Compliance Risks Result
![Compliance Risks Result](image/Example1_(compliance_risks_result).png)

#### Example 2: Financial Risks
![Financial Risks](image/Example2_(financial_risks).png)

#### Example 3: Legal Risks
![Legal Risks](image/Example3_(legal_risks).png)

#### Summary of Results
![Summary](image/result.png)


## 2. Setup and Installation

### 2.1 Requirements
Ensure that the following tools and packages are installed:
- Python 3.8 or later
- ``pip`` for managing Python packages

### 2.2 Installation
1. Clone the repository:
    ``` bash 
    git clone https://github.com/24-Open-Source-SW-Group-47/24-OSS-Gruop47.git
    cd 201835457 박재민
    ```
2. Install dependencies:
    ``` bash 
    pip install -r requirements.txt
    ```
3. Verify the installation:
    ``` bash 
    python -c "import nltk, pandas, tabulate, transformers; print('All dependencies are installed!')"
    ```

## 3. How to Use

### 3.1 Input Data
- Prepare the documents to be analyzed and place them in the ``insert_data/`` folder. Supported formats: ``.pdf``, ``.docx``, ``.txt``.

### 3.2 Output
- The tool provides:
    - Risk analysis for each file processed.
    - A summary table of all detected risks across all files.
    - Example console output:
    ``` bash
    --- Results for File: compliance_risks.txt ---
    Detected Risks:
    Risk 1:
        - Sentence: "Delays in filing tax documents, leading to penalties."
        - Category: "tax filing delays"
        - Confidence Score: 0.73

    --- Summary of All Detected Risks ---
    +----------------------+-----------------------------------------+---------------------+--------------------+
    | File Name            | Sentence                                | Category            | Confidence Score   |
    +----------------------+-----------------------------------------+---------------------+--------------------+
    | compliance_risks.txt | Delays in filing tax documents, ...    | tax filing delays   | 0.73              |
    +----------------------+-----------------------------------------+---------------------+--------------------+
    ```

## 4. Project Structure
The project follows a modular structure for better maintainability and extensibility.
``` bash
├── src/
│   ├── insert_data/          # Input files for risk analysis
│   ├── analyze.py        # Risk detection using NLP models
│   ├── main.py           # Main script to orchestrate processing and analysis
│   └── preprocess.py     # Text extraction and preprocessing
├── requirements.txt      # List of required Python packages
├── pyproject.toml        # Package setup configuration
└── README.md             # Project description
```

## 5. Module Details

### 5.1 Text Extraction
The ``preprocess.py`` module handles text extraction from different file formats:
- **PDF**: Uses ``PyPDF2``.
- **DOCX**: Uses ``python-docx``.
- **TXT**: Simple file reading.
- Includes preprocessing steps such as:
    - Removing special characters.
    - Splitting text into sentences.

### 5.2. Risk Detection
The ``analyze.py`` module performs risk detection:
- Uses ``Hugging Face Transformers`` for text classification.
- Supports zero-shot classification for dynamically adding risk categories.

### 5.3. Integration
The ``main.py`` module integrates all components:
- Iterates through the files in the ``insert_data/`` folder.
- Processes each file for risk detection.
- Displays individual results and a consolidated summary.


## 6. Predefined Risk Categories
The tool supports the following predefined categories:
- Financial Risks: ``budget overruns``, ``penalty clauses``, ``currency exchange fluctuations``.
- Legal Risks: ``breach of contract``, ``data breach penalties``, ``intellectual property violations``.
- Operational Risks: ``system downtime``, ``lack of contingency planning``, ``workplace hazards``.
- Custom Categories: Add new categories dynamically using zero-shot classification.

## 7. Example Usage

#### 7.1 Input
Place a document, such as ``compliance_risks.txt``, in the ``insert_data/`` folder with the following content:
``` css
Delays in filing tax documents, leading to penalties.
```

#### 7.2 Command
Run the tool:
``` bash
python src/main.py
```

#### 7.3 Output
Results in the console:
```  yaml
--- Results for File: compliance_risks.txt ---
Detected Risks:
Risk 1:
  - Sentence: "Delays in filing tax documents, leading to penalties."
  - Category: "tax filing delays"
  - Confidence Score: 0.73
```

## 8. License
This project is licensed under the ``MIT License``. See the LICENSE file for details.

## 9. Contribution Guidelines
#### 9.1 Issue Tracker
- Report bugs or request features through the GitHub issue tracker.

#### 9.2 Pull Requests
- Follow coding standards and provide unit tests for changes.
- Ensure code is thoroughly tested before submitting.