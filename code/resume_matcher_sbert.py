import os
os.environ["STREAMLIT_WATCHER_IGNORE_PACKAGES"] = "1"

import streamlit as st
import re
import fitz  # PyMuPDF
import unicodedata
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Streamlit App for Resume Matcher using SBERT
# Set up the Streamlit app
st.title("🔍 Resume Matcher using SBERT")

# Upload JD
jd_file = st.file_uploader("📄 Upload Job Description (txt)", type=["txt"])
# Upload multiple resumes
resume_files = st.file_uploader("📑 Upload Resumes (pdf)", type=["pdf"], accept_multiple_files=True)

# PDF text extraction
def extract_text(pdf_file):
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        return " ".join(page.get_text() for page in doc)

# Normalize unicode characters
def normalize_text(text):
    return unicodedata.normalize("NFKC", text)

# (Optional) Keyword extractor
def extract_keywords(text):
    from nltk.corpus import stopwords
    import nltk
    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('english'))
    return [w for w in re.findall(r'\b\w+\b', text.lower()) if w not in stop_words and len(w) > 2]

# Core SBERT Matcher Function
def match_texts(list_a, list_b, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    emb_a = model.encode(list_a, convert_to_tensor=True, device='cpu')
    emb_b = model.encode(list_b, convert_to_tensor=True, device='cpu')
    sim_matrix = cosine_similarity(emb_a.cpu().numpy(), emb_b.cpu().numpy())
    return sim_matrix

if jd_file and resume_files:
    # Read job description
    jd_text = jd_file.read().decode("utf-8")
    
    # Extract resume texts
    resume_texts = [extract_text(file) for file in resume_files]
    resume_names = [file.name for file in resume_files]

    # Semantic Similarity using SBERT
    similarity_scores = match_texts([jd_text], resume_texts)[0]  # Single JD vs multiple resumes

    # Keyword Matching (optional)
    jd_keywords = extract_keywords(jd_text)
    keyword_matches = []
    for res_text in resume_texts:
        res_keywords = extract_keywords(res_text)
        matches = set(jd_keywords).intersection(set(res_keywords))
        keyword_matches.append(matches)

    # Final DataFrame
    df = pd.DataFrame({
        'Resume Name': resume_names,
        'Similarity Score': similarity_scores,
        'Keyword Match Count': [len(m) for m in keyword_matches],
        'Matched Keywords': [", ".join(m) for m in keyword_matches]
    }).sort_values(by=['Similarity Score', 'Keyword Match Count'], ascending=False)

    st.subheader("📊 Matching Results")
    st.dataframe(df, use_container_width=True)
