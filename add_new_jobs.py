"""Demo of a 'constantly changing' index: add 2 new jobs to SQL, then sync the index without rebuilding."""
import sqlite3
from index_jobs import sync

con = sqlite3.connect("jobs.db")
cid = con.execute("SELECT company_id FROM companies LIMIT 1").fetchone()[0]
for title, desc in [("Intern RAG Engineer", "Build retrieval pipelines over documents. You will work with Python, RAG, Embeddings."),
                    ("Intern Agent Developer", "Build tool-using LLM agents. You will work with Python, LLMs, FastAPI.")]:
    cur = con.execute("INSERT INTO jobs(company_id,title,description,location,experience_level,posted_on) VALUES (?,?,?,?,?,?)",
                      (cid, title, desc, "Delhi", "intern", "2026-11-20"))
    for skill in ("Python", "Embeddings"):
        sid = con.execute("SELECT skill_id FROM skills WHERE name=?", (skill,)).fetchone()[0]
        con.execute("INSERT OR IGNORE INTO job_skills VALUES (?,?)", (cur.lastrowid, sid))
con.commit(); con.close()
sync()
