<<<<<<< HEAD
# 🎓 Student Performance Predictor  
*A Complete End-to-End Machine Learning Project (Fundamentals of AI & ML)*  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-brightgreen?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Data-Pandas-yellow?logo=pandas)
![VS Code](https://img.shields.io/badge/Editor-VSCode-blue?logo=visualstudiocode)
![GitHub](https://img.shields.io/badge/Version%20Control-GitHub-black?logo=github)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 🧑‍🎓 Student Details  
**Name:** Pragyanjyoti Dutta  
**Reg No.:** 25BCY10065  
**Course:** Fundamentals of AI and ML  

---

## 📌 Overview  
The **Student Performance Predictor** is a complete machine learning project designed to classify whether a student will *Pass* or *Fail* based on behavioral and academic features.  

This project demonstrates the **full machine learning development lifecycle**, including:  
- Synthetic dataset generation  
- Data preprocessing (scaling + stratified split)  
- Model training with Logistic Regression & Decision Tree  
- Model evaluation using accuracy, classification report, and confusion matrix  
- CLI-based prediction  
- Modular architecture following best practices  
- Automated testing using pytest  

It is built as an academic submission for the **Fundamentals of AI and ML** course, following clean coding and ML standards.

---

## 🧠 Key Features  

### ✔️ Complete ML Pipeline  
- Synthetic dataset generation  
- StandardScaler preprocessing  
- Stratified train-test split  
- Logistic Regression & Decision Tree models  
- Automated evaluation with classification metrics  

### ✔️ Command-Line Interface  
Easily train, evaluate, and predict through simple shell commands.

### ✔️ Robust Project Architecture  
- Modular Python files  
- Logging integrated  
- Organized data and report directories  

### ✔️ Automated Testing  
Includes pytest-based tests to ensure pipeline correctness.

---

## 🏗 Project Structure  

```
student-performance-predictor/
│
├── data/
│   └── students.csv                
│
├── report/
│   ├── eval.txt                    
│   └── confusion_matrix.png        
│
├── src/
│   ├── __init__.py
│   ├── cli.py                      
│   ├── data_generator.py           
│   ├── data_loader.py              
│   ├── preprocess.py               
│   ├── model.py                    
│   ├── evaluate.py                 
│   └── utils.py                    
│
├── tests/
│   └── test_pipeline.py            
│
├── requirements.txt
├── statement.md
└── README.md
```

---

## 📥 Installation & Setup  

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd student-performance-predictor
```

### 2. Create & activate a virtual environment

#### Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

#### macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage (CLI Commands)

### 1️⃣ Train the model
```bash
python -m src.cli train
```

---

### 2️⃣ Evaluate the saved model
```bash
python -m src.cli evaluate
```

---

### 3️⃣ Predict pass/fail for a new student
```bash
python -m src.cli predict     --hours 5     --attendance 80     --prev_grade 70     --sleep 7     --extra-help 0
```

**Expected Output:**
```
Prediction: Pass (prob: 0.82)
```

---

## 🧪 Running Tests  

Run automated tests:

```bash
pytest -q
```

Expected:
```
1 passed in 0.XXs
```

---

## 🧩 Technologies Used  
- Python 3.9+  
- scikit-learn  
- Pandas & NumPy  
- Matplotlib  
- Joblib  
- pytest  
- VS Code / GitHub Codespaces  

---

## 🎯 Project Objectives  
- Implement ML concepts from the course  
- Build a reproducible classification pipeline  
- Develop modular and maintainable software  
- Learn evaluation techniques  
- Practice GitHub version control  
- Build CLI tools for ML workflows  

---

## 🌱 Future Enhancements  
- Add advanced ML models  
- Hyperparameter tuning  
- Web app interface  
- Dashboard-style visualizations  
- Real dataset upload  
- CI/CD pipeline  

---

## 📚 References  
- scikit-learn Documentation — https://scikit-learn.org  
- Pandas — https://pandas.pydata.org  
- Matplotlib — https://matplotlib.org  
- Python Argparse — https://docs.python.org/3/library/argparse.html  
- Elements of Statistical Learning — Hastie, Tibshirani, Friedman  
=======

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
>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
