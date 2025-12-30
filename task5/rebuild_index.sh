#!/bin/bash
set -e

echo "Rebuilding chunks from task2/knowledge_base..."
python3 ../task3/chunk_documents.py

echo "Rebuilding FAISS index..."
python3 ../task3/build_faiss_index.py

echo "Index rebuilt successfully."
