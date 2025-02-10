import faiss
import numpy as np
import json

# Load the stored FAISS index
index = faiss.read_index("vector_database.index")  # Change to your actual FAISS index file

# Load the data file
with open("SAMBHV STEEL TUBES LIMITED_parsed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Function to search for similar vectors
def search(query_vector, top_k=5):
    query_vector = np.array([query_vector], dtype="float32")
    distances, indices = index.search(query_vector, top_k)
    
    results = []
    for i in range(top_k):
        idx = indices[0][i]
        if idx < len(data):  # Ensure index is within bounds
            results.append({"index": idx, "distance": float(distances[0][i]), "content": data[idx]})
    
    return results

# Example query: Use an actual embedding from your dataset
query_embedding = data[0]["embedding"]  # Replace with an actual vector

# Perform search
results = search(query_embedding, top_k=5)

# Print results
for i, result in enumerate(results):
    print(f"\n🔍 Result {i+1} - Distance: {result['distance']}\n{json.dumps(result['content'], indent=2)}")
