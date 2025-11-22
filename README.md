
# Student Performance Predictor

A beginner-friendly ML project for Fundamentals of AI & ML.

## Overview
Predict whether a student will pass or fail based on simple features (study hours, attendance, previous grade, etc.). Demonstrates data generation, preprocessing, training, evaluation, and a small CLI.

## Quick start
1. Create and activate a virtual environment:
   - Windows: `python -m venv .venv` & `.\.venv\Scripts\activate`
   - macOS/Linux/Codespaces: `python3 -m venv .venv` & `source .venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Train model: `python -m src.cli train`
4. Evaluate: `python -m src.cli evaluate`
5. Predict: `python -m src.cli predict --hours 5 --attendance 80 --prev_grade 70 --sleep 7 --extra-help 0`
