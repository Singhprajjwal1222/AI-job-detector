"""Stage 1 practice queries. In Stage 3 the agent's 'filter by SQL' tool will call functions like these."""
import sqlite3

def connect(db_path="jobs.db"):
    con = sqlite3.connect(db_path); con.row_factory = sqlite3.Row
    return con

def jobs_by_skills(con, skills, level=None, location=None, limit=10):
    """Jobs ranked by how many of the given skills they require."""
    marks = ",".join("?" * len(skills))
    sql = f"""
        SELECT j.job_id, j.title, c.name AS company, j.location, j.experience_level,
               COUNT(*) AS matched_skills
        FROM jobs j
        JOIN companies c   ON c.company_id = j.company_id
        JOIN job_skills js ON js.job_id = j.job_id
        JOIN skills s      ON s.skill_id = js.skill_id
        WHERE s.name IN ({marks})
          AND (? IS NULL OR j.experience_level = ?)
          AND (? IS NULL OR j.location = ?)
        GROUP BY j.job_id
        ORDER BY matched_skills DESC, j.posted_on DESC
        LIMIT ?"""
    params = [*skills, level, level, location, location, limit]
    return [dict(r) for r in con.execute(sql, params)]

def top_skills(con, limit=10):
    """Most in-demand skills across all postings."""
    sql = """SELECT s.name, COUNT(*) AS jobs
             FROM skills s JOIN job_skills js ON js.skill_id = s.skill_id
             GROUP BY s.skill_id ORDER BY jobs DESC LIMIT ?"""
    return [dict(r) for r in con.execute(sql, (limit,))]

if __name__ == "__main__":
    con = connect()
    print("Top skills:", top_skills(con, 5))
    print("\nBest matches for Python + SQL + Embeddings (intern, Delhi):")
    for row in jobs_by_skills(con, ["Python", "SQL", "Embeddings"], level="intern", location="Delhi", limit=5):
        print(row)
