import os
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Configurations
BASE_DIR = os.getcwd()
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_index.idx")
METADATA_PATH = os.path.join(BASE_DIR, "metadata.json")
MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

# Load FAISS index
if not os.path.exists(FAISS_INDEX_PATH):
    raise ValueError(f" Error: FAISS index not found at {FAISS_INDEX_PATH}!")

index = faiss.read_index(FAISS_INDEX_PATH)

# Load metadata
with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

# User Input
query = input(" Enter search query: ")
query_embedding = model.encode([query], convert_to_numpy=True)

# Search in FAISS
D, I = index.search(query_embedding, k=5)  # Top 5 results

print("\n *Top Matching Summaries:*\n")

for i, idx in enumerate(I[0]):
    str_idx = str(idx)  # Convert to string for metadata lookup

    if str_idx in metadata:
        file_name = metadata[str_idx]["file"]
        index_in_file = metadata[str_idx]["index"]

        file_path = os.path.join(BASE_DIR, file_name)

        # Read the summarized JSON file
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                summaries = json.load(f)

            # Ensure index exists in the JSON file
            if 0 <= index_in_file < len(summaries):
                # Try 'summary' first, then fallback to 'key_findings'
                summary_text = summaries[index_in_file].get("summary") or summaries[index_in_file].get("key_findings", "❌ Summary not found.")
                
                print(f"{i+1}.  *Source:* {file_name}")
                print(f"    *Summary:* {summary_text}\n")
            else:
                print(f"{i+1}.  *Error:* Index {index_in_file} out of range in {file_name}\n")
        else:
            print(f"{i+1}.  *Error:* File {file_name} not found.\n")

    else:
        print(f"{i+1}.  *Metadata not found for index {idx}*\n")
