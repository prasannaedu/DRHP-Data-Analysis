import faiss

index = faiss.read_index("vector_database.index")
print(f" FAISS contains {index.ntotal} embeddings.")
