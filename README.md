# PDFComparisonEngine

**PDFComparisonEngine** is a Python tool for comparing PDF invoices based on their text content. It extracts and analyzes text from invoices to determine similarity using both cosine similarity and Jaccard similarity metrics.

## Document Representation Method

### Text Extraction
- **Library Used**: `PyPDF2`
- **Method**: Extracts text from each page of a PDF file and combines it into a single string.

### Feature Extraction
- **Text Processing**: Uses `nltk` for tokenization and filtering.
  - **Tokenization**: Splits the text into individual words.
  - **Stopwords Removal**: Removes common, less informative words (e.g., "the", "and").
  - **Frequency Distribution**: Finds the most frequent words in the text.

- **Extracted Features**:
  - **Keywords**: The top 10 most frequent words in the text.
  - **Invoice Numbers**: Identified using regular expressions.
  - **Dates**: Extracted with regular expressions to capture various date formats.
  - **Amounts**: Extracted with regular expressions to find monetary values.

### Text Representation
- **TF-IDF Vectorization**:
  - **Library Used**: `sklearn`
  - **Method**: Converts text into numerical vectors where each word is weighted based on its importance in the document relative to the entire corpus.
  - **Similarity Metric**: Cosine similarity, which measures how similar two text vectors are.

- **Jaccard Similarity**:
  - **Method**: Compares sets of keywords from two texts.
  - **Metric**: Measures the similarity by calculating the ratio of the intersection of keyword sets to their union.

## Instructions

### Prerequisites
Ensure you have the following Python libraries installed:
- `PyPDF2`
- `nltk`
- `scikit-learn`

Install the required packages using pip:

```bash
pip install PyPDF2 nltk scikit-learn
