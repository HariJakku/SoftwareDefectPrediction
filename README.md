<div align="center">

# 🔬 Software Defect Prediction Using Stacking & LightGBM

[![Published](https://img.shields.io/badge/Published-IJESAT%20Vol%2026%20Issue%2003%20%7C%20March%202026-blue?style=for-the-badge)](https://www.ijesat.com/)
[![Accuracy](https://img.shields.io/badge/Accuracy-93.5%25-brightgreen?style=for-the-badge)](.)
[![Dataset](https://img.shields.io/badge/Dataset-NASA%20MDP-orange?style=for-the-badge)](.)
[![Framework](https://img.shields.io/badge/Deployed%20With-Flask-black?style=for-the-badge&logo=flask)](.)
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python)](.)

> **Peer-Reviewed Research | IJESAT Vol 26, Issue 03 (March 2026)**  
> *Accepted: 18-03-2026 | Published: 24-03-2026*

**Author:** Jakku Kumarswami  
Department of Computer Science and Engineering  
Seshadri Rao Gudlavalleru Engineering College, Andhra Pradesh – 521356, India  
📧 harijakku2005@gmail.com

</div>

---

## 📌 Overview

This project presents an **Intelligent ensemble-based software defect prediction (SDP) system** that combines the power of **Stacking Ensemble Learning** with **LightGBM** as a meta-learner. Deployed as a secure **Flask web application**, it enables real-time defect analysis on NASA MDP benchmark datasets.

The system achieves a remarkable **93.5% accuracy** on the PC4 dataset — outperforming traditional voting-based ensembles and individual classifiers by significant margins.

---

## 🏆 Key Results

| Algorithm | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
|---|---|---|---|---|
| Naïve Bayes (NB) | 78.2 | 76.4 | 74.8 | 75.6 |
| Support Vector Machine (SVM) | 82.6 | 81.3 | 79.5 | 80.4 |
| Multi-Layer Perceptron (MLP) | 84.1 | 83.6 | 82.2 | 82.9 |
| Random Forest (RF) | 87.9 | 86.8 | 85.7 | 86.2 |
| Voting Ensemble | 89.6 | 88.9 | 87.4 | 88.1 |
| **🥇 Proposed Stacking (DT + RF + LightGBM)** | **93.5** | **92.8** | **91.6** | **92.2** |

### Accuracy by Dataset (Stacking Classifier)

| Dataset | Voting Ensemble | Stacking + LightGBM |
|---|---|---|
| CM1 | 86.5% | **92.4%** |
| JM1 | 66.0% | **83.6%** |
| MC2 | 73.5% | 73.5% |
| MW1 | 80.1% | **89.7%** |
| PC1 | 87.0% | **92.2%** |
| PC3 | 87.5% | **92.4%** |
| PC4 | 90.4% | **93.5%** |

---

## 🧠 System Architecture

```
┌──────────────────────────────────────────────────────┐
│                   DATA LAYER                         │
│         NASA MDP Repository (CM1, PC4, etc.)         │
└──────────────────┬───────────────────────────────────┘
                   │
┌──────────────────▼───────────────────────────────────┐
│              PREPROCESSING LAYER                     │
│   Missing Value Handling | Normalization | SMOTE     │
└──────────────────┬───────────────────────────────────┘
                   │
┌──────────────────▼───────────────────────────────────┐
│         FEATURE OPTIMIZATION (PSO + K-Means)         │
│   Dimensionality Reduction | Cluster-based Learning  │
└──────┬──────────┬──────────┬──────────┬──────────────┘
       │          │          │          │
┌──────▼──┐ ┌────▼────┐ ┌───▼───┐ ┌───▼────┐
│   MLP   │ │   SVM   │ │  NB   │ │   RF   │   ← Base Learners
└──────┬──┘ └────┬────┘ └───┬───┘ └───┬────┘
       └─────────┴──────────┴─────────┘
                           │
┌──────────────────────────▼───────────────────────────┐
│              STACKING LAYER (META-LEARNER)            │
│         Decision Tree + Random Forest → LightGBM     │
└──────────────────────────┬───────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────┐
│           FLASK WEB APPLICATION LAYER                │
│     User Auth | Real-time Input | Prediction UI      │
└──────────────────────────────────────────────────────┘
```

---

## ⚙️ Modules

| Module | Description |
|---|---|
| **Data Loading** | Imports NASA MDP datasets; initializes preprocessing pipeline |
| **Data Preprocessing** | Label encoding, deduplication, missing value correction |
| **K-Means Clustering** | Groups data into clusters for pattern-aware learning |
| **PSO Feature Optimization** | Particle Swarm Optimization for dimensionality reduction |
| **Base Model Training** | Independent training of MLP, SVM, NB, RF with tuned hyperparameters |
| **Adaptive Voting Ensemble** | Combines base model predictions via weighted voting |
| **Stacking Classifier** | DT + RF predictions fed into LightGBM meta-learner |
| **Evaluation** | Accuracy, Precision, Recall, F1-Score benchmarking |
| **User Authentication** | Secure signup/login system for the web interface |
| **Prediction Interface** | Real-time defect prediction via Flask UI |

---

## 🛠️ Tech Stack

```
Machine Learning  : scikit-learn, LightGBM
Optimization      : Particle Swarm Optimization (PSO)
Clustering        : K-Means (scikit-learn)
Web Framework     : Flask (Python)
Authentication    : Flask-Login / Session Management
Datasets          : NASA MDP (CM1, JM1, MC2, MW1, PC1, PC3, PC4)
Language          : Python 3.8+
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install scikit-learn lightgbm flask numpy pandas matplotlib
```

### Installation

```bash
# Clone the repository
git clone https://github.com/HariJakku/SoftwareDefectPrediction.git
cd SoftwareDefectPrediction

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py
```

### Usage

1. Navigate to `http://localhost:5000`
2. Register/Login with your credentials
3. Upload or select a NASA MDP dataset
4. Click **Predict** to get real-time defect analysis
5. View accuracy metrics and per-module defect risk

---

## 📐 Evaluation Metrics

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall} = \frac{TP}{TP + FN}$$

$$\text{F1-Score} = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

---

## 📄 Publication

> **"Improving Software Defect Prediction Using Stacking and LightGBM"**  
> *International Journal of Engineering Science and Advanced Technology (IJESAT)*  
> Vol 26, Issue 03 (March 2026) | Pages 666–675 | ISSN: 2250-3676  
> Received: 11-02-2026 | Accepted: 18-03-2026 | Published: 24-03-2026

---

## 🔭 Future Scope

- Integration of **deep learning** (CNN, LSTM) as additional base learners
- Cross-project defect prediction with **transfer learning**
- **Drift detection** hooks for automatic model retraining
- **Explainability** layer using SHAP / LIME for industrial adoption
- Extended evaluation on **open-source project datasets** (Eclipse, Apache)

---

## 📬 Contact

**Jakku Kumarswami**  
B.Tech – Computer Science and Engineering  
Seshadri Rao Gudlavalleru Engineering College  
Andhra Pradesh – 521356, India  
📧 harijakku2005@gmail.com

---

<div align="center">

⭐ **If this research helped you, consider giving it a star!** ⭐

*Published Research | Peer-Reviewed | IJESAT 2026*

</div>
