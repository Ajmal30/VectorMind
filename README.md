# 🧠 Vectormind

Vectormind is an end-to-end **PDF-based Retrieval-Augmented Generation (RAG)** workflow that allows users to upload PDF documents of any size, automatically chunk and index their content, and query them through an interactive Streamlit UI.

Built using **LlamaIndex**, **Qdrant**, and **Inngest**, Vectormind enables scalable document ingestion, semantic search, and detailed, context-aware answer generation grounded entirely in the uploaded PDF files.

---

## 🚀 Features

- Upload PDFs of any size  
- Automatic text extraction and configurable chunking  
- Vector embedding and storage using Qdrant  
- Semantic search with user-controlled chunk retrieval  
- Detailed, source-grounded answers from PDF content  
- Event-driven ingestion and background workflows  
- Simple and interactive Streamlit interface  

---

## 🏗️ How It Works

1. Users upload PDF documents via the UI  
2. Documents are chunked and embedded using LlamaIndex  
3. Embeddings are stored in Qdrant  
4. Users submit a query and define the number of chunks to retrieve  
5. Relevant chunks are used to generate a detailed response  

---

## 🧠 Tech Stack

- **LlamaIndex** – Document parsing, chunking, and RAG  
- **Qdrant** – Vector database for embeddings  
- **Inngest** – Event-driven ingestion and background processing  
- **Streamlit** – Interactive user interface  
- **Python** – Core implementation  

---

## ▶️ Quick Start

```bash
git clone https://github.com/your-username/vectormind.git
cd vectormind
pip install -r requirements.txt
docker run -p 6333:6333 qdrant/qdrant
streamlit run app.py
