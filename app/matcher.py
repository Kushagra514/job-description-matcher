import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(pdf_bytes: bytes) -> str:
    file = fitz.open(stream= pdf_bytes, filetype= "pdf")
    text = ""
    for page in file:
        text += page.get_text()
    return text

def match_resume(resume_text: str,job_description: str) -> dict:
    new_list = [resume_text,job_description]
    obj = TfidfVectorizer()
    tfid_matrix = obj.fit_transform(new_list)
    score = cosine_similarity(tfid_matrix[0],tfid_matrix[1])[0][0]
    return {"match_score": round(float(score) * 100, 2)}