# AI Job Matcher

Semantic job search plus an LLM agent. Built in 4 stages.

- [x] Stage 1: Data and SQL (this folder)
- [x] Stage 2: Semantic search (embeddings + FAISS)
- [ ] Stage 3: LLM layer (tool-using agent, structured JSON)
- [ ] Stage 4: Ship it (FastAPI, Docker, free deploy)
- [ ] Eval: 20 test queries, top-5 accuracy

## Run Stage 1
```bash
python seed_data.py   # creates jobs.db with ~500 synthetic postings
python queries.py     # runs the example queries
```
No installs needed (Python standard library only).

## Schema
companies 1-to-many jobs; jobs many-to-many skills through job_skills.

## Run Stage 2
```bash
pip install -r requirements.txt   # first run downloads a ~90 MB model
python seed_data.py               # fresh database
python index_jobs.py              # embeds jobs into jobs.faiss
python search.py                  # semantic search + ranking demo
python add_new_jobs.py            # adds 2 jobs, index updates without a rebuild
```
