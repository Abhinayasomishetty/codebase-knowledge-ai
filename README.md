# 🚀 Codebase Knowledge AI

An AI-powered system that enables developers to understand and query a codebase using natural language.

---

## 🧠 Overview

Understanding large codebases is time-consuming and complex.  
This project solves that problem by allowing users to ask questions about code and retrieve relevant answers using semantic search and AI.

---

## ✨ Features

- 🔍 Semantic code search (not just keywords)
- 🤖 Natural language queries
- ⚡ Fast retrieval using FAISS
- 📂 Automatic code parsing and chunking
- 🧠 Embedding-based similarity matching

---

## 🛠️ Tech Stack

- Python
- Sentence Transformers
- FAISS
- NumPy

---

## ⚙️ How It Works

1. Reads all Python files from the project
2. Splits code into function-level chunks
3. Converts code into embeddings
4. Stores embeddings in FAISS index
5. Converts user query into embedding
6. Retrieves most relevant code snippets

---

## 📂 Project Structure
codebase-knowledge-ai/ │ ├── app.py ├── main.py ├── my_project/ │   ├── login.py │   ├── register.py │   ├── db.py │   ├── auth_service.py │   ├── utils.py │ ├── requirement.txt ├── README.md └── .gitignore

---

## ▶️ How to Run

1. Install dependencies:
pip install -r requirement.txt
2. Run the application:
python app.py
---

## 💡 Example Query

Ask:
How does authentication work?
Get:
- Relevant code snippets
- Context-aware explanation

---

## 🚀 Future Improvements

- Web UI (Streamlit / React)
- Multi-language support
- Chat-based interaction
- Cloud deployment

---

## 👩‍💻 Author

Abhinaya Somishetty
