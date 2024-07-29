# PDFComparisonEngine

**PDFComparisonEngine** is a Python tool designed to compare PDF invoices by analyzing their text content. It utilizes both cosine similarity and Jaccard similarity metrics to determine how closely invoices match each other.

## Document Representation Method

### Text Extraction
- **Library Used**: `PyPDF2`
- **Method**: Extracts text from each page of a PDF and combines it into a single string for analysis.

### Feature Extraction
- **Text Processing**: Utilizes `nltk` for text tokenization and filtering.
  - **Tokenization**: Breaks down text into individual words.
  - **Stopwords Removal**: Filters out common but less informative words (e.g., "the", "and").
  - **Frequency Distribution**: Analyzes the most frequent words in the text.

- **Extracted Features**:
  - **Keywords**: Identifies the top 10 most frequent words.
  - **Invoice Numbers**: Extracted using regular expressions.
  - **Dates**: Extracted using regular expressions for various date formats.
  - **Amounts**: Extracted using regular expressions to identify monetary values.

### Text Representation
- **TF-IDF Vectorization**:
  - **Library Used**: `scikit-learn`
  - **Method**: Converts text into numerical vectors, weighting words by their importance in the document relative to the entire corpus.
  - **Similarity Metric**: Cosine similarity, which measures the similarity between text vectors.

- **Jaccard Similarity**:
  - **Method**: Compares sets of keywords from two texts.
  - **Metric**: Calculates the ratio of the intersection of keyword sets to their union.

## Features
- **Cosine Similarity**: Evaluates how similar the query invoice is to other invoices based on text content.
- **Jaccard Similarity**: Compares sets of keywords between the query invoice and other invoices.
- **Confidence Levels**: Provides a score indicating the degree of similarity for each comparison.
- **File Names**: Outputs the file name of the most similar invoice for both similarity metrics.

## Instructions

### Prerequisites
Ensure you have the following Python libraries installed:
- `PyPDF2`
- `nltk`
- `scikit-learn`

Install the required packages using pip:

```bash
pip install PyPDF2 nltk scikit-learn

### **Setup**
Set File Paths:

##### Query Invoice Path:
Update the query_invoice_path variable in the script to point to the PDF file of the invoice you want to compare.
`query_invoice_path = './test/invoice_number.pdf'`

##### PDF Directory:
Update the pdf_directory variable in the script to point to the directory containing the PDFs you want to compare against.

`pdf_directory = './train'`

##### Run the Script:
Execute the script using Python:
`python script_name.py`
###### * Replace script_name.py with the name of your Python file.Replace script_name.py with the name of your Python file.*

#### Output
The script will print:

`The invoice most similar to the query invoice based on Cosine Similarity, including the confidence level and filename.`
`The invoice most similar based on Jaccard Similarity, including the confidence level and filename.`
*Each result includes the filename of the most similar invoice and the similarity score.*

##### License
This project is licensed under the MIT License - see the LICENSE file for details.

##### Notes
Ensure that all PDFs are properly formatted and contain extractable text.
The effectiveness of similarity measurements depends on the quality and structure of the text in the invoices.
