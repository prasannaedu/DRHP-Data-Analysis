import json
import numpy as np
import glob
import os
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from sentence_transformers import SentenceTransformer
from concurrent.futures import ThreadPoolExecutor

# ✅ Set working directory
BASE_DIR = "C:/Users/udumularahul/Downloads/data analysis drhp"

if not os.path.exists(BASE_DIR):
    raise ValueError(f"❌ Error: Directory {BASE_DIR} does not exist!")
os.chdir(BASE_DIR)

# ✅ Enable GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.manual_seed(42)  

# ✅ Define models
SUMMARIZATION_MODEL = "facebook/bart-large-cnn"
EMBEDDING_MODEL = "paraphrase-MiniLM-L6-v2"

print(f"🔄 Loading summarization model on {device}...")
try:
    tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_MODEL)
    
    model = AutoModelForSeq2SeqLM.from_pretrained(SUMMARIZATION_MODEL)
    model = model.to(device)  

    for param in model.parameters():
        param.requires_grad = False  # Freeze model (not training)
        param.data = param.data.to(torch.float32) 

    summarizer = pipeline(
        "summarization",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1  # Use GPU if available
    )

    print("✅ Summarization model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading summarization model: {e}")
    exit(1)

# ✅ Load embedding model
embedding_model = SentenceTransformer(EMBEDDING_MODEL, device=device)

# ✅ Function to split text into chunks
def split_text(text, max_tokens=512):  
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        token_count = len(tokenizer.encode(word, add_special_tokens=False))
        if current_length + token_count > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = token_count
        else:
            current_chunk.append(word)
            current_length += token_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# ✅ Function to summarize a chunk (dynamic max_length handling)
def summarize_chunk(chunk):
    if len(chunk.split()) < 50:  
        return chunk  # Return original text if too short

    try:
        input_length = len(tokenizer.encode(chunk, add_special_tokens=False))
        max_summary_length = min(150, max(20, int(0.6 * input_length)))  # Adjust max_length dynamically

        summary = summarizer(chunk, max_length=max_summary_length, min_length=10, do_sample=False)
        return summary[0]['summary_text']

    except Exception as e:
        print(f"❌ Error summarizing chunk: {e}")
        return chunk  

# ✅ Function to generate key findings (parallel processing)
def generate_key_findings(text):
    if not text.strip():
        return "No content available."

    chunks = split_text(text)
    
    # Process multiple summaries in parallel
    with ThreadPoolExecutor(max_workers=4) as executor:
        summaries = list(executor.map(summarize_chunk, chunks))

    return " ".join(summaries)

# ✅ Function to generate text embeddings
def generate_text_embeddings(text):
    return embedding_model.encode(text, convert_to_numpy=True)

# ✅ Function to process JSON files
def process_embeddings():
    json_files = glob.glob("*.json")  
    if not json_files:
        print("❌ No JSON files found!")
        return

    for json_file in json_files:
        print(f"🚀 Processing {json_file}...")

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Error reading {json_file}: {e}")
            continue

        if not isinstance(data, list) or not data:
            print(f"❌ Error: {json_file} is empty or has an incorrect format. Skipping...")
            continue

        key_findings = []
        embeddings = []

        for section in data:
            if not isinstance(section, dict):
                print(f"⚠ Skipping invalid section (expected dict, got {type(section)}): {section}")
                continue

            full_text = section.get("full_text", "")
            summary = generate_key_findings(full_text)
            key_findings.append(summary)
            embedding = generate_text_embeddings(summary)
            embeddings.append(embedding)

        # ✅ Save results
        embeddings_filename = os.path.join(BASE_DIR, json_file.replace(".json", "_embeddings.npy"))
        json_output_filename = os.path.join(BASE_DIR, json_file.replace(".json", "_summarized.json"))

        np.save(embeddings_filename, embeddings)
        for i in range(len(data)):
            data[i]["key_findings"] = key_findings[i]

        with open(json_output_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"✅ Processed {json_file}: Summaries and embeddings saved to {BASE_DIR}.")

if __name__ == "__main__":
    process_embeddings()