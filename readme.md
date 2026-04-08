# 🧠 Job Description Matcher API

A FastAPI-based REST API that compares a **PDF resume** with a **job description** and returns a **similarity score** using **TF-IDF** and **cosine similarity**.

---


## 🚀 Features

* 📄 Upload a PDF resume
* 📝 Input a plain-text job description
* 📊 Get a match score (0–100%)
* ⚡ Fast and lightweight API
* 🐳 Docker support for easy deployment

---

## 🛠️ Tech Stack

* **FastAPI** – API framework
* **PyMuPDF (fitz)** – PDF text extraction
* **scikit-learn** – TF-IDF + cosine similarity
* **Python 3.11**
* **Poetry** – dependency management
* **Docker** – containerization
* **Render** – deployment (optional)

---

## 📦 Installation (Local Setup)

```bash
# Clone the repository
git clone https://github.com/Kushagra514/job-description-matcher.git
cd job-description-matcher

# Install dependencies
poetry install

# Run the server
poetry run uvicorn app.main:app --reload
```

---

## 🌐 API Docs

Once the server is running, open:

👉 http://127.0.0.1:8000/docs

Interactive Swagger UI will be available.

---

## 🔌 API Endpoint

### `POST /match`

Compare a resume with a job description.

### 📥 Request (multipart/form-data)

| Field           | Type             | Description            |
| --------------- | ---------------- | ---------------------- |
| file            | UploadFile (PDF) | Resume file            |
| job_description | string           | Job description (text) |

---

### 📤 Response

```json
{
  "match_score": 27.66
}
```

* Score is a percentage
* Higher = better match

---

## 🐳 Docker Usage

```bash
# Build image
docker build -t job-description-matcher .

# Run container
docker run -p 8000:8000 job-description-matcher
```

API will be available at:

👉 http://localhost:8000

---

## ☁️ Deployment (Render)

1. Push your code to GitHub
2. Go to Render → New Web Service
3. Select:

   * Environment: **Docker**
   * Branch: `main`
4. Deploy 🚀

---

## 🌍 Live Demo

👉 *Add your deployed link here*

---

## 📌 Future Improvements

* Semantic matching using embeddings (BERT/OpenAI)
* Highlight matched keywords
* Resume feedback suggestions
* Support for DOCX files

---

## 📄 License

MIT © Kushagra Tewari
