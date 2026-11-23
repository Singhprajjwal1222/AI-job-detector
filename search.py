
"""Stage 2b: Semantic search with strict filters."""

import numpy as np
from queries import connect
from embedder import embed
from index_jobs import INDEX_PATH


def search(query, k=5, level=None, location=None, pool=50):

    data = np.load(INDEX_PATH)

    vectors = data["vectors"]
    ids = data["ids"]

    query_vector = embed([query])[0]

    # Cosine similarity
    scores = vectors @ query_vector

    # Check all jobs when filters are provided
    count = len(scores) if level or location else min(pool, len(scores))

    top_indices = np.argsort(scores)[::-1][:count]

    con = connect()
    results = []

    try:
        for idx in top_indices:

            score = float(scores[idx])
            job_id = int(ids[idx])

            row = con.execute("""
                SELECT j.job_id, j.title, c.name AS company,
                       j.location, j.experience_level
                FROM jobs j
                JOIN companies c ON c.company_id = j.company_id
                WHERE j.job_id = ?
            """, (job_id,)).fetchone()

            if row is None:
                continue

            # Strict experience filter
            if level and row["experience_level"].lower() != level.lower():
                continue

            # Strict location filter
            if location and row["location"].lower() != location.lower():
                continue

            results.append({
                **dict(row),
                "similarity": round(score, 3),
                "final_score": round(score, 3)
            })

            if len(results) >= k:
                break

    finally:
        con.close()

    return results


if __name__ == "__main__":

    q = "Python SQL machine learning internship"

    for r in search(q, k=5, level="intern", location="Delhi"):
        print(r)
