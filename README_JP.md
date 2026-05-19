# Scientific Literature AI Assistant

科学論文解析のための最小構成の多言語 RAG（Retrieval-Augmented Generation）プロトタイプ。

本プロジェクトでは、PDF形式の科学論文をアップロードし、FastAPI・OpenAI Embeddings・ChromaDB・LLM を用いて論文内容に対する質問応答を行うことができます。

## 主な機能

- 科学論文 PDF のアップロードとインデックス化
- PyMuPDF を用いた PDF テキスト抽出
- 論文テキストのチャンク分割
- OpenAI Embeddings によるベクトル化
- ChromaDB を用いたベクトルデータベース管理
- 論文内容に関する質問応答
- 関連箇所の意味検索（semantic retrieval）
- OpenAI LLM を用いた回答生成
- 日本語・英語による質問／回答対応
- AI／データエンジニアリング学習用ミニプロジェクト

## 使用技術

- Python
- FastAPI
- OpenAI API
- ChromaDB
- PyMuPDF
- Docker
- Uvicorn

## ディレクトリ構成

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .env.example
└── papers/