import faiss
import numpy as np
import glob
import os

def store_embeddings_in_faiss(embeddings, index_filename):
    if len(embeddings) == 0:
        print(f"❌ No embeddings to store for {index_filename}.")
        return

    dim = len(embeddings[0])  # Get the embedding dimension
    index = faiss.IndexFlatL2(dim)

    # Convert embeddings to numpy array and add them to FAISS
    index.add(np.array(embeddings).astype(np.float32))

    try:
        faiss.write_index(index, index_filename)
        print(f"✅ FAISS index saved: {index_filename} with {index.ntotal} embeddings.")
    except Exception as e:
        print(f"❌ Error saving FAISS index: {e}")

if __name__ == "__main__":
    embedding_files = glob.glob("*_embeddings.npy")  # Find all embedding files
    if not embedding_files:
        print("❌ No embedding files found!")
    else:
        for embedding_file in embedding_files:
            try:
                embeddings = np.load(embedding_file, allow_pickle=True)

                if embeddings.shape[0] == 0:
                    print(f"❌ Error: {embedding_file} is empty.")
                else:
                    index_filename = embedding_file.replace("_embeddings.npy", "_faiss.index")
                    store_embeddings_in_faiss(embeddings, index_filename)

            except Exception as e:
                print(f"❌ Error loading {embedding_file}: {e}")
