# Scientific Literature AI Assistant

科学論文解析のための最小構成の多言語 RAG（Retrieval-Augmented Generation）プロトタイプ。

使用技術：
- FastAPI
- OpenAI API
- ChromaDB
- semantic retrieval（意味検索）
- LLM 質問応答

Live demo:

https://scientific-literature-ai-rag-assistant.onrender.com/docs

---

# クイックデモ

1. `/ask` を開く
2. 「Try it out」をクリック
3. 質問を入力
4. 「Execute」をクリック

デモでは、起動時にサンプル科学論文が自動的に読み込まれます。

---

# 質問例

```text
この論文で扱われている物質を教えてください。
```

```text
この論文の主な目的を日本語で説明してください。
```

```text
有効ハミルトニアンの役割を説明してください。
```

---

# 主な機能

- 科学論文 PDF 解析
- 日本語・英語質問応答
- semantic retrieval（RAG）
- OpenAI embeddings
- ベクトルデータベース検索
- FastAPI バックエンド
- Docker デプロイ

---

# 使用技術

- Python
- FastAPI
- OpenAI API
- ChromaDB
- PyMuPDF
- Docker

---

# 使用論文

Jean-Baptiste Morée and Ryotaro Arita,  
“Universal chemical formula dependence of ab initio low-energy effective Hamiltonian in single-layer carrier-doped cuprate superconductors: Study using a hierarchical dependence extraction algorithm”,  
Physical Review B 110, 014502 (2024).

---

# 現時点での制限

- 図表は完全には解析できない
- OCR 未実装
- 回答は retrieval された chunk のみを利用