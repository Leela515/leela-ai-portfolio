# AI Research Assistant

# Project Overview

The AI Research Assistant was designed to solve the problem of research-grounded question answering over academic papers.

Traditional chatbots can generate fluent responses but often hallucinate or produce unsupported claims. The goal of this project was to build a Retrieval-Augmented Generation (RAG) system capable of:

* retrieving relevant academic papers,
* parsing and indexing technical documents,
* answering questions using retrieved evidence,
* generating grounded citations,
* and verifying answer faithfulness using a critic layer.

The project focused on reliable research assistance.

---

# System Design

The project was designed as a production-style academic RAG assistant with local AI inference.

The architecture combined:

* backend APIs,
* document parsing,
* semantic retrieval,
* vector search,
* citation validation,
* and answer verification workflows.

The system was intentionally built with modular engineering principles to support scalability and future retrieval improvements.

---

# Technology Stack

This section describes the technologies, frameworks, libraries, tools, and models used in the AI Research Assistant project.

## Backend & APIs

* Python
* FastAPI

## Retrieval & Vector Search

* FAISS
* sentence-transformers (`all-MiniLM-L6-v2`)

## LLM Inference

* Ollama
* Llama3

## Document Processing

* Docling

## Machine Learning & NLP

* PyTorch
* Transformers

---

# Retrieval Pipeline

The retrieval workflow followed a full RAG architecture:

Research Papers (PDFs)
↓
PDF Parsing using Docling
↓
Section-aware paragraph chunking
↓
Embedding generation using sentence-transformers
↓
FAISS vector indexing
↓
Semantic retrieval + diversified retrieval
↓
Context-aware prompt construction
↓
Answer generation using Llama3
↓
Critic review + citation validation
↓
Final grounded response

The system retrieves semantically relevant chunks first and generates answers strictly from retrieved evidence.

---

# Chunking Strategy

The final implementation used a:

* section-aware paragraph chunking strategy,
* sentence-boundary splitting,
* and contextual overlap.

The chunking pipeline:

* preserved document section structure,
* prioritized paragraph boundaries,
* filtered low-quality chunks,
* avoided reference-only sections,
* and reduced semantic fragmentation across chunk boundaries.

This produced significantly cleaner retrieval compared to naive fixed-window chunking.

---

# Retrieval Features

## Dense Semantic Retrieval

The system primarily used dense retrieval with embeddings and FAISS vector search.

## Diversified Retrieval

The pipeline implemented diversified retrieval and per-paper balancing to avoid excessive retrieval from the same document.

## Metadata-Aware Retrieval

The system tracked:

* paper identifiers,
* chunk identifiers,
* section metadata,
* chunk scores,
* and retrieval previews.

---

# Citation System

The assistant enforced:

* grounded citations,
* structured source references,
* citation validation,
* and citation cleanup workflows.

A citation validator checked whether generated citations aligned with retrieved source chunks.

---

# Evaluation & Verification

The project included:

* retrieval inspection,
* confidence scoring,
* citation validation,
* critic-based answer verification,
* and manual retrieval quality evaluation.

Planned future evaluation metrics included:

* recall@k,
* hit@k,
* faithfulness,
* citation accuracy,
* and automated RAG evaluation pipelines.

---

# Technical Challenges

One of the biggest engineering challenges was maintaining:

* answer faithfulness,
* retrieval quality,
* and citation accuracy.

Key problems included:

* noisy PDF parsing,
* fragmented retrieval,
* hallucinated citations,
* duplicated retrieval results,
* and unsupported LLM claims.

To address these issues, the system evolved into a more production-oriented RAG architecture with:

* improved chunking,
* metadata-aware retrieval,
* confidence scoring,
* citation validation,
* diversified retrieval,
* and critic-based answer verification.

---

# What Makes This Different From A Basic Chatbot

Unlike a generic chatbot, this system:

* retrieves evidence from academic documents,
* grounds responses in retrieved context,
* validates citations,
* measures confidence,
* and verifies generated answers using a critic layer.

The project focused on reliable evidence-grounded research assistance rather than unrestricted conversation.

---

# Engineering Focus

This project combined:

* RAG system design,
* backend engineering,
* retrieval optimization,
* local LLM inference,
* evaluation workflows,
* and production-oriented AI engineering practices.
