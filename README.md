# Jobpilot 🎯
### Connecting Talent with Opportunity.

An AI-powered recruitment platform that connects job seekers with relevant career opportunities through intelligent job matching, natural-language understanding, and semantic search.

## Overview

Jobpilot helps job seekers discover relevant opportunities by describing their skills, experience, preferred job roles, and location in natural language.

Powered by Google Gemini and semantic search, Jobpilot understands job requirements and recommends opportunities based on relevance and skill compatibility.

Our vision is to build a two-sided recruitment platform where job seekers discover the right opportunities and recruiters find the right talent.

## ✨ Features

- **AI-Powered Job Search:** Search for jobs using natural-language descriptions.
- **Gemini AI Integration:** Understands job requirements and extracts relevant information.
- **Smart Skill Matching:** Matches job opportunities with relevant skills and experience.
- **Semantic Search:** Uses vector embeddings and similarity scoring to find relevant jobs.
- **Location-Based Filtering:** Finds opportunities based on preferred locations.
- **Experience-Level Filtering:** Helps identify jobs suitable for different experience levels.
- **AI Match Explanations:** Explains why recommended jobs are relevant.
- **Interactive Dashboard:** Displays job recommendations through a React-based interface.
- **REST API:** Connects the frontend with the FastAPI backend.
- **Fallback Support:** Provides alternative request processing and lightweight embedding support.

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| Programming Language | Python |
| AI Model | Google Gemini API |
| Embeddings | Sentence Transformers / Hash Embeddings |
| Similarity Search | NumPy |
| Database | SQLite |
| Backend | FastAPI |
| Frontend | React.js |
| Build Tool | Vite |
| Icons | Lucide React |
| Frontend Hosting | Vercel |
| Backend Hosting | Render |

## 🏗️ System Architecture

```text
                 User
                   |
                   v
             React Frontend
                   |
                   v
             FastAPI Backend
                   |
                   v
              Gemini AI Agent
                   |
                   v
          Requirement Extraction
                   |
                   v
              Job Search
                   |
                   v
          Vector Similarity Matching
                   |
                   v
             SQLite Database
                   |
                   v
          AI Match Explanations
                   |
                   v
           Job Recommendation UI
```

## 📂 Project Structure

```text
ai-job-detector/
│
├── agent.py
├── main.py
├── search.py
├── embedder.py
├── index_jobs.py
├── queries.py
├── add_new_jobs.py
├── seed_data.py
├── schema.sql
├── requirements.txt
├── jobs.db
├── jobs.npz
├── render.yaml
│
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   ├── index.css
    │   └── main.jsx
    ├── package.json
    └── vite.config.js
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Singhprajjwal1222/HireSense.git
cd HireSense
```

### 2. Create a Python virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Gemini API