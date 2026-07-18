import streamlit as st
from recommendation import recommend_career

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🎯",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------

st.title("🎯 AI Career Advisor")
st.markdown(
    "Find the best career based on your skills, education and interests."
)

st.sidebar.title("About")
st.sidebar.info(
    """
This project is a Rule-Based AI Career Advisor.

Technologies Used

• Python

• Streamlit

• Rule-Based Expert System
"""
)

# ----------------------------
# User Inputs
# ----------------------------

st.header("👤 Candidate Information")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input("Full Name")

    education = st.selectbox(
        "Education",
        [
            "High School",
            "Diploma",
            "Bachelor",
            "Master",
            "PhD"
        ]
    )

with col2:

    experience = st.slider(
        "Experience (Years)",
        0,
        20,
        0
    )

    interest = st.selectbox(
        "Career Interest",
        [
            "Data Analyst",
            "Data Scientist",
            "Business Analyst",
            "Data Engineer",
            "Machine Learning Engineer",
            "AI Engineer",
            "Python Developer",
            "Software Developer",
            "Cloud Engineer",
            "Cyber Security Analyst"
        ]
    )

skills = st.multiselect(
    "Select Your Skills",

    [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Tableau",
        "Statistics",
        "Machine Learning",
        "Deep Learning",
        "Pandas",
        "NumPy",
        "Java",
        "C++",
        "Git",
        "AWS",
        "Azure",
        "Spark",
        "Hadoop",
        "Docker",
        "Kubernetes",
        "Linux",
        "Networking",
        "Flask",
        "Django",
        "Communication",
        "Agile",
        "Requirements Gathering",
        "ETL",
        "Prompt Engineering",
        "NLP"
    ]
)

# ----------------------------
# Analyze Button
# ----------------------------

if st.button("🚀 Analyze My Career", use_container_width=True):

    if not name:

        st.warning("Please enter your name.")

    elif len(skills) == 0:

        st.warning("Please select at least one skill.")

    else:

        result = recommend_career(
            skills,
            interest
        )

        st.success("Career Analysis Completed!")

        st.divider()

        # ----------------------------
        # Candidate Profile
        # ----------------------------

        st.subheader("👤 Candidate Profile")

        c1, c2, c3 = st.columns(3)

        c1.info(name)
        c2.info(education)
        c3.info(f"{experience} Years")

        st.divider()

        # ----------------------------
        # Dashboard Cards
        # ----------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🎯 Recommended Career",
                result["career"]
            )

        with col2:

            st.metric(
                "📊 Match Score",
                f'{result["score"]}%'
            )

        with col3:

            st.metric(
                "💰 Salary",
                result["salary"]
            )

        # ----------------------------
        # Progress
        # ----------------------------

        st.subheader("Career Match")

        st.progress(result["score"] / 100)

        if result["score"] >= 80:

            st.success("Excellent Match")

            readiness = "Advanced"

        elif result["score"] >= 60:

            st.info("Good Match")

            readiness = "Intermediate"

        else:

            st.warning("Needs Improvement")

            readiness = "Beginner"

        st.metric(
            "🚀 Career Readiness",
            readiness
        )

        # ----------------------------
        # Missing Skills
        # ----------------------------

        with st.expander("📌 Missing Skills", expanded=True):

            for skill in result["missing_skills"]:

                st.write("❌", skill)

        # ----------------------------
        # Certifications
        # ----------------------------

        with st.expander("📚 Recommended Certifications"):

            for cert in result["certifications"]:

                st.write("🏆", cert)

        # ----------------------------
        # Projects
        # ----------------------------

        with st.expander("💼 Suggested Projects"):

            for project in result["projects"]:

                st.write("📁", project)

        # ----------------------------
        # Roadmap
        # ----------------------------

        with st.expander("🛣 Learning Roadmap"):

            for i, step in enumerate(result["roadmap"], start=1):

                st.write(f"{i}. {step}")

        # ----------------------------
        # Interview Topics
        # ----------------------------

        with st.expander("🎤 Interview Preparation"):

            for topic in result["interview_topics"]:

                st.write("⭐", topic)

        # ----------------------------
        # Footer
        # ----------------------------

        st.divider()

        st.caption(
            "Developed using Python | Streamlit | Rule-Based AI Expert System"
        )


































































































































































































































































































        