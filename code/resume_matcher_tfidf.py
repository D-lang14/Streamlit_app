import streamlit as st
import os
import re
import fitz
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Resume Matcher")

#  Upload JD
jd_file = st.file_uploader("Upload Job Description (txt)", type=["txt"])
resume_files = st.file_uploader("Upload Resumes (pdf)", type=["pdf"], accept_multiple_files=True)

def extract_text(pdf_file):
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
      return " ".join(page.get_text() for page in doc)

def extract_keywords(text):
  from nltk.corpus import stopwords
  import nltk
  nltk.download('stopwords')
  stop_words = set(stopwords.words('english'))
  return [w for w in re.findall(r'\b\w+\b', text.lower()) if w not in stop_words and len(w) > 2]

if jd_file and resume_files:
  jd_text = jd_file.read().decode("utf-8")
  resumes = [extract_text(file) for file in resume_files]
  names = [file.name for file in resume_files]

  # TF-IDF Similarity
  tfidf = TfidfVectorizer(tokenizer=extract_keywords)
  matrix = tfidf.fit_transform([jd_text] + resumes)
  similarity = cosine_similarity(matrix[0:1], matrix[1:]).flatten()

  # Keyword Match
  jd_keywords = extract_keywords(jd_text)
  keyword_matches = []
  for res in resumes:
    res_keywords = extract_keywords(res)
    matches = set(jd_keywords) & set(res_keywords)
    keyword_matches.append(matches)

  # Final DataFrame
  df = pd.DataFrame({
      'Resume Name' : names,
      'Similarity Score' : similarity,
      'Keyword Match Count' : [len(m) for m in keyword_matches],
      'Matched Keywords' : [", ".join(m) for m in keyword_matches]
  }).sort_values(by=['Similarity Score', 'Keyword Match Count'], ascending=False)

  st.dataframe(df)

