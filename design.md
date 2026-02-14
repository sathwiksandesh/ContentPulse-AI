# ContentPulse AI - Design Document (Gemini API Version)

## 1. System Architecture Overview

ContentPulse AI is a lightweight AI-powered content assistant built using **Streamlit** and **Google Gemini API**.  
The system helps creators and small businesses generate, repurpose, plan, and optimize social media content quickly.

This solution is designed to be:
- Easy to run locally or deploy online
- User-friendly for non-technical users
- Fast and scalable using cloud AI inference

---

## 2. High-Level Architecture

### 2.1 Architecture Diagram

┌──────────────────────────────────────────────────────┐
│ User Interface │
│ (Streamlit Web App) │
│ │
│ Features: │
│ - Generate Social Media Post │
│ - Repurpose Content │
│ - Weekly Content Planner │
│ - Caption Optimizer │
└──────────────────────────┬───────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────┐
│ Application Layer │
│ (Python Business Logic) │
│ │
│ - Prompt Engineering Module │
│ - Request Validation │
│ - API Request Builder │
│ - Response Parser │
│ - History Saving Module (JSON) │
└──────────────────────────┬───────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────┐
│ AI Model Layer │
│ (Google Gemini API) │
│ │
│ - Text Generation │
│ - Summarization │
│ - Content Optimization │
│ - Planning & Strategy Suggestions │
└──────────────────────────┬───────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────┐
│ Storage Layer │
│ Local JSON File Storage │
│ history/generated_history.json │
└──────────────────────────────────────────────────────┘   



---

## 3. Design Principles

### 3.1 Simplicity First
The solution is designed to be minimal, easy to execute, and hackathon-friendly.  
No heavy backend or complex database is required.

### 3.2 Prompt-Based Modular AI
Each feature uses a different structured prompt to Gemini to generate specific outputs.

### 3.3 User-Friendly Workflow
Users only need to enter basic inputs like topic, platform, and tone, and the AI generates complete content.

### 3.4 Extendable Architecture
The system can be extended later with:
- Database support
- Multi-user login
- Scheduling integrations
- Analytics dashboards
- AWS Bedrock integration

---

## 4. Technology Stack

| Component | Technology |
|----------|------------|
| Frontend UI | Streamlit |
| Backend Logic | Python |
| AI Model | Google Gemini API |
| Environment Variable Handling | python-dotenv |
| Data Storage | Local JSON file |
| API Communication | google-generativeai SDK |

---

## 5. Modules and Components

### 5.1 User Interface Module (Streamlit)

**Purpose:**  
Provides an interactive UI for content creation and optimization.

**UI Components:**
- Sidebar feature selection menu
- Input forms (topic, tone, platform, etc.)
- Output display box
- Spinner loading animation
- Success / error messages

---

### 5.2 Prompt Engineering Module

**Purpose:**  
Creates structured prompts to get high-quality output from Gemini.

Each feature has its own prompt template:

#### Generate Social Media Post Prompt
- Hook line
- Main content
- CTA
- Hashtags

#### Repurpose Content Prompt
- Instagram caption
- LinkedIn post
- Twitter thread
- Shorts script
- Blog summary

#### Weekly Planner Prompt
- 7-day content plan
- Post type suggestions
- Caption idea + CTA + hashtags

#### Caption Optimizer Prompt
- Improved caption
- CTA suggestions
- Hashtags
- Engagement tips

---

### 5.3 Gemini Integration Module

**Purpose:**  
Sends user prompts to Gemini API and returns AI output.

**Key Tasks:**
- Configure API key
- Select Gemini model dynamically
- Call `generate_content()`
- Handle API errors (quota, invalid model, network)

**Implementation Used:**
- Auto-detect the first available model supporting `generateContent`

---

### 5.4 Content History Module

**Purpose:**  
Stores user generated outputs for future reference.

**Storage Type:** JSON file

**File Location:**
history/generated_history.json 


**Data Stored:**
- timestamp
- feature name
- input parameters
- AI output response

This is useful for tracking demo results and showing history during hackathon presentation.

---

## 6. Application Workflow

### 6.1 Social Media Post Generation Workflow

User enters Topic + Platform + Audience + Tone
│
▼
Prompt is built in structured format
│
▼
Gemini API generates post content
│
▼
Output displayed in Streamlit
│
▼
Saved to JSON history


---

### 6.2 Content Repurposing Workflow

User pastes long content
│
▼
Prompt asks AI to convert into multiple formats
│
▼
Gemini generates multi-platform content
│
▼
Output shown + stored in history


---

### 6.3 Weekly Planner Workflow
User enters niche + goal + platform
│
▼
Prompt asks AI to generate 7-day plan
│
▼
Gemini generates calendar plan
│
▼
Output shown + stored in history

---

### 6.4 Caption Optimization Workflow

User pastes caption + selects tone
│
▼
Prompt asks AI to improve caption + hashtags
│
▼
Gemini returns optimized caption and tips
│
▼
Output shown + stored in history

---

## 7. Data Design

### 7.1 History JSON Format

Example record stored in `generated_history.json`:

```json
{
  "timestamp": "2026-02-14 10:30:00",
  "feature": "Generate Post",
  "input": {
    "topic": "AI in Education",
    "platform": "LinkedIn",
    "audience": "Students",
    "tone": "Professional"
  },
  "output": "Generated post content..."
}
8. Error Handling Strategy
8.1 Gemini API Errors

Handled cases:

Invalid API key

Model not available

Quota exceeded

Network/API connection issues

The UI displays errors as messages instead of crashing the app.

8.2 User Input Validation

If required fields are missing:

Topic not entered

Caption not entered

Content not pasted

The app shows warning messages.

9. Security Considerations
9.1 API Key Protection

API key is stored in .env file

.env file is excluded from GitHub uploads

Key is loaded using python-dotenv

9.2 User Data Handling

No user authentication is implemented in this prototype

User-generated content is stored only locally

No personal data is sent except prompt text

10. Scalability Considerations:-

10.1 Current Prototype Scalability

Streamlit supports multiple users but is best for prototype/demo usage.

10.2 Future Scaling Improvements

Future versions can integrate:

FastAPI backend

Database (MongoDB/PostgreSQL)

User authentication (OAuth/Google login)

Cloud deployment on AWS/GCP

Job queues for bulk content generation

11. Future Roadmap
Phase 2 Enhancements

Multi-language support (Hindi, Telugu, Tamil)

Brand voice personalization (user-defined style)

Export feature (PDF/Word/CSV)

Copy-to-clipboard & download outputs

Phase 3 Enhancements

Social media scheduling integration

Trend analysis (hashtags + viral topics)

Engagement prediction scoring

Auto thumbnail & poster generator (AI image support)

Phase 4 (Production Level)

Full AWS Bedrock integration for enterprise-level deployment

Real-time analytics dashboard

Multi-user team collaboration workspace

12. Summary

ContentPulse AI is a practical AI-based content assistant that helps users generate and optimize digital content quickly.
By using Google Gemini API and Streamlit, the system delivers a fast and user-friendly prototype suitable for hackathon evaluation and future real-world deployment.

The solution demonstrates:

Creativity and usefulness in content workflows

Practical AI integration

Simple but scalable architecture

Strong real-world relevance in India