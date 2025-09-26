
<img src="https://github.com/user-attachments/assets/1b04d15e-4f72-42c1-b42d-b2281e0e41b5" width="100%" style="max-height:600px;" alt="AI Resume Screener Output"/>

# Hirebie AI-Powered Resume Screening Tool

**Author:** Sai Sarthak Sadangi  
**Assignment:** Smart Resume Screening Tool  
**Role:** AI/ML & Data Scientist Intern  

## Project Overview

This tool is designed to assist recruiters and hiring teams in evaluating how well a candidate's resume aligns with a specific job description. By using natural language processing (NLP) techniques, it automates the initial resume screening process. This reduces manual workload, saves time, and brings consistency to candidate evaluation.

## Features

- Upload multiple resumes in PDF or DOCX format
- Paste a job description into the app interface
- Automatically extract and process text from resumes
- Score resumes based on relevance using NLP techniques
- Rank resumes by match percentage
- Download results as a CSV file
- Simple and clean user interface built using Streamlit

## How It Works

1. **Text Extraction**  
   The resumes are parsed using `pdfplumber` for PDFs and `docx2txt` for Word documents.

2. **Preprocessing**  
   Stopwords are removed and the text is tokenized using `nltk` to prepare for analysis.

3. **Vectorization**  
   The job description and resume texts are converted to TF-IDF vectors using `TfidfVectorizer`.

4. **Scoring**  
   Cosine similarity is calculated between the job description and each resume to determine a match score.

5. **Output**  
   A ranked table is displayed showing match percentages, with an option to export the data as a CSV file.

## Technology Stack

- Python 3.10+
- Streamlit
- pdfplumber
- docx2txt
- scikit-learn
- pandas
- nltk

 Live Demo

 [Click here to try the app](https://ai-resume-screener-ultra.streamlit.app/)

## Installation and Usage

Follow these steps to run the application locally on your system:

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/AI_Resume_Screener.git
   cd AI_Resume_Screener
