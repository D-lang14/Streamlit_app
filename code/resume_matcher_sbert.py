import os
os.environ["STREAMLIT_WATCHER_IGNORE_PACKAGES"] = "1"

import streamlit as st
import re
import fitz  # PyMuPDF
import unicodedata
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Streamlit App for Multilingual Resume Matcher
st.title("🔍 Resume Matcher using SBERT")

# Upload JD
jd_file = st.file_uploader("📄 Upload Job Description (txt)", type=["txt"])
# Upload multiple resumes
resume_files = st.file_uploader("📑 Upload Resumes (pdf)", type=["pdf"], accept_multiple_files=True)

# Extract text from PDF
def extract_text(pdf_file):
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        return " ".join(page.get_text() for page in doc)

# Normalize Unicode characters
def normalize_text(text):
    return unicodedata.normalize("NFKC", text)

# Optional: Extract keywords from any language (basic version)
def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return [w for w in words if len(w) > 2]  # Filter very short words

# SBERT Matcher (multilingual)
def match_texts(list_a, list_b, model_name="distiluse-base-multilingual-cased-v1"):
    model = SentenceTransformer(model_name)
    emb_a = model.encode(list_a, convert_to_tensor=True, device='cpu')
    emb_b = model.encode(list_b, convert_to_tensor=True, device='cpu')
    sim_matrix = cosine_similarity(emb_a.cpu().numpy(), emb_b.cpu().numpy())
    return sim_matrix

if jd_file and resume_files:
    # Read & normalize JD
    jd_text = normalize_text(jd_file.read().decode("utf-8"))

    # Read, extract, normalize resumes
    resume_texts = [normalize_text(extract_text(file)) for file in resume_files]
    resume_names = [file.name for file in resume_files]

    # Compute similarity
    similarity_scores = match_texts([jd_text], resume_texts)[0]

    # Basic keyword match
    jd_keywords = extract_keywords(jd_text)
    keyword_matches = []
    for res_text in resume_texts:
        res_keywords = extract_keywords(res_text)
        matches = set(jd_keywords).intersection(set(res_keywords))
        keyword_matches.append(matches)

    # Results DataFrame
    df = pd.DataFrame({
        'Resume Name': resume_names,
        'Similarity Score': similarity_scores,
        'Keyword Match Count': [len(m) for m in keyword_matches],
        'Matched Keywords': [", ".join(m) for m in keyword_matches]
    }).sort_values(by=['Similarity Score', 'Keyword Match Count'], ascending=False)

    st.subheader("📊 Matching Results")
    st.dataframe(df, use_container_width=True)
