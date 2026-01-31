# FAQ Chatbot using NLP and Streamlit

## 📌 Project Description
This project implements a simple **FAQ Chatbot** using **Natural Language Processing (NLP)** techniques.  
The chatbot answers user questions by matching them with the most relevant FAQ from a dataset using **TF-IDF vectorization** and **cosine similarity**.

A **Streamlit web interface** is used to allow users to interact easily with the chatbot.

---

## 🎯 Objectives
- Collect and use FAQ data from a CSV dataset
- Preprocess text using NLP techniques (tokenization, stopword removal)
- Match user questions with FAQs using cosine similarity
- Display the most relevant answer as a chatbot response
- Provide a simple and interactive user interface

---

## 🏗️ Project Architecture


---

## 📊 Dataset
- Source: **Kaggle (Mental Health FAQ Dataset)** https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot?resource=download
- Format: CSV file
- Columns used:
  - `ID`: Question ID
  - `Questions`: FAQ questions
  - `Answers`: Corresponding answers

The dataset is included in the project to ensure reproducibility.

---

## 🧠 Technologies Used
- **Python 3**
- **Pandas** – CSV data handling
- **NLTK** – Text preprocessing
- **Scikit-learn** – TF-IDF & cosine similarity
- **Streamlit** – Web interface
- **Git & GitHub** – Version control

---

## ⚙️ Installation Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/faq_chatbot.git
cd faq_chatbot
