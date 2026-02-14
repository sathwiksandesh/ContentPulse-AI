import streamlit as st
import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# ------------------ STREAMLIT CONFIG ------------------ #
st.set_page_config(page_title="ContentPulse AI", page_icon="🔥", layout="wide")

# ------------------ LOAD ENV ------------------ #
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY not found. Please check your .env file.")
    st.stop()

# ------------------ CONFIGURE GEMINI ------------------ #
genai.configure(api_key=GEMINI_API_KEY)

# ------------------ AUTO SELECT MODEL ------------------ #
selected_model = None

try:
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            selected_model = m.name
            break
except Exception as e:
    st.error(f"❌ Error while listing Gemini models: {str(e)}")
    st.stop()

if not selected_model:
    st.error("❌ No Gemini model available that supports generateContent in your account.")
    st.stop()

# Load Gemini model dynamically
model = genai.GenerativeModel(selected_model)

# Show model in sidebar
st.sidebar.success(f"✅ Using Model: {selected_model}")


# ------------------ GEMINI CALL FUNCTION ------------------ #
def call_gemini(prompt):
    try:
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text
        else:
            return "⚠ No output generated. Try again."

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"


# ------------------ SAVE HISTORY FUNCTION ------------------ #
def save_to_history(feature, user_input, output):
    if not os.path.exists("history"):
        os.makedirs("history")

    filename = "history/generated_history.json"

    data = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except:
                data = []

    data.append({
        "timestamp": str(datetime.now()),
        "feature": feature,
        "input": user_input,
        "output": output
    })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# ------------------ STREAMLIT UI ------------------ #
st.title("🔥 ContentPulse AI")
st.subheader("AI-powered Content Creation, Repurposing & Optimization")

menu = st.sidebar.radio("📌 Select Feature", [
    "Generate Social Media Post",
    "Repurpose Content",
    "Weekly Content Planner",
    "Optimize Caption"
])


# ------------------ FEATURE 1: Generate Social Media Post ------------------ #
if menu == "Generate Social Media Post":
    st.header("📢 Generate Social Media Post")

    topic = st.text_input("Enter Topic (Example: AI in Education)")
    platform = st.selectbox("Choose Platform", ["Instagram", "LinkedIn", "Twitter/X", "YouTube Shorts"])
    audience = st.text_input("Target Audience (Example: Students, Startups, Developers)")
    tone = st.selectbox("Choose Tone", ["Professional", "Funny", "Motivational", "Emotional", "Storytelling"])

    if st.button("✨ Generate Content"):
        if topic and audience:
            prompt = f"""
You are an expert social media content creator.

Generate a {platform} post on the topic: "{topic}"

Target Audience: {audience}
Tone: {tone}

Include:
1. A strong hook line
2. Main content (short and engaging)
3. Call to action
4. 10 trending hashtags
"""

            with st.spinner("Generating content..."):
                output = call_gemini(prompt)

            st.success("✅ Content Generated!")
            st.text_area("Generated Output", value=output, height=350)

            save_to_history(
                "Generate Post",
                {"topic": topic, "platform": platform, "audience": audience, "tone": tone},
                output
            )
        else:
            st.warning("⚠ Please enter topic and audience.")


# ------------------ FEATURE 2: Repurpose Content ------------------ #
elif menu == "Repurpose Content":
    st.header("🔄 Repurpose Content into Multiple Formats")

    text = st.text_area("Paste your content (blog, post, notes, etc.)", height=200)

    if st.button("🔁 Repurpose"):
        if text:
            prompt = f"""
You are a content repurposing AI assistant.

Convert the following content into:

1) Instagram caption (with hashtags)
2) LinkedIn professional post
3) Twitter/X thread (5 tweets)
4) YouTube Shorts script (30 seconds)
5) Blog summary (short)

Content:
{text}
"""

            with st.spinner("Repurposing content..."):
                output = call_gemini(prompt)

            st.success("✅ Repurposed Successfully!")
            st.text_area("Repurposed Output", value=output, height=450)

            save_to_history("Repurpose Content", {"text": text[:200]}, output)
        else:
            st.warning("⚠ Please paste some content.")


# ------------------ FEATURE 3: Weekly Content Planner ------------------ #
elif menu == "Weekly Content Planner":
    st.header("📅 Weekly Content Planner")

    niche = st.text_input("Enter Niche (Example: Fitness, AI, Food Business)")
    goal = st.selectbox("Content Goal", ["Increase Engagement", "Increase Followers", "Promote Product", "Brand Awareness"])
    platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter/X", "YouTube Shorts"])

    if st.button("📌 Generate Weekly Plan"):
        if niche:
            prompt = f"""
You are a social media strategist.

Create a 7-day content calendar for:
Niche: {niche}
Goal: {goal}
Platform: {platform}

For each day include:
- Post Topic
- Content type (Reel/Carousel/Post/Story)
- Caption idea
- Suggested CTA
- Suggested hashtags
"""

            with st.spinner("Generating weekly content plan..."):
                output = call_gemini(prompt)

            st.success("✅ Weekly Plan Generated!")
            st.text_area("Weekly Planner Output", value=output, height=450)

            save_to_history(
                "Weekly Planner",
                {"niche": niche, "goal": goal, "platform": platform},
                output
            )
        else:
            st.warning("⚠ Please enter your niche.")


# ------------------ FEATURE 4: Caption Optimizer ------------------ #
elif menu == "Optimize Caption":
    st.header("⚡ Caption Optimizer")

    caption = st.text_area("Paste your caption to optimize", height=200)
    platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter/X"])
    tone = st.selectbox("Desired Tone", ["Professional", "Funny", "Motivational", "Emotional", "Storytelling"])

    if st.button("🚀 Optimize"):
        if caption:
            prompt = f"""
You are a social media marketing expert.

Optimize this caption for {platform}.
Tone should be: {tone}

Caption:
{caption}

Return:
1. Improved Caption
2. Suggested CTA
3. Suggested Hashtags
4. 3 Tips to improve engagement
"""

            with st.spinner("Optimizing caption..."):
                output = call_gemini(prompt)

            st.success("✅ Caption Optimized!")
            st.text_area("Optimized Output", value=output, height=450)

            save_to_history(
                "Caption Optimizer",
                {"caption": caption[:200], "platform": platform, "tone": tone},
                output
            )
        else:
            st.warning("⚠ Please paste a caption.")