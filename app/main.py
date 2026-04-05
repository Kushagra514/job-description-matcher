from fastapi import FastAPI,UploadFile,File,Form
from app.matcher import extract_text,match_resume
app = FastAPI()

@app.post("/match")
async def match(file: UploadFile = File(...), job_description: str = Form(...)):
    pdf_bytes = await file.read()
    resume_text = extract_text(pdf_bytes)
    return match_resume(resume_text,job_description)
