# Fynd AI Intern – Take Home Assignment

This repository contains my submission for the **Fynd AI Engineering Intern take-home assignment**, covering prompt engineering with LLMs and a deployed AI-powered feedback system.

---

## 📌 Project Overview

The assignment consists of two main tasks:

### **Task 1 – Rating Prediction via Prompting**
- Yelp reviews are classified into **1–5 star ratings** using LLM prompting
- Multiple prompt designs are tested and compared
- Evaluation includes accuracy and JSON validity

### **Task 2 – AI Feedback System (Web-Based)**
- A user-facing dashboard to submit ratings and reviews
- An admin dashboard to monitor feedback with AI-generated insights
- Both dashboards are fully deployed and publicly accessible

---

## 📂 Repository Structure



fynd-ai-intern-assignment/

│
├── task1_prompting/

│   ├── data/

│   │   └── yelp.csv

│   ├── yelp_prompt_experiments.ipynb

│   ├── prompt_comparison_results.csv

│   └── prompts.md
│
├── task2_app/

│   ├── app.py              # User Dashboard

│   ├── admin.py            # Admin Dashboard

│   ├── utils/

│   │   └── llm.py

│   ├── data/

│   │   └── feedback.csv

│   └── requirements.txt

│
├── report/

│   └── Fynd_AI_Intern_Assignment_Report.pdf

│
└── README.md



## 🧠 Task 1 – Prompt Engineering

- Dataset: Yelp Reviews (sampled ~200 rows)
- Implemented **3 different prompt strategies**
- Each prompt evaluated on:
  - Prediction accuracy
  - JSON validity
  - Output consistency
- Results and comparison are included in:
  - `yelp_prompt_experiments.ipynb`
  - `prompt_comparison_results.csv`

---

## 🌐 Task 2 – Deployed Dashboards

### **User Feedback Dashboard**
Users can:
- Select a star rating
- Write a short review
- Receive an AI-generated response

🔗 **URL:**  
https://fynd-ai-intern-assignment-rox9waszj7wtw94redpy8y.streamlit.app/

---

### **Admin Dashboard**
Admins can view:
- All submitted feedback
- AI-generated summaries
- AI-recommended actions
- Basic analytics (total feedback, average rating, 5-star count)

🔗 **URL:**  
https://fynd-ai-intern-assignment-ksou8pge2qznujcromlkxp.streamlit.app/

---

## 🤖 LLM Usage

LLMs are used for:
- Rating prediction via prompting (Task 1)
- User-facing responses
- Review summarization
- Recommended next actions

Free-tier LLMs were used for experimentation and deployment.

---

## 📄 Report

A short report summarizing:
- Prompt iterations
- Design decisions
- Evaluation results
- System behavior


