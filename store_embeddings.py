import os
import faiss
import json
import numpy as np

#  Configurations
BASE_DIR = os.getcwd()
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_index.idx")
METADATA_PATH = os.path.join(BASE_DIR, "metadata.json")

#  Get all embedding files
embedding_files = [f for f in os.listdir(BASE_DIR) if f.endswith("_embeddings.npy")]

metadata = {}
index = None
embedding_dim = 384  # MiniLM model

for i, embedding_file in enumerate(embedding_files):
    print(f" Processing {embedding_file}...")

    # Load embeddings
    embeddings = np.load(os.path.join(BASE_DIR, embedding_file))

    if index is None:
        index = faiss.IndexFlatL2(embedding_dim)
    
    # Store metadata
    for j in range(len(embeddings)):
        metadata[str(i * 100 + j)] = {
            "file": embedding_file.replace("_embeddings.npy", "_summarized.json"),
            "index": i * 100 + j
        }

    index.add(embeddings)

# Save FAISS index
faiss.write_index(index, FAISS_INDEX_PATH)
with open(METADATA_PATH, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=4)

print(f" Successfully stored {len(metadata)} embeddings in FAISS!")
