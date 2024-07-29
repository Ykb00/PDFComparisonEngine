import os
import re
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

##############################
# Pdf to match 
query_invoice_path = './test/invoice_number.pdf'

# Directory containing PDFs
pdf_directory = './train'

##############################

# Function to extract text from a PDF file
def extract_text_from_pdf(filepath):
    with open(filepath, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to extract features from the text
def extract_features(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalpha() and word.lower() not in stop_words]
    fDist = FreqDist(filtered_words)
    
    keywords = [word for word, freq in fDist.most_common(10)]
    invoice_number = re.findall(r'\b\d{5,}\b', text)
    dates = re.findall(r'\b\d{2}[-/]\d{2}[-/]\d{4}\b', text)
    amounts = re.findall(r'\b\d+\.\d{2}\b', text)

    return {
        'keywords': keywords,
        'invoice_number': invoice_number,
        'dates': dates,
        'amounts': amounts
    }

# Function to calculate cosine similarity between two texts
def calculate_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

# Function to calculate Jaccard similarity between two sets of keywords
def calculate_jaccard_similarity(keywords1, keywords2):
    set1 = set(keywords1)
    set2 = set(keywords2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0



# Extract text and features from all PDFs in the directory
pdf_texts = {}
pdf_features = {}

for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        filepath = os.path.join(pdf_directory, filename)
        text = extract_text_from_pdf(filepath)
        features = extract_features(text)
        pdf_texts[filename] = text
        pdf_features[filename] = features



query_text = extract_text_from_pdf(query_invoice_path)
query_features = extract_features(query_text)

# Find the most similar invoice
max_cosine_similarity = 0
max_jaccard_similarity = 0
most_similar_invoice_cosine = None
most_similar_invoice_jaccard = None

for filename, text in pdf_texts.items():
    if filename == os.path.basename(query_invoice_path):
        continue  # Skip comparison with itself
    
    cosine_sim = calculate_cosine_similarity(query_text, text)
    jaccard_sim = calculate_jaccard_similarity(query_features['keywords'], pdf_features[filename]['keywords'])

    if cosine_sim > max_cosine_similarity:
        max_cosine_similarity = cosine_sim
        most_similar_invoice_cosine = filename

    if jaccard_sim > max_jaccard_similarity:
        max_jaccard_similarity = jaccard_sim
        most_similar_invoice_jaccard = filename

print(f"Most similar invoice by Cosine Similarity: {most_similar_invoice_cosine} with score {max_cosine_similarity}")
print(f"Most similar invoice by Jaccard Similarity: {most_similar_invoice_jaccard} with score {max_jaccard_similarity}")
