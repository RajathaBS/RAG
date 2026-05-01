# Building a RAG System with LangChain and FastAPI

This project demonstrates how to build a **Retrieval-Augmented Generation (RAG)** system using **LangChain** and **FastAPI**. A RAG system improves the quality of language model responses by retrieving relevant information from external data sources before generating an answer.

---

## What Is Retrieval-Augmented Generation (RAG)?

Retrieval-Augmented Generation (RAG) combines:

- **Information retrieval** from custom data sources
- **Natural language generation** using large language models

This approach produces responses that are:
- More accurate
- Context-aware
- Grounded in your own documents

---

## Architecture Overview

A typical RAG pipeline consists of the following components:

1. Document Loaders  
2. Text Splitting  
3. Indexing (Embeddings)  
4. Retrieval  
5. Generation  

---

## Core Components

### Document Loaders

Document loaders ingest data from multiple sources such as:
- Text files
- PDFs
- Databases

They convert raw data into a structured format that can be processed by the rest of the pipeline.

---

### Text Splitting

Loaded documents are split into smaller chunks to:
- Improve retrieval accuracy
- Stay within language model context limits
- Enable fine-grained searches

---

### Indexing

Each text chunk is transformed into a vector embedding and stored in a vector database. Indexing enables:
- Fast similarity search
- Efficient document retrieval at query time

---

### Retrieval Models

#### Vector Stores
Vector stores hold embeddings and support similarity search to find relevant chunks.

#### Retrievers
Retrievers:
1. Convert a user query into an embedding
2. Search the vector store
3. Return the most relevant documents

---

### Generative Models

The language model:
- Combines retrieved context with the user query
- Generates a coherent and informed response
- Produces answers grounded in your data and model knowledge

---

## Setup Instructions

### Prerequisites

- **Python 3.10 or later**

Verify your Python version:
```bash
python --version


python3 -m venv ragenv

# Linux / macOS
source ragenv/bin/activate

# Windows
ragenv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Environment Variables
Create a .env file and add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here

Running the Application
Start the FastAPI server:
uvicorn app.main:app --reload

Open your browser and visit:
http://127.0.0.1:8000/docs

Project Structure (Example)
.
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── rag/
├── data/
├── requirements.txt
├── .env
└── README.md

Credits and Inspiration
Inspired by the DataCamp tutorial by Dr. Ana Rojo‑Echeburúa:

Building a RAG System with LangChain and FastAPI
https://www.datacamp.com/tutorial/building-a-rag-system-with-langchain-and-fastapi

Future Improvements

Add authentication
Add streaming responses
Swap vector stores (FAISS, Chroma, Pinecone)
Add evaluation metrics and logging
Dockerize and deploy the application
