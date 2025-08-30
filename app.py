import streamlit as st
import pdfplumber
import docx2txt
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


# Custom stopwords 

custom_stopwords = set("""
a about above after again against all am an and any are as at be because been before being below between both but by
could did do does doing down during each few for from further had has have having he he'd he'll he's her here here's
hers herself him himself his how how's i i'd i'll i'm i've if in into is it it's its itself let's me more most my
myself nor of on once only or other ought our ours ourselves out over own same she she'd she'll she's should so some
such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've
this those through to too under until up very was we we'd we'll we're we've were what what's when when's where where's
which while who who's whom why why's with would you you'd you'll you're you've your yours yourself yourselves
""".split())


# Streamlit Page Configuration

st.set_page_config(page_title="Hirebie Resume Screener", layout="wide")


# Sidebar

with st.sidebar:
    st.image("https://i.ibb.co/9m8T5ggT/hirebie-logo.png", width=200)
    st.markdown("### Hirebie Resume Screener")
    st.markdown("Developed by Sai Sarthak Sadangi")
    st.markdown("---")
    st.markdown(
        "1. Upload multiple resumes (.pdf or .docx)\n"
        "2. Paste job description\n"
        "3. Click 'Match Resumes'\n"
        "4. Download result as CSV"
    )


# Main Area

st.markdown("<h1 style='font-size:36px; margin-bottom:20px;'>AI-powered Resume Screening Tool</h1>", unsafe_allow_html=True)

uploaded_files = st.file_uploader("Upload Resume Files", type=["pdf", "docx"], accept_multiple_files=True)
job_description = st.text_area("Paste the Job Description", height=200)


# Text Preprocessing Function

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    filtered = [word for word in tokens if word not in custom_stopwords]
    return " ".join(filtered)


# Resume Matching Logic

if st.button("Match Resumes"):

    if not uploaded_files:
        st.error("Please upload at least one resume.")
    elif not job_description.strip():
        st.error("Please enter a job description.")
    else:
        results = []
        job_desc_cleaned = preprocess_text(job_description)

        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name
            file_ext = file_name.split('.')[-1]

            # Extract text from resume
            if file_ext == 'pdf':
                text = ""
                with pdfplumber.open(uploaded_file) as pdf:
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text
            elif file_ext == 'docx':
                text = docx2txt.process(uploaded_file)
            else:
                st.warning(f"{file_name} is not a supported format.")
                continue

            resume_cleaned = preprocess_text(text)

            # Calculate similarity
            documents = [job_desc_cleaned, resume_cleaned]
            tfidf = TfidfVectorizer()
            tfidf_matrix = tfidf.fit_transform(documents)
            similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            match_percentage = round(similarity_score * 100, 2)

            results.append({
                "Filename": file_name,
                "Match (%)": match_percentage
            })

        # Display results
        sorted_results = sorted(results, key=lambda x: x["Match (%)"], reverse=True)
        df = pd.DataFrame(sorted_results)

        st.subheader("Resume Match Results")
        st.dataframe(df, use_container_width=True)

        # CSV download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Results as CSV",
            data=csv,
            file_name='resume_screening_results.csv',
            mime='text/csv'
        )
