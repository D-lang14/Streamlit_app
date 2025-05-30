## 🧠 Project Title
Resume Matcher – AI-Powered Resume Ranking Tool

## 📌 Description
This project automatically matches candidate resumes against a given job description (JD) using TF-IDF and keyword similarity techniques. It helps recruiters shortlist the most relevant profiles quickly and efficiently.

## 🛠️ Features
- 📄 Extracts text from PDF resumes using PyMuPDF
- 🤖 Compares resumes to JD using TF-IDF and cosine similarity
- 🔍 Highlights matched keywords
- 📊 Ranks resumes by relevance score
- 🧪 Optional Streamlit UI for quick testing (coming soon)

## 🔧 Technologies Used
- Python 🐍
- Scikit-learn
- pandas
- PyMuPDF (fitz)
- re (Regex)
- Streamlit (optional UI)

## 🚀 Getting Started
🔹 1. Clone the repo
```
git clone https://github.com/your-username/resume-matcher.git
cd resume-matcher
```
🔹 2. Install dependencies
```
# Step 1: Upgrade pip (optional, if pip is outdated)
python3 -m pip install --upgrade pip

# Step 2: Install dependencies
pip install -r requirements.txt
# OR if the above doesn't work
pip install streamlit pandas scikit-learn pymupdf nltk
```
🔹 3. Run the App
```
# Step 3: Run the app using Streamlit
streamlit run Resume_Matcher.py
```

## 📷 Sample Output
![Screenshot 2025-05-29 175517](https://github.com/user-attachments/assets/fc7aeea3-07a2-4867-afcf-26dac7f45913)

This is how it looks on Streamlit.
![Screenshot 2025-05-29 175652](https://github.com/user-attachments/assets/502a4bbf-65ea-4e7e-b3a4-6118f474bf00)


## 🎯 Future Scope
- Add a web-based UI using Streamlit
- Support multiple job descriptions
- Add NLP-based keyword extraction from JD

## 🙋‍♂️ Author
Disha Tarun Patil

📍 Maharashtra, India

🎯 Aspiring AI Engineer | Tech Enthusiast

## 📄 License
This project is licensed under the MIT License.

## 📫 Contact
If you'd like to contribute, suggest improvements, or just say hi, feel free to reach out! 😊
