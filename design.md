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
### 2.1 Architecture Diagram

```text
+-------------------------------------------------------------+
|                    User Interface Layer                      |
|                   (Streamlit Web Application)                |
|                                                             |
|  Features:                                                  |
|   - Generate Social Media Post                               |
|   - Repurpose Content                                        |
|   - Weekly Content Planner                                   |
|   - Caption Optimizer                                        |
+-------------------------------+-----------------------------+
                                |
                                v
+-------------------------------------------------------------+
|                    Application Logic Layer                   |
|                      (Python Backend Code)                   |
|                                                             |
|  Modules:                                                   |
|   - Prompt Engineering Module                                |
|   - Input Validation Module                                  |
|   - Gemini API Request Handler                               |
|   - Response Formatter / Parser                              |
|   - History Saving Module (JSON)                             |
+-------------------------------+-----------------------------+
                                |
                                v
+-------------------------------------------------------------+
|                         AI Model Layer                       |
|                     (Google Gemini API)                      |
|                                                             |
|  Capabilities:                                              |
|   - Text Generation                                          |
|   - Summarization                                            |
|   - Content Optimization                                     |
|   - Strategy & Planning Suggestions                          |
+-------------------------------+-----------------------------+
                                |
                                v
+-------------------------------------------------------------+
|                         Storage Layer                        |
|                    Local JSON File Storage                   |
|                                                             |
|  File: history/generated_history.json                        |
+-------------------------------------------------------------+
```

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
```
## 8. Error Handling Strategy

### 8.1 Gemini API Errors

The application handles Gemini API failures gracefully without crashing the UI.  
The following cases are managed:

- Invalid API Key  
- Model not available / unsupported model  
- Quota exceeded (rate limits or daily usage limits)  
- Network/API connection issues (timeouts, internet failure)

If any of the above errors occur, the system displays a user-friendly error message in the Streamlit interface.

---

### 8.2 User Input Validation

Before sending prompts to Gemini API, the system validates user inputs.  
If required fields are missing, warnings are displayed:

- Topic not entered  
- Caption not entered  
- Content not pasted  
- Niche not entered for weekly planner  

This ensures no empty or invalid prompts are sent to the AI model.

---

## 9. Security Considerations

### 9.1 API Key Protection

To protect sensitive credentials, the Gemini API key is stored securely:

- API key is stored in a `.env` file  
- `.env` file is excluded from GitHub using `.gitignore`  
- Key is loaded using the `python-dotenv` library  

This prevents accidental leakage of API keys in public repositories.

---

### 9.2 User Data Handling

- No user authentication is implemented in this prototype version  
- User-generated content is stored only locally in JSON history files  
- No personal data is shared except the prompt text sent to Gemini API  

---

## 10. Scalability Considerations

### 10.1 Current Prototype Scalability

Streamlit supports multiple users but is mainly intended for prototype and demo deployment.

---

### 10.2 Future Scaling Improvements

Future versions can be scaled by integrating:

- FastAPI backend services  
- Database storage (MongoDB / PostgreSQL)  
- User authentication (OAuth / Google Login)  
- Cloud deployment on AWS or GCP  
- Job queues for bulk content generation and scheduling  

---

## 11. Future Roadmap

### Phase 2 Enhancements

- Multi-language support (Hindi, Telugu, Tamil)  
- Brand voice personalization (user-defined writing style)  
- Export generated content to PDF/Word/CSV  
- Copy-to-clipboard and download outputs  

---

### Phase 3 Enhancements

- Social media scheduling integration  
- Trend analysis using hashtags and viral topics  
- Engagement prediction scoring system  
- AI thumbnail and poster generation support  

---

### Phase 4 (Production-Level Deployment)

- Enterprise deployment using Amazon Bedrock or Vertex AI  
- Real-time analytics dashboard  
- Multi-user team collaboration workspace  

---

## 12. Summary

ContentPulse AI is a practical AI-based content assistant that helps users generate and optimize digital content quickly.  
By using Google Gemini API and Streamlit, the system delivers a fast and user-friendly prototype suitable for hackathon evaluation and future real-world deployment.

The solution demonstrates:

- Creativity and usability in content workflows  
- Effective AI integration for content creation  
- Simple but scalable architecture  
- Strong relevance and real-world impact for users in India  

