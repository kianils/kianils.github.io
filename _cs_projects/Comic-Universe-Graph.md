---
title: "Comic Universe Graph"
layout: single
classes: wide
excerpt: "Knowledge graph of comic characters, series, and crossovers using Azure Cosmos DB (Gremlin), Azure Functions API, and interactive graph visualization."
---

## Overview

A cloud-native knowledge graph that models comic universes (Marvel, DC, etc.) as a network of characters, issues, volumes, arcs, and events. Comic universes are inherently graph-shaped: characters appear in issues, team up, face villains, and participate in arcs and events. Modeling this as a graph enables powerful queries (paths, timelines, co-occurrence) that would be cumbersome with relational DBs—questions like "First meeting of Spider-Man and Wolverine?" or "Path between two characters via shared issues" become graph traversals.

**Why recruiters care:** Demonstrates graph databases, cloud architecture (Azure), API design, and full-stack development—skills directly applicable to recommendation systems, content graphs, and data platforms.

## Key Features

| Feature | Description |
|---------|-------------|
| **Graph Database** | Azure Cosmos DB (Gremlin API) stores vertices (characters, issues, volumes, arcs, events, teams) and edges (APPEARS_IN, TEAMED_WITH, VILLAIN_OF, etc.) |
| **Path Finding** | Shortest path between characters via shared issues/teams |
| **Timeline** | Chronological list of issues/arcs/events for a character |
| **Issues in Common** | Finds issues featuring multiple specified characters |
| **Search** | Full-text search across characters, volumes, arcs |
| **Data Ingestion** | Scripts for Comic Vine API and Marvel API; optional hand-curated JSON/CSV |
| **Interactive Frontend** | Cytoscape.js / D3 / vis-network for graph visualization |

## How It Works

1. **Data Ingestion**: Python scripts fetch from Comic Vine and Marvel APIs; normalize to a common schema; insert vertices and edges via Gremlin.
2. **Graph Queries**: Azure Functions execute Gremlin traversals for path, timeline, search, and subgraph endpoints.
3. **API Layer**: HTTP-triggered Functions expose REST APIs (e.g., `/api/path?from=Spider-Man&to=Wolverine`).
4. **Frontend**: Static Web App renders the graph; users search, pick characters, and view paths or timelines.

## Technical Architecture

### Graph Schema (Cosmos DB Gremlin)

**Vertices:** `character`, `issue`, `volume`, `arc`, `event`, `team`  
**Edges:** `APPEARS_IN`, `TEAMED_WITH`, `VILLAIN_OF`, `PART_OF_ARC`, `PART_OF_EVENT`, `IN_VOLUME`, `MEMBER_OF`

### API Design (Azure Functions)

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/path` | `from`, `to` → shortest path via shared issues/teams |
| GET | `/api/timeline` | `character` → chronological issues/arcs/events |
| GET | `/api/issues-in-common` | `chars` → issues featuring all |
| GET | `/api/search` | `q` → search characters/volumes/arcs |
| GET | `/api/graph` | `ids`, `depth` → subgraph for visualization |
| GET | `/api/character/{id}` | Character details + adjacent nodes |

### Project Structure

```
comic_universe_graph/
├── PLAN.md          # Architecture, schema, phases
├── data/            # Seed JSON, schema examples
├── scripts/         # ingest_comicvine.py, ingest_marvel.py, seed_from_json.py
├── api/             # Azure Functions (path, timeline, search, graph)
└── web/             # Static Web App frontend (Cytoscape.js / D3)
```

## Azure Resources

- **Cosmos DB** — Gremlin API, graph container
- **Azure Functions** — Python or Node.js, HTTP triggers
- **Static Web Apps** — Frontend hosting
- **Key Vault** — API keys (Comic Vine, Marvel), Cosmos connection
- **Managed Identity** — Secure access to Key Vault and Cosmos (no keys in code)
- **Blob Storage** (optional) — Cache API responses; respect rate limits

## Example Gremlin Queries

```groovy
// Character appears in issue
g.V().has('character', 'id', 'cv-spider-man')
  .addE('APPEARS_IN').to(g.V().has('issue', 'id', 'marvel-asymmetric-1'))
  .property('role', 'hero')

// Shortest path between characters
g.V().has('character', 'name', 'Spider-Man')
  .repeat(both().simplePath())
  .until(has('character', 'name', 'Wolverine'))
  .path().limit(1)
```

## Skills & Technologies

- **Azure Cosmos DB** — Gremlin API, graph modeling
- **Azure Functions** — Serverless HTTP APIs
- **Gremlin** — Graph traversal queries
- **Python** — Ingest scripts, API logic
- **JavaScript** — Cytoscape.js, D3, vis-network
- **REST API** — Design, documentation

## Repository

[View on GitHub](https://github.com/kianils)
