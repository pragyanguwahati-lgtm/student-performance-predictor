# Student Performance Predictor


**A beginner-friendly ML project for Fundamentals of AI & ML**


## Overview
This project predicts whether a student will pass or fail based on simple features (study hours, attendance, previous grade, etc.). It demonstrates the end-to-end ML pipeline: dataset, preprocessing, modeling, evaluation, and a small CLI for inference.


## Features
- Synthetic dataset generator
- Data preprocessing and feature engineering
- Model training (Logistic Regression & Decision Tree options)
- Model evaluation and basic plots
- CLI for training/evaluation/prediction


## Technologies
- Python 3.10+
- scikit-learn, pandas, numpy, matplotlib


## Setup
1. Create and activate a virtual environment:
- Windows: `python -m venv .venv` & `.\.venv\Scripts\activate`
- macOS/Linux: `python3 -m venv .venv` & `source .venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the training: `python -m src.cli train`


## Usage
- Train model: `python -m src.cli train`
- Evaluate model: `python -m src.cli evaluate`
- Predict: `python -m src.cli predict --hours 5 --attendance 85 --prev_grade 60`


## Tests
Run `pytest` to execute the unit tests in `tests/`.


## Files
See the repository structure in the project root.