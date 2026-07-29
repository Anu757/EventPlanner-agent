## 📌 Project Overview

The **AI Event Planner** is a smart web application that helps users plan events efficiently using Artificial Intelligence. Built with Streamlit and powered by the Groq API, the system generates structured event plans including budget, timeline, and vendor suggestions. It also allows users to download the plan as a professionally formatted PDF.

---

## ❗ Problem Statement

Planning an event can be time-consuming and complex. Users often struggle with:
- Organizing event details efficiently  
- Estimating budgets accurately  
- Creating timelines and schedules  
- Finding suitable vendors  

Traditional planning requires manual effort, which can lead to errors, missed tasks, and poor organization.

---

## 💡 Proposed Solution

This project provides an **AI-driven solution** that:
- Automatically generates complete event plans  
- Structures content into clear sections (Overview, Budget, Timeline, Vendors)  
- Reduces manual effort and planning time  
- Provides a downloadable PDF for easy sharing and documentation  

The system leverages AI to deliver quick, accurate, and well-organized event planning assistance.

---

## 🗂️ Project Structure
event-planner/
│── app.py # Main Streamlit application
│── requirements.txt # Dependencies
│── logo.png # Logo for PDF
│── .env # API keys (not uploaded to GitHub)


---

## ⚙️ How to Use the Agent

Follow these steps to run the project:


1. Clone the Repository

git clone https://github.com/your-username/Recipe-Generator-Agent.git
cd Recipe-Generator-Agent

3. Create Virtual Environment

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

3. Install Dependencies
   
pip install -r requirements.txt

4. Add API Key

Create a .env file and add:

GROQ_API_KEY=your_api_key_here

5. Run the Application

streamlit run app.py


🧠 How the Agent Works
1.User enters event details (e.g., birthday, wedding, corporate event)
2.The AI processes the input using Groq API
3.A structured event plan is generated
4.The app formats the plan into sections
5.A downloadable PDF is created

🎯 Output
Detailed event plan
Organized sections
Professional PDF document



