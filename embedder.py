"""Turns text into vectors. Real mode uses a small sentence-transformers model (downloads ~90 MB once).
Set EMBEDDER=hash to use a crude offline stand-in (only for testing the plumbing)."""
import os, re, zlib
import numpy as np

DIM = 384  # all-MiniLM-L6-v2 output size

_model = None
def _real(texts):
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model.encode(texts, normalize_embeddings=True, show_progress_bar=False)

def _hash(texts):
    out = np.zeros((len(texts), DIM), dtype="float32")
    for i, t in enumerate(texts):
        for w in re.findall(r"[a-z0-9+#]+", t.lower()):
            out[i, zlib.crc32(w.encode()) % DIM] += 1.0
    norms = np.linalg.norm(out, axis=1, keepdims=True); norms[norms == 0] = 1
    return out / norms

def embed(texts):
    vecs = _hash(texts) if os.environ.get("EMBEDDER") == "hash" else _real(texts)
    return np.asarray(vecs, dtype="float32")
