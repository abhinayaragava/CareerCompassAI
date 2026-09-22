# CareerCompass AI - Career Recommendation Engine

def get_career_recommendations(profile):
    stage = profile.get("education_stage", "")

    recommendations = []

    # -----------------------------------------
    # AFTER 12TH
    # -----------------------------------------
    if stage == "after_12th":

        stream = (profile.get("twelfth_stream") or "").lower()
        interests = (profile.get("interests_12th") or "").lower()
        direction = (profile.get("career_direction") or "").lower()
        subjects = (profile.get("strongest_subjects") or "").lower()

        # Design & Architecture
        if (
            "design" in interests
            or "architecture" in interests
            or "design" in direction
        ):
            recommendations.extend([
                {
                    "career": "UI/UX Designer",
                    "domain": "Design & Technology",
                    "reason": "Matches your interest in design and creative technology.",
                    "skills": ["UI Design", "UX Research", "Figma", "Design Thinking"]
                },
                {
                    "career": "Architecture",
                    "domain": "Design & Architecture",
                    "reason": "Suitable for students interested in architecture and spatial design.",
                    "skills": ["Drawing", "Design", "3D Modeling", "Architecture Fundamentals"]
                },
                {
                    "career": "Product Designer",
                    "domain": "Design & Technology",
                    "reason": "Combines creativity, technology and user-centered problem solving.",
                    "skills": ["Product Design", "UX", "Prototyping", "Figma"]
                }
            ])

        # Computer / Technology
        if (
            "computer" in subjects
            or "computer" in interests
            or "technology" in interests
            or "software" in interests
        ):
            recommendations.extend([
                {
                    "career": "Software Developer",
                    "domain": "Technology",
                    "reason": "Matches interest in computers and technology.",
                    "skills": ["Python", "Programming", "Data Structures", "Git"]
                },
                {
                    "career": "Data Analyst",
                    "domain": "Data & Technology",
                    "reason": "Suitable for students interested in technology and analytical work.",
                    "skills": ["Python", "SQL", "Statistics", "Data Visualization"]
                },
                {
                    "career": "AI/ML Engineer",
                    "domain": "Artificial Intelligence",
                    "reason": "Combines programming, mathematics and artificial intelligence.",
                    "skills": ["Python", "Machine Learning", "Mathematics", "Data Science"]
                }
            ])

        # Science
        if "science" in stream:
            recommendations.append({
                "career": "Research Scientist",
                "domain": "Science & Research",
                "reason": "Science background can provide a foundation for research-oriented careers.",
                "skills": ["Research", "Scientific Method", "Data Analysis", "Subject Knowledge"]
            })

    # -----------------------------------------
    # AFTER 10TH
    # -----------------------------------------
    elif stage == "after_10th":

        interests = (profile.get("interests_10th") or "").lower()
        pathway = (profile.get("after10_pathway") or "").lower()
        subjects = (profile.get("favorite_subjects") or "").lower()

        if "technology" in interests or "computer" in interests:
            recommendations.extend([
                {
                    "career": "Software Developer",
                    "domain": "Technology",
                    "reason": "Your interests indicate an inclination toward computers and technology.",
                    "skills": ["Programming", "Python", "Problem Solving", "Computer Fundamentals"]
                },
                {
                    "career": "AI/ML Engineer",
                    "domain": "Artificial Intelligence",
                    "reason": "A technology-oriented pathway can lead toward AI and machine learning.",
                    "skills": ["Python", "Mathematics", "Machine Learning", "Data Science"]
                }
            ])

        if "science" in pathway or "science" in subjects:
            recommendations.append({
                "career": "Science & Research",
                "domain": "Science",
                "reason": "Your subject interests indicate a possible science-oriented pathway.",
                "skills": ["Scientific Thinking", "Research", "Mathematics", "Problem Solving"]
            })

        if "defense" in interests or "defence" in interests:
            recommendations.append({
                "career": "Defence Services",
                "domain": "Defence",
                "reason": "You have expressed interest in defence-related careers.",
                "skills": ["Physical Fitness", "Discipline", "Leadership", "General Knowledge"]
            })

    # -----------------------------------------
    # AFTER GRADUATION
    # -----------------------------------------
    elif stage in ["graduation", "after_graduation", "graduate"]:

        interests = (profile.get("interests") or "").lower()
        skills = (profile.get("skills") or "").lower()
        career_goal = (profile.get("career_goal") or "").lower()

        if (
            "software" in interests
            or "technology" in interests
            or "python" in skills
        ):
            recommendations.append({
                "career": "Software Developer",
                "domain": "Technology",
                "reason": "Your profile indicates an interest or skill base in software and technology.",
                "skills": ["Programming", "Data Structures", "Databases", "Git"]
            })

        if "data" in interests or "data" in career_goal:
            recommendations.append({
                "career": "Data Analyst",
                "domain": "Data & Analytics",
                "reason": "Your profile indicates an interest in data-oriented careers.",
                "skills": ["SQL", "Python", "Statistics", "Data Visualization"]
            })

        if "ai" in interests or "machine learning" in interests:
            recommendations.append({
                "career": "AI/ML Engineer",
                "domain": "Artificial Intelligence",
                "reason": "Your interests indicate an AI and machine-learning direction.",
                "skills": ["Python", "Machine Learning", "Deep Learning", "Mathematics"]
            })

    # -----------------------------------------
    # FALLBACK
    # -----------------------------------------
    if not recommendations:
        recommendations.append({
            "career": "Career Exploration",
            "domain": "Multiple Domains",
            "reason": "More profile information is needed to generate highly personalized recommendations.",
            "skills": ["Aptitude Assessment", "Interest Assessment", "Skill Assessment"]
        })

    return recommendations
