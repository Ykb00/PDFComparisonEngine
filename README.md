Invoice Similarity Analysis
Overview
This project aims to find the most similar invoice to a given query invoice from a collection of PDF invoices. It uses text extraction and analysis techniques to compare invoices based on their content.

Document Representation Method
Text Extraction
Library Used: PyPDF2
Method: Extracts text from each page of a PDF file and combines it into a single string.
Feature Extraction
Text Processing: Uses nltk for tokenization and filtering.

Tokenization: Splits the text into individual words.
Stopwords Removal: Removes common, less informative words (e.g., "the", "and").
Frequency Distribution: Finds the most frequent words in the text.
Extracted Features:

Keywords: The top 10 most frequent words in the text.
Invoice Numbers: Identified using regular expressions.
Dates: Extracted with regular expressions to capture various date formats.
Amounts: Extracted with regular expressions to find monetary values.
Text Representation
TF-IDF Vectorization:

Library Used: sklearn
Method: Converts text into numerical vectors where each word is weighted based on its importance in the document relative to the entire corpus.
Similarity Metric: Cosine similarity, which measures how similar two text vectors are.
Jaccard Similarity:

Method: Compares sets of keywords from two texts.
Metric: Measures the similarity by calculating the ratio of the intersection of keyword sets to their union.
Instructions
Prerequisites
Ensure you have the following Python libraries installed:

PyPDF2
nltk
scikit-learn
re (part of the Python standard library)
Install the required packages using pip:

bash
Copy code
pip install PyPDF2 nltk scikit-learn
Download NLTK Data
The script requires specific NLTK data for tokenization and stopwords. Run the following commands to download the necessary data:

python
Copy code
import nltk
nltk.download('punkt')
nltk.download('stopwords')
Setup
Set File Paths:

query_invoice_path: Update this variable to point to the PDF file of the invoice you want to match.
pdf_directory: Update this variable to point to the directory containing the PDFs you want to compare against.
Run the Script:
Execute the script using Python:

bash
Copy code
python script_name.py
Replace script_name.py with the name of your Python file.

Output
The script will print:

The invoice most similar to the query invoice based on Cosine Similarity.
The invoice most similar based on Jaccard Similarity.
Each result includes the filename of the most similar invoice and the similarity score.

Notes
Ensure that all PDFs are properly formatted and contain text that can be extracted.
The effectiveness of similarity measurements depends on the quality and structure of the text in the invoices.
