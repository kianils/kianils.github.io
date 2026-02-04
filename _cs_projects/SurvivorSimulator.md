---
title: "Survivor Simulator"
layout: single
classes: wide
excerpt: "Flask-based Survivor game simulator using real True Dork Times data, with tribal councils, alliances, challenges, and ML models for outcome prediction."
---

## Overview

Survivor Simulator is a full-stack web application that simulates the Survivor TV show using real contestant data from True Dork Times. The ML models use survivor-specific features: challenge performance, social connections, alliance membership, vote history, and morale. Training data comes from historical simulation runs, teaching the models which attribute combinations tend to lead to elimination vs. survival.

## Project Details

Survivor Simulator lets fans explore different season outcomes, run fantasy simulations, and predict elimination results using machine learning models. The project demonstrates end-to-end software engineering: data fetching and processing, game logic, web interfaces, and educational ML implementations.

## Key Features

| Feature | Description |
|---------|-------------|
| **Data Fetching** | Automatically fetches player data from True Dork Times for any season |
| **Player Initialization** | Processes Excel data into players with realistic stats (challenge skill, intelligence, social skill, luck, morale) |
| **Tribe Management** | Organize players into tribes with dynamic stats tracking |
| **Alliance System** | Form and manage alliances based on social graphs and player relationships |
| **Challenge System** | Run tribal and individual immunity challenges with outcome modeling |
| **Tribal Councils** | Simulate voting with strategic decision-making from alliances and attributes |
| **Machine Learning** | Perceptron and MLP models for predicting game outcomes |
| **Web Interface** | Flask-based app with tribe sorter, simulation views, and API endpoints |

## How It Works

1. **Data Collection**: Fetches season data from True Dork Times and processes it into player stats (challenge skill, intelligence, social skill, luck).
2. **Tribe Formation**: Players are randomly divided into tribes; stats update as the game progresses.
3. **Alliance Formation**: Alliances form from social graphs and player compatibility.
4. **Game Simulation**:
   - Challenges determine immunity winners
   - Tribal councils determine vote-outs based on alliances and attributes
   - Player stats (morale, votes received) update dynamically
5. **ML Prediction**: Perceptron and MLP models predict vote-out risk and outcomes from player features.

## Technical Architecture

### Project Structure

```
SurvivorSimulator/
├── app.py                      # Flask web application
├── game_engine.py              # Main game simulation engine
├── game_mechanics.py           # Core mechanics (challenges, voting)
├── alliance_sim.py             # Alliance formation algorithms
├── ml_models.py                # Perceptron & MLP implementations
├── initializePlayers.py        # Player initialization from Excel
├── SurvivorData.py             # Data fetching from True Dork Times
├── class_Definitions/
│   ├── playerClass.py          # Player model
│   ├── tribeClass.py           # Tribe model
│   └── allianceClass.py        # Alliance model
└── templates/                  # Flask HTML templates
```

### API Endpoints

- `GET /` — Homepage
- `POST /process_season` — Process a season number and initialize players
- `GET /tribe_sorter/<season_number>` — Tribe sorting interface
- `GET /simulate/<season_number>` — Simulation interface
- `GET /api/simulate/<season_number>` — Run full simulation (JSON)
- `GET /api/simulate_round/<season_number>` — Run single round (JSON)

## Machine Learning Models

The project includes educational implementations from scratch:

### Perceptron

- Single-layer neural network for binary classification
- Learns via weight updates from prediction errors
- Features: challenge skill, social skill, intelligence, morale
- Used to predict vote-out risk

### Multi-Layer Perceptron (MLP)

- Deep network with hidden layers for non-linear patterns
- Handles complex interactions between player attributes
- High-level `SurvivorPredictor` interface for game outcome prediction

## Usage

### Run the Web App

```bash
python app.py
```

Navigate to `http://localhost:5000`.

### Run Simulations Programmatically

```python
from game_engine import run_simulation

results = run_simulation(season_number=32, num_tribes=2, max_rounds=20)
```

## Skills & Technologies

- **Python** — Core logic, data processing, ML
- **Flask** — Web framework, templates, API
- **Pandas** — Data handling from Excel
- **NumPy** — ML model computations
- **Machine Learning** — Perceptron, MLP from scratch

## Repository

[View on GitHub](https://github.com/kianils)
