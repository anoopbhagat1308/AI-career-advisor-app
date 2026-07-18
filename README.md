# 🎯 AI Career Advisor

A **Rule-Based AI Career Advisor** built with **Python** and **Streamlit** that helps users discover suitable career paths based on their skills, education, experience, and career interests.

Unlike LLM-based applications, this project uses a **Rule-Based Expert System** to provide intelligent recommendations without requiring API keys, internet connectivity, or heavy AI models.

---

# 📌 Project Overview

Choosing the right career can be overwhelming, especially with the rapidly changing technology landscape. This application analyzes a user's profile and compares it against predefined career requirements to recommend the most suitable career path.

The recommendation engine evaluates the user's skills and identifies the closest career match using a rule-based approach.

---

# ✨ Features

* 🎯 Career recommendation based on skills
* 📊 Career match percentage
* 🚀 Career readiness level
* 📌 Skill gap analysis
* 📚 Recommended certifications
* 🛣️ Personalized learning roadmap
* 💼 Suggested portfolio projects
* 🎤 Interview preparation topics
* 💰 Estimated salary range
* 🎨 Interactive and user-friendly Streamlit interface
* 🔑 No API Keys required
* 🌐 Works completely offline after installation

---

# 🧠 AI Approach

This project implements a **Rule-Based Expert System**, one of the earliest and most widely used forms of Artificial Intelligence.

Instead of using Generative AI or Machine Learning models, the application compares the user's skills against predefined career profiles and recommends the best matching career.

### Recommendation Process

1. User enters their:

   * Education
   * Experience
   * Skills
   * Career Interest

2. The recommendation engine:

   * Compares user skills with required skills for each career
   * Calculates a career match percentage
   * Identifies missing skills
   * Recommends the best career based on matching rules

3. The application displays:

   * Recommended Career
   * Match Score
   * Missing Skills
   * Certifications
   * Learning Roadmap
   * Suggested Projects
   * Interview Topics
   * Salary Estimate

---

# 🏗️ Project Structure

```text
AI_Career_Advisor/
│
├── app.py
├── career_data.py
├── recommendation.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Rule-Based Expert System

---

# 📋 Supported Career Roles

The application currently supports recommendations for:

* Data Analyst
* Data Scientist
* Business Analyst
* Data Engineer
* Machine Learning Engineer
* AI Engineer
* Python Developer
* Software Developer
* Cloud Engineer
* Cyber Security Analyst

---

# ▶️ Installation


### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

# 📸 Application Workflow

1. Enter your personal details.
2. Select your skills.
3. Choose your career interest.
4. Click **Analyze My Career**.
5. Review your personalized career recommendation, skill gaps, certifications, roadmap, projects, interview topics, and salary estimate.

---

# 🎯 Learning Outcomes

This project demonstrates:

* Python programming
* Rule-Based AI concepts
* Expert System design
* Streamlit application development
* Data structures and dictionaries
* Decision-making using conditional logic
* User interface development

---

# 🚀 Future Enhancements

Possible future improvements include:

* PDF report generation
* Resume upload and analysis
* Career recommendation history
* Skill assessment quiz
* Career comparison dashboard
* Interactive data visualizations
* Integration with Generative AI for personalized guidance
* Database support for storing user profiles
* User authentication and login

---

# 👨‍💻 Author

**Anoop Bhagat**

If you found this project helpful, feel free to ⭐ the repository and connect with me on LinkedIn.

---

# 📄 License

This project is created for educational and learning purposes. You are free to use, modify, and enhance it for personal or academic projects.
