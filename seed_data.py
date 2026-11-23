"""Fills the database with ~500 synthetic job postings so you can start today.
Later, replace this with a real dataset (e.g. a Kaggle jobs CSV) using the same tables."""
import random, sqlite3, datetime, os

random.seed(42)
COMPANIES = [("Acme AI","AI"),("DataNest","Analytics"),("CloudCraft","Cloud"),("FinEdge","Fintech"),
             ("HealthLoop","Healthtech"),("ShopSphere","E-commerce"),("EduSpark","Edtech"),("RouteWise","Logistics"),
             ("PixelForge","Gaming"),("SecureNet","Security")]
LOCATIONS = ["Delhi","Bengaluru","Mumbai","Hyderabad","Pune","Remote"]
LEVELS = ["intern","junior","mid","senior"]
ROLES = {
 "LLM Engineer":      (["Python","LLMs","Prompt Engineering","RAG","FastAPI","Embeddings"],
                       "Build LLM-powered agents that use tools and remember context."),
 "Backend Engineer":  (["Python","SQL","FastAPI","Docker","PostgreSQL","REST APIs"],
                       "Ship backend features to production and keep them reliable."),
 "Data Scientist":    (["Python","Pandas","Scikit-learn","SQL","Statistics","NumPy"],
                       "Analyse data and build models that improve the product."),
 "ML Engineer":       (["Python","PyTorch","Scikit-learn","Docker","MLOps","SQL"],
                       "Train, evaluate and deploy machine learning models."),
 "Search Engineer":   (["Python","Embeddings","FAISS","SQL","Ranking","Elasticsearch"],
                       "Develop semantic search over a large, constantly changing index."),
 "Data Engineer":     (["Python","SQL","Airflow","Docker","AWS","Spark"],
                       "Build reliable data pipelines and warehouse tables."),
 "Frontend Engineer": (["JavaScript","React","HTML","CSS","TypeScript","REST APIs"],
                       "Build fast, accessible user interfaces."),
 "Cloud Engineer":    (["AWS","Docker","Kubernetes","Linux","Terraform","Python"],
                       "Design and operate cloud infrastructure."),
}

def main(db_path="jobs.db", n_jobs=500):
    if os.path.exists(db_path):
        os.remove(db_path)  # start fresh so reruns do not duplicate
    con = sqlite3.connect(db_path)
    con.executescript(open("schema.sql").read())
    cur = con.cursor()
    for name, ind in COMPANIES:
        cur.execute("INSERT OR IGNORE INTO companies(name, industry) VALUES (?,?)", (name, ind))
    company_ids = [r[0] for r in cur.execute("SELECT company_id FROM companies")]
    skill_cache = {}
    def skill_id(name):
        if name not in skill_cache:
            cur.execute("INSERT OR IGNORE INTO skills(name) VALUES (?)", (name,))
            skill_cache[name] = cur.execute("SELECT skill_id FROM skills WHERE name=?", (name,)).fetchone()[0]
        return skill_cache[name]
    today = datetime.date(2026, 11, 20)
    for _ in range(n_jobs):
        role = random.choice(list(ROLES))
        skills, blurb = ROLES[role]
        level = random.choice(LEVELS)
        picked = random.sample(skills, k=random.randint(4, len(skills)))
        title = f"{'' if level=='mid' else level.capitalize()+' '}{role}".strip()
        desc = f"{blurb} You will work with {', '.join(picked)}."
        posted = (today - datetime.timedelta(days=random.randint(0, 90))).isoformat()
        cur.execute("""INSERT INTO jobs(company_id,title,description,location,experience_level,posted_on)
                       VALUES (?,?,?,?,?,?)""",
                    (random.choice(company_ids), title, desc, random.choice(LOCATIONS), level, posted))
        job_id = cur.lastrowid
        for s in picked:
            cur.execute("INSERT INTO job_skills VALUES (?,?)", (job_id, skill_id(s)))
    con.commit(); con.close()
    print(f"Seeded {n_jobs} jobs into {db_path}")

if __name__ == "__main__":
    main()
