# Scientific Literature AI Assistant

A minimal multilingual RAG prototype for scientific paper analysis.

This project allows users to upload a PDF paper, index its text, and ask questions about its content using a FastAPI backend, OpenAI embeddings, a ChromaDB vector database, and an OpenAI chat model.

## Features

- Upload and index scientific PDF papers
- Extract text using PyMuPDF
- Split papers into overlapping text chunks
- Create embeddings with OpenAI embeddings
- Store vectors locally with ChromaDB
- Ask questions about uploaded papers
- Retrieve relevant paper chunks
- Generate answers using an OpenAI chat model
- Supports English and Japanese questions/answers
- Designed as a small portfolio project for AI/data engineering

## Tech Stack

- Python
- FastAPI
- OpenAI API
- ChromaDB
- PyMuPDF
- Docker
- Uvicorn

## Project Structure

```text
.
„¥„Ÿ„Ÿ app.py
„¥„Ÿ„Ÿ requirements.txt
„¥„Ÿ„Ÿ Dockerfile
„¥„Ÿ„Ÿ .gitignore
„¥„Ÿ„Ÿ .env.example
„¤„Ÿ„Ÿ papers/