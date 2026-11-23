# AI Job Matcher — AI-Powered Job Recommendation System

An intelligent job recommendation platform that understands natural-language job requests and recommends relevant opportunities using AI, semantic search, and skill-based matching.

## Overview

AI Job Matcher helps users discover relevant job opportunities by describing their skills, experience level, and preferred location in natural language.

The system uses Google's Gemini API to understand user requests, sentence-transformer embeddings for semantic search, and a FastAPI backend connected to a React frontend.

## Key Features

- **Natural Language Understanding:** Extracts skills, job roles, experience levels, and locations from user queries.
- **Semantic Search:** Finds relevant jobs using sentence-transformer embeddings and NumPy cosine similarity.
- **AI-Powered Recommendations:** Uses Gemini to generate explanations for recommended jobs.
- **Smart Filtering:** Filters opportunities by experience level and location.
- **REST API:** FastAPI backend with structured JSON responses.
- **Interactive Dashboard:** React frontend displaying job recommendations and match scores.
- **Fallback Handling:** Provides local request parsing and fallback explanations when the AI service is unavailable.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| AI / LLM | Google Gemini API |
| Embeddings | Sentence Transformers |
| Similarity Search | NumPy |
| Database | SQLite |
| Backend | FastAPI |
| Frontend | React, Vite |
| Icons | Lucide React |
| API Testing | Swagger UI |

## System Architecture

User Query → React Frontend → FastAPI Backend → Gemini Request Understanding → Semantic Search → SQLite Job Data → AI Explanations → React Results Dashboard

## Project Structure

```text
ai-job-detector/
│
├── agent.py
├── main.py
├── search.py
├── embedder.py
├── index_jobs.py
├── queries.py
├── seed_data.py
├── add_new_jobs.py
├── schema.sql
├── requirements.txt
├── jobs.db
├── jobs.npz
│
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   └── index.css
    ├── package.json
    └── ...
```

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-job-detector
```

### 2. Create and activate a Python environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Never commit your `.env` file or expose your API key.

### 5. Start the backend

```bash
uvicorn main:app --reload
```

Backend: `http://127.0.0.1:8000`

API documentation: `http://127.0.0.1:8000/docs`

### 6. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:5173`

## Example User Query

```text
I know C++, DSA and Python.
I want a junior software developer job in Bangalore.
```

The system extracts the user's skills, experience level, and location, then returns relevant job recommendations with explanations.

## Current Implementation

- SQL-based job database with companies, jobs, and skills.
- Semantic embeddings for job descriptions.
- NumPy-based cosine similarity search.
- Gemini-powered natural-language request understanding.
- AI-generated job recommendation explanations.
- FastAPI backend and React frontend integration.

## Future Improvements

- Docker containerization.
- Cloud deployment.
- Larger real-world job datasets.
- Recommendation evaluation using top-5 accuracy.
- Advanced ranking based on skill overlap and job relevance.

---

**Developed as an AI-powered software engineering project combining LLM agents, semantic search, backend APIs, databases, and frontend development.**