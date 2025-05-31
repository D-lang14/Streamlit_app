# 🤖 Resume Matcher App (TF-IDF + SBERT + Multilingual)

An intelligent resume matcher built with Streamlit.  
Supports **English, German, French, Hindi, Marathi**, and more – thanks to multilingual SBERT!

---

## 📂 Available Matching Modes

### 1. `app.py` – TF-IDF Matcher
- Traditional keyword-based filtering using TF-IDF + cosine similarity.

### 2. `sbert_resume_matcher.py` – SBERT Matcher
- Uses `sentence-transformers` to find semantically similar resumes.
- Supports multilingual input using:

```
python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('distiluse-base-multilingual-cased-v1')
```

---

## 🧠 Tech Stack

- Python 3.8+
- Streamlit
- Scikit-learn
- Sentence-Transformers (SBERT)
- PyPDF2 / pdfplumber for PDF parsing
- unicodedata, langdetect (optional)

---

## 🌐 Supported Languages
- English 🇬🇧
- German 🇩🇪
- French 🇫🇷
- Hindi 🇮🇳
- Marathi 🇮🇳
- And 50+ more!

---

## 📦 Installation

```
bash
git clone https://github.com/your-username/resume-matcher.git
cd resume-matcher
pip install -r requirements.txt
```

## 🚀 Getting Started
🔹 1. Clone the repo
```
git clone 
cd 
```
🔹 2. Install dependencies
```
# Step 1: Upgrade pip (optional, if pip is outdated)
python3 -m pip install --upgrade pip

# Step 2: Install dependencies
pip install -r requirements.txt
# OR if the above doesn't work
pip install streamlit pandas scikit-learn pymupdf nltk
# For SBERT
pip install sentence_transformers
```
🔹 3. Run the App
```
# Step 3: Run the app using Streamlit
streamlit run resume_matcher_tfidf.py
# or
streamlit run resume_matcher_sbert.py
```

## 📷 Sample Output
![Screenshot 2025-05-31 181332](https://github.com/user-attachments/assets/081eadd4-4b66-489b-8ad1-21ae8aba882f)

![Screenshot 2025-05-31 181349](https://github.com/user-attachments/assets/3edeacf7-1bb8-438f-a277-400ff5bf2376)


## ✅ Features
- Upload multiple resumes and job descriptions
- Support for PDF and TXT
- Similarity score ranking
- Download CSV results
- SBERT-based deep semantic matcher
- DOCX support (coming soon)

## 🙋‍♂️ Author
Disha Tarun Patil

📍 Maharashtra, India

🎯 Aspiring AI Engineer | Tech Enthusiast

## 📄 License
This project is licensed under the MIT License.

## 📫 Contact
If you'd like to contribute, suggest improvements, or just say hi, feel free to reach out! 😊
