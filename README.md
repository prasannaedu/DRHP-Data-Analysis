# DRHP Data Analysis
📊 Parsing, Embedding, and Storing Large PDF Data in a Vector Database.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Generate & Store Embeddings](#Generate&storeembeddings)
- [Contributing](#contributing)
- [License](#license)
- [Query the Vector Database](#querythevectordatabase)
- [Extract Data from PDFs](#extractdatafrompdfs)
- [Extract Data from PDFs](#extractdatafrompdfs)
- [Project Structure](#projectstructure)
- 

## Introduction
• This project involves extracting, parsing, structuring, and embedding data from large PDF documents (Draft Red Herring Prospectus - DRHP) using Python. The structured data is stored in a vector database (FAISS) for efficient querying.

## Features
- Extract structured data (text & tables) from PDFs.
- Generate summaries & key findings using NLP models.
- Create vector embeddings for summaries.
- Store data in FAISS for fast similarity-based search.
- Query the vector database using natural language

## Installation

Clone the repository:
```bash
git clone https://github.com/prasannaedu/DRHP-Data-Analysis.git
cd DRHP-Data-Analysis
```
## Install dependencies
•Python (Primary Language)
•PyMuPDF (fitz) → Extracting text from PDFs
•pdfplumber → Extracting structured tabular data
•FAISS → Vector database for fast similarity search
•Hugging Face Transformers → Sentence Embeddings
•sentence-transformers → Generating vector embeddings
•NumPy / Pandas → Data processing
•JSON → Storing structured extracted data
•Git & GitHub → Version contro

##  Create a Virtual Environment:
python -m venv drhp_env
source drhp_env/bin/activate  # On macOS/Linux
drhp_env\Scripts\activate     # On Windows


##  Extract Data from PDFs
python scripts/extract_text.py
python scripts/extract_tables.py


## Generate & Store Embeddings
python scripts/generate_embeddings.py
python scripts/store_embeddings.py

## Query the Vector Database
python scripts/query_faiss.py


## Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.
Fork the repository

1.Create your feature branch (git checkout -b feature/AmazingFeature)

2.Commit your changes (git commit -m 'Add some AmazingFeature')

3.Push to the branch (git push origin feature/AmazingFeature)

4.Open a Pull Request

## Project Structure
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


## Table of Contents
- [Python](#Python)
- [PyMuPDF (fitz)](#PyMuPDF (fitz))
- [pdfplumber](#pdfplumber)
- [FAISS ](#FAISS )
- [Hugging Face Transformers ](#Hugging Face Transformers )
- [sentence-transformers](#sentence-transformers)
- [NumPy / Pandas](#NumPy/Pandas)
- [JSON](#JSON )
- [Git & GitHub  ](#Git&GitHub  )
  
