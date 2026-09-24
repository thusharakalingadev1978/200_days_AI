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

### Phase 3 – Deep Learning
- Neural Networks
- Forward Propagation
- Backpropagation
- CNN
- RNN
- LSTM
- Transformers
- PyTorch

### Phase 4 – NLP
- Text Processing
- Tokenization
- Embeddings
- Attention Mechanism
- Transformer Architecture
- Text Classification
- Named Entity Recognition

### Phase 5 – LLM Engineering
- LLM Fundamentals
- Prompt Engineering
- Embeddings
- Vector Databases
- RAG
- Function Calling
- Tool Use
- Agents
- Fine-tuning
- Evaluation

### Phase 6 – Generative AI
- Generative AI Fundamentals
- LLM Applications
- Multimodal AI
- AI Agents
- Image Generation
- Document Intelligence
- Voice AI

### Phase 7 – AI Backend Engineering
- FastAPI
- Authentication
- Authorization
- JWT
- Microservices
- API Gateway
- Async Communication
- Event-Driven Architecture

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
