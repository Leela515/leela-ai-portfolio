# Leela AI Portfolio — Architecture

# Overview

This portfolio is designed as a modular AI system 

The architecture combines:

* a modern frontend application,
* a FastAPI backend,
* a Retrieval-Augmented Generation (RAG) pipeline,
* and vector-based document retrieval

to create an interactive portfolio experience.

The system is designed to allow recruiters and engineers to:

* explore projects,
* inspect technical details,
* and interact with an AI assistant capable of answering questions grounded in my portfolio content.

---

# High-Level System Flow

User
↓
Frontend Application
↓
FastAPI Backend
↓
RAG Retrieval Pipeline
↓
Vector Search
↓
LLM Response Generation
↓
Grounded Response with Citations

---

# Frontend Architecture

## Responsibilities

The frontend is responsible for:

* rendering portfolio pages,
* displaying project information,
* handling recruiter interactions,
* rendering AI assistant responses,
* and displaying citations and technical content.

## Planned Stack

* Next.js
* TailwindCSS
* Framer Motion

---

# Backend Architecture

## Responsibilities

The backend will act as the orchestration layer between:

* frontend requests,
* retrieval systems,
* and answer generation.

The backend will also manage:

* API routes,
* prompt construction,
* citation generation,
* and retrieval workflows.

## Planned Stack

* FastAPI
* Pydantic
* Uvicorn

---

# Retrieval Pipeline

The RAG pipeline is one of the core systems in this portfolio.

## Responsibilities

The retrieval system will:

* ingest portfolio documents,
* chunk content,
* generate embeddings,
* retrieve relevant context,
* and prepare grounded information for answer generation.

## Knowledge Sources

The retrieval system will use:

* resume content,
* project writeups,
* architecture documents,
* research summaries,
* and technical notes.

---

# Vector Search

The vector search layer will store embeddings generated from portfolio documents.

This enables semantic retrieval of:

* project details,
* technical explanations,
* implementation decisions,
* and engineering experience.

---

# Answer Generation

The answer generation layer will:

* receive retrieved context,
* construct grounded prompts,
* generate concise responses,
* and return citation-supported answers.

The system is designed to reduce hallucinations by restricting answers to retrieved portfolio content.

---

# Deployment Architecture

## Frontend Deployment

* Vercel

## Backend Deployment

* Railway / Render / Azure

## Containerization

* Docker

## CI/CD

* GitHub Actions

---

# Future Improvements

Future versions of the system may include:

* streaming responses,
* evaluation dashboards,
* monitoring and telemetry,
* query analytics,
* authentication,
* and multi-agent workflows.

---

# Design Philosophy

I want this portfolio to function as both:

* a personal portfolio,
* and a demonstration of production-oriented AI engineering practices.

The architecture is intentionally modular so that individual components such as:

* retrieval,
* APIs,
* frontend systems,
* and evaluation pipelines

can evolve independently over time.
