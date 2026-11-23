-- Job Matcher: Stage 1 schema (SQLite; works the same idea in PostgreSQL)
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL UNIQUE,
    industry   TEXT
);

CREATE TABLE IF NOT EXISTS jobs (
    job_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id       INTEGER NOT NULL REFERENCES companies(company_id),
    title            TEXT NOT NULL,
    description      TEXT NOT NULL,
    location         TEXT NOT NULL,
    experience_level TEXT NOT NULL CHECK (experience_level IN ('intern','junior','mid','senior')),
    posted_on        TEXT NOT NULL            -- ISO date, e.g. 2026-11-20
);

CREATE TABLE IF NOT EXISTS skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT NOT NULL UNIQUE
);

-- many-to-many: a job needs many skills, a skill appears in many jobs
CREATE TABLE IF NOT EXISTS job_skills (
    job_id   INTEGER NOT NULL REFERENCES jobs(job_id) ON DELETE CASCADE,
    skill_id INTEGER NOT NULL REFERENCES skills(skill_id),
    PRIMARY KEY (job_id, skill_id)
);

CREATE INDEX IF NOT EXISTS idx_jobs_location   ON jobs(location);
CREATE INDEX IF NOT EXISTS idx_jobs_level      ON jobs(experience_level);
CREATE INDEX IF NOT EXISTS idx_job_skills_skill ON job_skills(skill_id);
