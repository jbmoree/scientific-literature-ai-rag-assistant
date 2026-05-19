# Scientific Literature AI Assistant

Minimal multilingual RAG prototype for scientific paper analysis using:
- FastAPI
- OpenAI API
- ChromaDB
- semantic retrieval
- LLM question answering

Live demo:

https://scientific-literature-ai-rag-assistant.onrender.com/docs

---

# Quick Demo

1. Open `/ask`
2. Click "Try it out"
3. Enter a question
4. Click "Execute"

The demo automatically loads an example scientific paper at startup.

---

# Example Questions

## English

```text
Which materials does this paper study?
```

```text
Could you summarize the main motivation of the paper?
```

```text
Explain the role of the effective Hamiltonian.
```

# Features

- Scientific PDF analysis
- Multilingual English/Japanese Q&A
- Semantic retrieval (RAG)
- OpenAI embeddings
- Vector database search
- FastAPI backend
- Docker deployment

# Tech Stack

- Python
- FastAPI
- OpenAI API
- ChromaDB
- PyMuPDF
- Docker

# Example Paper

Jean-Baptiste Morée and Ryotaro Arita,
"Universal chemical formula dependence of ab initio low-energy effective Hamiltonian in single-layer carrier-doped cuprate superconductors: Study using a hierarchical dependence extraction algorithm",
Physical Review B 110, 014502 (2024).

# Current Limitations

- Figures/tables are not fully interpreted
- OCR is not implemented
- Answers are generated only from retrieved chunks