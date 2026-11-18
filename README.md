# Agentic Incident Intelligence & Resolution System

An Agentic RAG-based system for investigating and resolving technical incidents using internal knowledge, evidence evaluation, query refinement, and external web search when required.

## Overview

The system helps software engineers, DevOps/SRE teams, and technical support teams investigate technical incidents by retrieving relevant information from an internal knowledge base and generating evidence-grounded responses.

Unlike a basic RAG system that retrieves documents once and immediately generates an answer, this project evaluates the retrieved evidence before answering. If the available evidence is insufficient, the system can refine the query and retry retrieval or use external web search as a fallback.

## Problem

Traditional RAG systems can produce unreliable answers when:

- Relevant information is not retrieved.
- Retrieved documents do not contain enough evidence.
- The internal knowledge base is incomplete or outdated.
- The user's query is ambiguous.
- The system generates an answer without verifying the retrieved evidence.

This project addresses these limitations by introducing an agentic workflow that can evaluate evidence, refine queries, and use additional sources when necessary.

## Core Workflow

```text
User Incident
      ↓
Query Analysis
      ↓
Internal Knowledge Retrieval
      ↓
Evidence Evaluation
      ↓
 ┌───────────────┐
 │ Evidence Good?│
 └───────┬───────┘
     Yes │ No
         │
         ↓
   Query Refinement
         ↓
      Retry
         ↓
 External Web Search
         ↓
 Evidence Evaluation
         ↓
    Final Response
```

The workflow will be implemented using **LangGraph**.

## Key Features

- Internal knowledge-base retrieval
- Evidence evaluation
- Query refinement and retry
- External web-search fallback
- Source-grounded responses
- Agentic workflow orchestration
- Document ingestion
- Investigation history
- Execution tracing
- FastAPI backend
- Web-based interface

## Example Use Case

A developer could ask:

> "Our authentication service started returning 401 errors after a deployment. What should I investigate?"

The system searches the internal knowledge base for relevant architecture documentation, troubleshooting guides, and historical incidents.

If the retrieved evidence is insufficient, the system can refine the search and, when necessary, use external sources before producing the final response.

## Knowledge Base

The knowledge base will contain technical documentation such as:

- Architecture documentation
- Troubleshooting runbooks
- Historical incident reports
- Service and API documentation
- Engineering policies

The documents will be processed, split into chunks, embedded, and stored in a vector database for retrieval.

## Technology Stack

### Backend
- Python
- FastAPI

### AI / Agentic Workflow
- LangGraph
- LangChain
- OpenAI
- Tavily

### Vector Database
- Pinecone

### Document Processing
- PyPDF
- Python-DOCX
- LangChain Text Splitters

### Frontend
- HTML
- CSS
- JavaScript

## Project Structure

```text
agentic-incident-intelligence/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── ingestion/
│   ├── retrieval/
│   ├── services/
│   └── utils/
│
├── knowledge_base/
│
├── tests/
│
├── frontend/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

> The project structure may evolve as development progresses.

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd agentic-incident-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add the required API keys and configuration.

```env
OPENAI_API_KEY=
PINECONE_API_KEY=
TAVILY_API_KEY=
```

Additional environment variables will be added as the implementation develops.

### 5. Run the application

```bash
uvicorn main:app --reload
```