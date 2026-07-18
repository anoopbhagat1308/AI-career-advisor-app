

from career_data import career_database

def recommend_career(user_skills, interest=None):

    best_match = None
    highest_score = 0
    best_details = {}

    user_skills = [skill.lower() for skill in user_skills]

    for career, details in career_database.items():

        required_skills = [skill.lower() for skill in details["skills"]]

        matched = [
            skill for skill in required_skills
            if skill in user_skills
        ]

        score = int((len(matched) / len(required_skills)) * 100)

        # Bonus if career matches user's interest
        if interest and interest.lower() == career.lower():
            score += 15

        if score > 100:
            score = 100

        if score > highest_score:

            highest_score = score
            best_match = career
            best_details = details

            missing_skills = [
                skill
                for skill in details["skills"]
                if skill.lower() not in user_skills
            ]

    return {
        "career": best_match,
        "score": highest_score,
        "missing_skills": missing_skills,
        "certifications": best_details["certifications"],
        "projects": best_details["projects"],
        "salary": best_details["salary"],
        "roadmap": best_details["roadmap"],
        "interview_topics": best_details["interview_topics"]
    }