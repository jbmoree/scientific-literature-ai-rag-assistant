import os
import fitz  # PyMuPDF
import chromadb
from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI(title="Scientific Literature AI Assistant")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma = chromadb.PersistentClient(path="./chroma_db")
collection = chroma.get_or_create_collection(name="papers")


def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text


def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 200):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks


def embed(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs("papers", exist_ok=True)
    file_path = f"papers/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text)

    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[f"{file.filename}_{i}"],
            documents=[chunk],
            embeddings=[embed(chunk)],
            metadatas=[{"source": file.filename, "chunk": i}]
        )

    return {"message": "PDF uploaded and indexed", "chunks": len(chunks)}


@app.get("/ask")
def ask(question: str):
    question_embedding = embed(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=12
    )

    retrieved_chunks = results["documents"][0]
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a scientific literature assistant.
Answer ONLY using the context below.
If the answer is not in the context, say so clearly.
When materials, compounds, or datasets are mentioned,
extract their names explicitly and list them precisely.
If the answer is incomplete, say so.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "question": question,
        "answer": response.choices[0].message.content,
        "sources": results["metadatas"][0]
    }
