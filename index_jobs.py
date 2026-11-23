
"""Stage 2a: Build or update NumPy vector index."""

import os
import numpy as np
from queries import connect
from embedder import embed, DIM

INDEX_PATH = "jobs.npz"


def job_texts(con, only_ids=None):
    sql = """
        SELECT j.job_id, j.title, j.description,
               GROUP_CONCAT(s.name, ', ') AS skills
        FROM jobs j
        JOIN job_skills js ON js.job_id = j.job_id
        JOIN skills s ON s.skill_id = js.skill_id
        GROUP BY j.job_id
        ORDER BY j.job_id
    """

    rows = con.execute(sql).fetchall()

    if only_ids is not None:
        rows = [r for r in rows if r["job_id"] in only_ids]

    ids = [r["job_id"] for r in rows]
    texts = [
        f"{r['title']}. {r['description']} Skills: {r['skills']}"
        for r in rows
    ]

    return ids, texts


def sync(db_path="jobs.db"):
    con = connect(db_path)

    if os.path.exists(INDEX_PATH):
        data = np.load(INDEX_PATH)
        old_ids = data["ids"]
        old_vectors = data["vectors"]
    else:
        old_ids = np.array([], dtype="int64")
        old_vectors = np.empty((0, DIM), dtype="float32")

    indexed = set(old_ids.tolist())
    all_ids = {
        r[0] for r in con.execute("SELECT job_id FROM jobs")
    }

    new_ids = all_ids - indexed

    if not new_ids:
        print("Index already up to date:", len(old_ids), "jobs")
        return

    ids, texts = job_texts(con, new_ids)
    new_vectors = embed(texts)

    all_ids_array = np.concatenate([
        old_ids,
        np.array(ids, dtype="int64")
    ])

    all_vectors = np.vstack([
        old_vectors,
        new_vectors
    ])

    np.savez(
        INDEX_PATH,
        ids=all_ids_array,
        vectors=all_vectors
    )

    print(
        f"Embedded {len(ids)} new jobs. "
        f"Index now has {len(all_ids_array)} jobs."
    )


if __name__ == "__main__":
    sync()
