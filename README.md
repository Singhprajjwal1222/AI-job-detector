#Jobpilot -AI Job Matcher 🚀

An AI-powered job recommendation platform that understands natural-language job requests and recommends relevant opportunities using LLMs, semantic search, and skill-based matching.

## ✨ Features

- **Natural Language Understanding:** Extracts skills, experience level, job role, and location from user queries.
- **AI Agent:** Uses Google Gemini to understand job requirements.
- **Semantic Search:** Uses Sentence Transformers and NumPy cosine similarity to find relevant jobs.
- **Smart Filtering:** Filters jobs by location and experience level.
- **AI Explanations:** Explains why recommended jobs match the user's request.
- **REST API:** FastAPI backend with structured JSON responses.
- **Interactive Dashboard:** React frontend with job recommendation cards.
- **Fallback Handling:** Supports local request parsing when the AI service is unavailable.

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| Language | Python |
| LLM | Google Gemini API |
| Embeddings | Sentence Transformers |
| Similarity Search | NumPy |
| Database | SQLite |
| Backend | FastAPI |
| Frontend | React, Vite |
| Icons | Lucide React |

## 🏗️ Architecture

```text
User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
Gemini AI Agent
  ↓
Request Understanding
  ↓
Semantic Search
  ↓
SQLite Job Database
  ↓
AI Recommendation Explanations
  ↓
React Dashboard
```

## 📂 Project Structure

```text
ai-job-detector/
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
└── frontend/
    ├── src/
    ├── package.json
    └── vite.config.js
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Singhprajjwal1222/AI-job-detector.git
cd AI-job-detector
```

### 2. Create a Python environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Never upload your API key to GitHub.

### 5. Start the backend

```bash
uvicorn main:app --reload
```

Backend: http://127.0.0.1:8000

API documentation: http://127.0.0.1:8000/docs

### 6. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173

## 💡 Example Query

```text
I know C++, DSA and Python.
I want a junior software developer job in Bangalore.
```

The system extracts the user's skills, experience level, and preferred location before finding relevant job recommendations.

## 📈 Development Progress

- [x] Stage 1: Data engineering and SQL database
- [x] Stage 2: Semantic search and embeddings
- [x] Stage 3: Gemini-powered AI agent and structured JSON
- [x] Stage 4: FastAPI backend and React frontend
- [ ] Docker and cloud deployment
- [ ] Evaluation using 20 test queries and top-5 accuracy

## 🔮 Future Improvements

- Docker containerization
- Cloud deployment
- Larger real-world job datasets
- Improved recommendation ranking
- Recommendation accuracy evaluation

---

**Built to explore practical applications of LLM agents, semantic search, backend engineering, and modern frontend development.**
