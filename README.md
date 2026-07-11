# 🤖 AI Resume Matcher (ATS)

An AI-powered Applicant Tracking System (ATS) that analyzes resumes against job descriptions using Natural Language Processing (NLP), semantic embeddings, and skill matching.

The system extracts information from resumes, compares them with job requirements, calculates a match score, and identifies missing skills.

---

## 🚀 Features

* 📄 Upload Resume PDF
* 📝 Add Job Description
* 🔍 Extract resume text automatically
* 🧠 Semantic similarity using Sentence Transformers
* 🛠️ Skill matching using NLP techniques
* ❌ Detect missing skills
* ✅ Show matched skills
* 📊 Calculate ATS compatibility score
* 📈 Resume structure analysis
* 🎨 Interactive Streamlit interface

---

## 🧠 How It Works

### 1. Resume Processing

The uploaded PDF is converted into text using PDF extraction techniques.

```
PDF Resume
     |
     ↓
Text Extraction
```

---

### 2. Skill Extraction

The system detects technical skills from:

* Resume
* Job Description

Example:

Resume:

```
Python
Machine Learning
SQL
TensorFlow
```

Job Description:

```
Python
Deep Learning
SQL
Docker
```

Result:

Matched:

```
Python
SQL
```

Missing:

```
Deep Learning
Docker
```

---

### 3. Semantic Matching

The project uses Sentence Transformers to understand the meaning of text.

Instead of only matching keywords:

Example:

Resume:

```
Built machine learning models for prediction tasks
```

Job:

```
Experience developing ML predictive systems
```

The model understands that they have similar meanings.

---

### 4. ATS Score Calculation

Final score:

```
Final Score =
( Semantic Similarity × 70% )
+
( Skill Match × 30% )
```

---

## 🛠️ Technologies

### Programming

* Python

### NLP

* Sentence Transformers
* spaCy
* Regex
* Embeddings

### Machine Learning

* Scikit-learn

### Deployment/UI

* Streamlit

### Data Processing

* Pandas

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/yourusername/ATS_Resume_Matcher.git
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

Add screenshots here:

```
![ATS Interface](assets/screenshot.png)
```

---

## 🔮 Future Improvements

* Advanced skill ontology
* Skill synonym matching
* Resume ranking system
* LLM-based improvement suggestions
* Job recommendation system
* Explainable ATS feedback

---

## 👨‍💻 Author

Youssef Ayman

AI Engineer | Data Scientist | Machine Learning Engineer

---

## ⭐ Project Goal

Build a practical NLP application that demonstrates how AI can assist recruiters and candidates in improving resume-job compatibility.
