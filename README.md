# 🔥 ContentPulse AI

ContentPulse AI is an AI-powered content creation and optimization platform built using **Streamlit** and the **Google Gemini API**.  
It helps users generate engaging social media posts, repurpose long content into multiple formats, create weekly content plans, and optimize captions for better engagement.

This project is developed as a **Hackathon Prototype** under the track:

✅ **AI for Media, Content & Digital Experiences**

---

## 🚀 Key Features

### ✅ 1. Social Media Post Generator
Generate platform-specific posts for:
- Instagram
- LinkedIn
- Twitter/X
- YouTube Shorts

Includes:
- Strong hook line
- Short engaging content
- CTA (Call-to-action)
- Trending hashtags

---

### ✅ 2. Content Repurposing Tool
Convert one long content into:
- Instagram caption
- LinkedIn professional post
- Twitter/X thread (5 tweets)
- YouTube Shorts script
- Blog summary

---

### ✅ 3. Weekly Content Planner
Generates a 7-day content calendar with:
- Topic ideas
- Post format suggestions (Reels/Posts/Carousels)
- Caption idea
- CTA and hashtags

---

### ✅ 4. Caption Optimizer
Improves captions by providing:
- Enhanced caption
- Strong CTA
- Suggested hashtags
- Engagement improvement tips

---

### ✅ 5. History Saving (Local Storage)
All generated outputs are saved in:
history/generated_history.json

This helps track previous outputs during demo and evaluation.

---

## 🎯 Problem Statement

Content creators, students, and small businesses struggle with:
- Writing daily social media content
- Generating new post ideas
- Repurposing the same content across platforms
- Optimizing captions and hashtags for engagement

ContentPulse AI solves this problem using AI automation.

---

## 💡 Solution Overview

ContentPulse AI takes simple inputs like:
- Topic
- Platform
- Audience
- Tone

Then it uses **Google Gemini API** to generate complete, high-quality digital content instantly.

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Google Gemini API |
| Storage | JSON File Storage |
| Environment Config | python-dotenv |

---

## 🤖 AI Model Used

This project uses **Google Gemini API** for generating and optimizing content.

Gemini model is auto-selected based on availability in the user account.

---

## 📂 Project Structure


ContentPulse-AI/
│── app.py
│── requirements.txt
│── README.md
│── design.md
│── requirements.md
│── .env (not uploaded to GitHub)
│
└── history/
└── generated_history.json  

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/sathwiksandesh/ContentPulse-AI.git
cd ContentPulse-AI

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create .env File

Create a file named .env inside the project folder:
GEMINI_API_KEY=your_api_key_here

4️⃣ Run the Application
python -m streamlit run app.py

The app will open in your browser at:

http://localhost:8501
