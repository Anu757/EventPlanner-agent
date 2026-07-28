import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# PDF function
def create_pdf(content):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    story = []
    for line in content.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 10))

    doc.build(story)
    buffer.seek(0)
    return buffer

# UI
st.title("🎉 AI Event Planner Agent (Groq Powered)")

st.subheader("Enter Event Details")

event_type = st.text_input("Event Type (Wedding, Birthday, Corporate)")
guests = st.number_input("Number of Guests", 1, 1000)
budget = st.text_input("Budget")
location = st.text_input("Location")
date = st.date_input("Event Date")

if st.button("Generate Event Plan"):

    prompt = f"""
    You are an expert event planner.

    Create a detailed event plan based on:

    Event Type: {event_type}
    Guests: {guests}
    Budget: {budget}
    Location: {location}
    Date: {date}

    Include:
    - Theme ideas
    - Decoration plan
    - Food menu
    - Schedule
    - Budget breakdown
    - Tips
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        plan = response.choices[0].message.content

        st.success("✅ Event Plan Generated!")
        st.write(plan)

        # Create PDF
        pdf = create_pdf(plan)

        st.download_button(
            label="📄 Download Plan as PDF",
            data=pdf,
            file_name="event_plan.pdf",
            mime="application/pdf"
        )

    except Exception as e:
        st.error(f"Error: {e}")