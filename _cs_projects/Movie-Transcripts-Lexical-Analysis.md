---
title: "Movie Transcripts Lexical Analysis"
layout: single
classes: wide
excerpt: "Lexical algorithms and research using the Movie Transcripts 59k Kaggle dataset—trie-based similarity, divergence timelines, and temporal vocabulary evolution."
---

## Overview

A research-oriented NLP project that explores how vocabulary in cinema evolves over time using the [Movie Transcripts 59k Kaggle dataset](https://www.kaggle.com/datasets/fayaznoor10/movie-transcripts-59k). The project connects NLP techniques to film studies: vocabulary choices in scripts reflect genre, era, and authorial style. The Lexical Trie enables efficient computation at scale (59k movies), and the divergence visualization makes abstract lexical relationships interpretable.

**Why recruiters care:** Demonstrates algorithmic thinking, custom data structure design, NLP tooling (NLTK), and the ability to turn research ideas into working software with clear visualizations.

## Key Features

| Feature | Description |
|---------|-------------|
| **Lexical Trie** | Custom prefix tree for efficient word storage, similarity computation, and vocabulary analysis |
| **Divergence Timeline** | Interactive branching timeline showing how movie vocabularies diverge over time |
| **Similarity Metrics** | Jaccard and Cosine similarity for clustering lexically similar movies |
| **Temporal Clustering** | Groups movies by vocabulary + temporal proximity (within configurable year windows) |
| **Visualization** | Static PNG and interactive HTML (Plotly) outputs |
| **Kaggle Integration** | Uses Kaggle API / kagglehub for dataset loading |

## How It Works

1. **Data Loading**: Fetches Movie Transcripts 59k dataset (movie titles, transcripts, metadata).
2. **Trie Construction**: Builds a Lexical Trie from all transcript words; tracks word counts and which movies contain each word.
3. **Lexical Profiles**: Each movie gets a vocabulary profile from the trie.
4. **Clustering**: Movies are clustered by Jaccard/Cosine similarity and temporal proximity.
5. **Divergence Tree**: Constructs a tree structure showing where vocabulary branches diverge.
6. **Visualization**: Renders branching timeline (year on x-axis, divergence on y-axis) with color-coded clusters.

## Technical Architecture

### Lexical Trie (`lexical_trie.py`)

- **Insert:** O(m) per word (m = word length)
- **Search / Prefix:** O(m)
- **Similarity:** Jaccard and Cosine computed from trie-derived word sets
- Tracks `word_count`, `movies` per node for downstream analysis

### Divergence Timeline (`divergence_timeline.py`)

- Builds lexical profiles per movie
- Configurable `similarity_threshold` and `min_movies_per_cluster`
- Outputs: `divergence_timeline.png`, `divergence_timeline.html`, `divergence_tree.json`

### Project Structure

```
├── lexical_trie.py              # Trie data structure
├── divergence_timeline.py       # Main divergence pipeline
├── temporal_evolution_analysis.py  # Temporal language metrics
├── explore_dataset.py           # Dataset exploration
└── requirements.txt             # NLTK, pandas, kagglehub, etc.
```

## Algorithms

### Jaccard Similarity
```
J(A, B) = |A ∩ B| / |A ∪ B|
```
Measures vocabulary overlap (0 = different, 1 = identical).

### Cosine Similarity
Uses word frequencies from the trie; weighted by how common words are across movies.

### Clustering
- Temporal clustering: groups by lexical similarity + year proximity (e.g., 20-year window)
- Divergence tree: connects clusters by similarity and time; splits represent vocabulary divergence events

## Research Applications

- **Genre Evolution** — Track how Action, Drama, Comedy vocabularies diverge over decades
- **Director Styles** — Compare lexical fingerprints of different directors
- **Cultural Periods** — Identify lexical shifts (e.g., tech terms in 2000s)
- **Innovation Tracking** — Find movies with unusually high divergence (lexical innovators)

## Skills & Technologies

- **Python** — Core logic, data processing
- **NLTK** — Tokenization, stopwords, POS tagging
- **Pandas** — Data handling
- **Kaggle** — Dataset access (kagglehub)
- **Plotly** — Interactive visualizations
- **Data Structures** — Custom Trie implementation

## Repository

[View on GitHub](https://github.com/kianils)
