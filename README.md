# AI Resume Screener

**Author:** Sai Sarthak Sadangi  

---

## Project Overview
The AI Resume Screener is a tool designed to assist recruiters and hiring teams in evaluating how well a candidate's resume aligns with a specific job description. Leveraging Natural Language Processing (NLP) techniques, it automates the initial resume screening process, reducing manual workload, saving time, and ensuring consistency in candidate evaluation.  

---

## Features
- Upload multiple resumes in **PDF** or **DOCX** format  
- Input a job description directly into the application  
- Extract and process text automatically from resumes  
- Score resumes based on relevance using **NLP-based techniques**  
- Rank resumes by match percentage  
- Export results to a **CSV file**  
- Intuitive and minimal user interface built with **Streamlit**  

---

## How It Works
1. **Text Extraction** – Resumes are parsed using **pdfplumber** (PDF files) and **docx2txt** (Word documents).  
2. **Preprocessing** – Stopwords are removed and text is tokenized using **NLTK**.  
3. **Vectorization** – Both job description and resumes are transformed into **TF-IDF vectors** with `TfidfVectorizer`.  
4. **Scoring** – **Cosine similarity** is calculated to generate a relevance score.  
5. **Output** – A ranked table displays match percentages with an option to download results as **CSV**.  

---

## Technology Stack
- **Python 3.10+**  
- **Streamlit** – User interface  
- **pdfplumber** – PDF parsing  
- **docx2txt** – DOCX parsing  
- **scikit-learn** – TF-IDF and similarity scoring  
- **pandas** – Data handling and output formatting  
- **NLTK** – Text preprocessing  

---

## Live Demo
[Link to the live demo will be provided here]  

---

## Installation and Usage (Single Flow)

Run the following commands step by step in your terminal:

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/AI_Resume_Screener.git
cd AI_Resume_Screener

# Create and activate virtual environment (recommended)
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Launch the application
streamlit run app.py
