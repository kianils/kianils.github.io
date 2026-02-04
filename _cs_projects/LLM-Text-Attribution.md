---
title: "LLM Text Attribution & Temporal Style Tracker"
layout: single
classes: wide
excerpt: "LLM-based text attribution system using prompt engineering and RAG to assess authenticity across writing styles, with version history and style drift detection."
---

## Overview

An LLM-powered tool that assesses whether text is human-written or AI-generated, and tracks how writing styles evolve over time. The system addresses a practical problem: distinguishing human-written from AI-generated text and tracking how authorship or style changes over multiple revisions. Uses prompt engineering to elicit reliable authenticity signals, feature extraction (sentence length, vocabulary richness) to quantify style, and threshold-based drift detection to flag meaningful changes without false positives.

**Why recruiters care:** Demonstrates full-stack development (Flask + React), prompt engineering, RAG integration, and handling of real-world NLP tasks with clear business value.

## Key Features

| Feature | Description |
|---------|-------------|
| **Authenticity Analysis** | Uses optimized LLM prompts to assess whether text is human or AI-generated |
| **Version History Tracking** | Stores multiple versions of documents with timestamps for longitudinal analysis |
| **Style Drift Detection** | Identifies significant changes in writing patterns between versions (configurable thresholds) |
| **Timeline Visualization** | Multi-panel graphs showing authenticity scores and style feature evolution over time |
| **REST API** | Flask backend with endpoints for analyze, documents, versions, drift detection |
| **React Frontend** | Modern UI with document tracking, analyzer, and dashboard components |

## How It Works

1. **Single-Text Analysis**: User submits text; system extracts style features (sentence length, lexical diversity, etc.) and runs LLM-based authenticity assessment.
2. **Version Tracking**: Multiple versions of the same document are stored with timestamps; each version is analyzed and metadata is persisted.
3. **Drift Detection**: Consecutive versions are compared to identify significant changes in style features and authenticity scores.
4. **Visualization**: Timeline graphs show authenticity score evolution, feature changes, and marked drift points.

## Technical Architecture

### Stack

- **Backend:** Python, Flask, Flask-CORS
- **Frontend:** React, Tailwind CSS
- **LLM:** OpenAI API (prompt engineering, RAG)
- **Storage:** JSON-based version history (extensible to DB)

### API Endpoints

- `POST /api/analyze` — Analyze a single text for authenticity
- `GET /api/documents` — List all tracked documents
- `GET /api/documents/<id>/versions` — Get version history
- `POST /api/drift` — Detect style drift between versions
- `GET /api/health` — Health check

### Project Structure

```
├── app.py                  # Flask API
├── temporal_tracker.py     # Core: version tracking, drift detection, LLM analysis
├── dataset_evaluator.py    # Dataset-level evaluation
├── frontend/               # React app
│   └── src/
│       ├── components/     # Analyzer, Dashboard, DocumentTracker
│       └── contexts/       # ThemeContext
└── temporal_data/          # Persisted version history
```

## Skills & Technologies

- **Python** — Backend logic, API design
- **Flask** — REST API, CORS
- **OpenAI API** — LLM integration, prompt engineering
- **RAG** — Retrieval-Augmented Generation for context
- **NLP** — Style feature extraction (lexical diversity, sentence structure)
- **React** — Frontend, component architecture
- **Tailwind CSS** — Styling

## Repository

[View on GitHub](https://github.com/kianils)
