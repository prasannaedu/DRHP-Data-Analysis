## DRHP Data Analysis
📊 Parsing, Embedding, and Storing Large PDF Data in a Vector Database

📌 Overview
•This project involves extracting, parsing, structuring, and embedding data from large PDF documents (Draft Red Herring Prospectus - DRHP) using Python. The structured data is stored in a vector database (FAISS) for efficient querying.

## Key Features:
•Extract structured data (text & tables) from PDFs.
•Generate summaries & key findings using NLP models.
•Create vector embeddings for summaries.
•Store data in FAISS for fast similarity-based search.
•Query the vector database using natural language.

## Technologies Used:
•Python (Primary Language)
•PyMuPDF (fitz) → Extracting text from PDFs
•pdfplumber → Extracting structured tabular data
•FAISS → Vector database for fast similarity search
•Hugging Face Transformers → Sentence Embeddings
•sentence-transformers → Generating vector embeddings
•NumPy / Pandas → Data processing
•JSON → Storing structured extracted data
•Git & GitHub → Version control

📂 Project Structure:
📁 data analysis drhp
│── 📂 drhp_env/                 # Virtual environment (ignored in Git)
│── 📂 data/                      # Raw PDF files
│── 📂 parsed_data/               # Extracted & structured data
│── 📂 embeddings/                # Vector embeddings stored in .npy files
│── 📂 scripts/                   # Python scripts
│   ├── extract_text.py           # Extract text from PDFs
│   ├── extract_tables.py         # Extract tabular data
│   ├── generate_embeddings.py    # Generate embeddings from summaries
│   ├── store_embeddings.py       # Store embeddings in FAISS
│   ├── query_faiss.py            # Query the vector database
│── 📜 requirements.txt           # Dependencies
│── 📜 README.md                  # Project Documentation

## Setup & Installation:
1️. Clone the Repository
git clone https://github.com/prasannaedu/DRHP-Data-Analysis.git
cd DRHP-Data-Analysis

## Create a Virtual Environment:
python -m venv drhp_env
source drhp_env/bin/activate  # On macOS/Linux
drhp_env\Scripts\activate     # On Windows

## Install Dependencies:
--pip install -r requirements.txt

## How to Run:
--Extract Data from PDFs:
python scripts/extract_text.py
python scripts/extract_tables.py

## Generate & Store Embeddings:
python scripts/generate_embeddings.py
python scripts/store_embeddings.py

## Query the Vector Database:
python scripts/query_faiss.py
🔍 Example Query:
Revenue growth of Kumar Arch Tech Limited

## What I Learned:
• PDF Data Extraction: Using PyMuPDF & pdfplumber for structured parsing.
• Vector Embeddings: Generating sentence embeddings using sentence-transformers.
• FAISS Vector Database: Efficient similarity search on extracted summaries.
• Git & GitHub: Repository setup, version control, and troubleshooting push errors.
• Virtual Environments: Managing dependencies with venv.
• Performance Optimization: Handling large datasets efficiently.

## Features:
• Improve parsing for complex PDF structures.
• Enhance search query results using semantic search.
• Implement a web interface for querying FAISS easily.

## Author:
🔗 GitHub: prasannaedu
📧 Email: [udumulaprasannakumar.com]

















