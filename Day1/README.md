# 🚀 1. Today's Goal

මේ concepts theory එකෙන් විතරක් නෙවෙයි, actual application එකක් හරහා understand වෙන්න ඕන.

## 📚 You should understand:

- 🤖 What is AI?
- 🧠 What is Machine Learning?
- 🎓 Supervised Learning
- 📈 Regression
- 🔢 Features
- 🎯 Target
- 📊 Dataset
- 🏋️ Training Data
- 🧪 Testing Data
- 🧠 Model
- 🔮 Prediction
- 🔄 Training vs Prediction
- ⚙️ Basic ML Workflow

Practical side:
අපි අද House Price Prediction System එකේ foundation එක build කරනවා.

```text
House Information
       ↓
   ML Model
       ↓
Predicted House Price
```
---

## 🎯 Learning Goal

My main goal is to become a:

අපේ application එකට user කෙනෙක් මේ information දෙන්න පුළුවන්:
```text
Area       = 1500 sq.ft
Bedrooms   = 3
Bathrooms  = 2
Age        = 8 years
Location   = Kandy
```
ML model එක:
```text
Input
  ↓
Machine Learning Model
  ↓
Predicted Price
```
Output:
```text
Predicted Price = Rs. 28,500,000

```
Important: මේ price එක example එකක්. අපේ actual trained model එක dataset එක අනුව prediction එක calculate කරනවා.

---
The learning approach is **practical and project-based**, with real-world
applications rather than only theoretical learning.

---

## 📚 3. Today's Architecture

අද අපි මේ architecture එකේ first part එක build කරනවා.

```text
  HOUSE PRICE SYSTEM
                        │
                        ▼
                  House Dataset
                        │
                        ▼
                 Data Understanding
                        │
                        ▼
                    Features
                        │
                        ▼
                     Target
                        │
                        ▼
               Train/Test Dataset
                        │
                        ▼
                ML Model Training
```
Day 1 later stages වල:
```text
ML Model
   ↓
Saved Model
   ↓
FastAPI
   ↓
POST /predict
   ↓
Prediction

```

### 4. What Is Artificial Intelligence?
Artificial Intelligence (AI) කියන්නේ computer system එකකට human-like intelligent tasks perform කරන්න හැකියාව ලබාදීම.
```text
Examples:

Image recognition
Speech recognition
Recommendation systems
Chatbots
Autonomous systems
Fraud detection
Language translation
```
```text
AI
│
├── Machine Learning
│
├── Deep Learning
│
├── NLP
│
├── Computer Vision
│
└── Generative AI
```
### 🧠 5. What Is Machine Learning?e Learning

Traditional programming එකේ:
```text
Rules + Data
     ↓
 Program
     ↓
 Output
```
Example:
```text
if area > 2000:
    price = 30000000
```
මෙතන rules developer තමයි manually ලියන්නේ.
Machine Learning වල:
```text
Data + Answers
      ↓
  ML Algorithm
      ↓
     Model
```
Model එක data වල patterns learn කරනවා.
House example:
```text
Area   Bedrooms   Price
1000      2       15M
1500      3       22M
2000      4       31M
2500      4       38M
```
Model එක මේ data වල relationship එක learn කරනවා.

### 🔥 6. Our First Important Concept — Supervised Learning

අපේ House Price application එක Supervised Learning problem එකක්.
ඇයි?
අපි model එකට historical examples දෙනවා.
```text
Input                    Answer
──────────────────────────────────
1000 sq.ft, 2 rooms  →   15M
1500 sq.ft, 3 rooms  →   22M
2000 sq.ft, 4 rooms  →   31M
```
Model එකට:

"මේ inputs වලට මේ answers තියෙනවා. මේ relationship එක learn කරන්න."

කියනවා.

Supervised Learning:
```text
Input Data
    +
Correct Output
    ↓
Training
    ↓
Model
```

### 📈 7. Regression
House price එක:
```text
Rs. 15,000,000
Rs. 22,500,000
Rs. 31,750,000
Rs. 45,200,000
```
වගේ continuous numerical value එකක්.

ඒ නිසා මේක:

Regression Problem

Regression examples

- House price
- Car price
- Salary prediction
- Temperature prediction
- Sales prediction
- Demand prediction

### 🧩 8. Features
Features කියන්නේ prediction එකට model එකට දෙන input variables.
අපේ application එකේ:
```text
Area
Bedrooms
Bathrooms
Age
Location
```
මේවා features.

Example:
```text
Area = 1500
Bedrooms = 3
Bathrooms = 2
Age = 8
```

### 🎯 9. Target
Target කියන්නේ අපි predict කරන්න ඕන output එක.

අපේ application එකේ:
```text
Target = House Price
```
So:
```text
Features
──────────────
Area
Bedrooms
Bathrooms
Age
Location

        ↓

     MODEL

        ↓

Target
──────────────
House Price
```
මේ distinction එක ML වල extremely important.

### 📊 10. Dataset
Dataset එක කියන්නේ training examples collection එක.
Example:
| Area | Bedrooms | Bathrooms | Age | Price |
| ---: | -------: | --------: | --: | ----: |
| 1000 |        2 |         1 |  15 |   15M |
| 1200 |        2 |         2 |  10 |   18M |
| 1500 |        3 |         2 |   8 |   22M |
| 1800 |        3 |         2 |   5 |   27M |
| 2200 |        4 |         3 |   4 |   34M |
මෙතන:

Features = Area, Bedrooms, Bathrooms, Age
Target   = Price


### Phase 8 – MLOps
- Docker
- CI/CD
- Model Deployment
- Model Versioning
- Experiment Tracking
- Monitoring
- Cloud Deployment

### Phase 9 – AI Architecture
- AI System Design
- Distributed Systems
- Scalable AI Systems
- LLM Architecture
- RAG Architecture
- Agent Architecture
- AI Infrastructure
- Production AI Systems

---

# 📅 Daily Learning Structure

Each learning day follows a practical structure:

1. 📖 Theory
2. 🧠 Concept Explanation
3. 💻 Hands-on Coding
4. 🏗️ Mini Project
5. 🧪 Testing
6. 🔍 Debugging
7. 🚀 Real-World Application
8. 📝 Notes
9. 🎯 Interview Questions
10. ✅ Daily Tasks

---

# 🗂️ Project Structure

```text
AI-Learning/
│
├── Day-01/
│   ├── README.md
│   ├── src/
│   ├── tests/
│   ├── data/
│   ├── requirements.txt
│   └── .gitignore
│
├── Day-02/
│   ├── README.md
│   ├── src/
│   ├── tests/
│   └── requirements.txt
│
├── Day-03/
│   └── ...
│
├── Machine-Learning/
│
├── Deep-Learning/
│
├── NLP/
│
├── LLM/
│
├── Generative-AI/
│
├── MLOps/
│
└── AI-Architecture/
