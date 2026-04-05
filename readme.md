# job-description-matcher

A FastAPI REST API that matches your resume against a job description and returns a compatibility score using TF-IDF and cosine similarity.

## What it does
- Upload a PDF resume
- Paste a job description
- Returns a match score (0-100%)

## Stack
- FastAPI
- PyMuPDF (fitz)
- scikit-learn (TF-IDF + cosine similarity)
- Python 3.11
- Poetry

## Run Locally
```bash
git clone https://github.com/Kushagra514/job-description-matcher.git
cd job-description-matcher
poetry install
poetry run uvicorn app.main:app --reload
```

## API Endpoints

### POST /match
Upload resume PDF and provide job description text.

**Request:** multipart/form-data — PDF file + job_description string

**Response:**
```json
{
  "match_score": 27.66
}
```

## Docs
Visit `http://127.0.0.1:8000/docs` for Swagger UI.