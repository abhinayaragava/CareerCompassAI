# ============================================
# CAREERCOMPASS AI
# AFTER 12TH CAREER INTELLIGENCE
# ============================================

DOMAIN_GUIDANCE = {}

CAREER_GUIDANCE = {}


def get_after12th_career_intelligence(career, domain):
    default = DOMAIN_GUIDANCE.get(
        domain,
        {
            "education_path": "Choose an undergraduate pathway related to this career.",
            "beginner_action": "Explore beginner activities and complete a small project related to this career.",
            "opportunities": [
                "Beginner projects",
                "Subject-related competitions",
                "Clubs and activities",
                "Portfolio-building activities"
            ]
        }
    )

    result = dict(default)
    result.update(CAREER_GUIDANCE.get(career, {}))

    return result

DOMAIN_GUIDANCE.update({
    "Technology & AI": {
        "education_path": "Choose B.Tech/B.E. Computer Science, AI, IT, BCA or B.Sc. Computer Science/Data Science.",
        "beginner_action": "Build a small programming or technology project and strengthen Mathematics and problem-solving.",
        "opportunities": [
            "Coding competitions and hackathons",
            "Technology clubs",
            "Beginner portfolio projects",
            "Programming challenges"
        ]
    },

    "Engineering": {
        "education_path": "Choose a suitable B.Tech/B.E. or engineering-related undergraduate pathway.",
        "beginner_action": "Strengthen Mathematics and Physics and explore a small engineering or electronics project.",
        "opportunities": [
            "Engineering exhibitions",
            "Robotics projects",
            "Technical competitions",
            "Engineering clubs"
        ]
    },

    "Medicine & Healthcare": {
        "education_path": "Choose an appropriate healthcare pathway such as medicine, dentistry, pharmacy, nursing or physiotherapy.",
        "beginner_action": "Strengthen Biology and Chemistry and explore health-science concepts.",
        "opportunities": [
            "Science exhibitions",
            "Biology projects",
            "Health-awareness activities",
            "Science competitions"
        ]
    }
})

DOMAIN_GUIDANCE.update({
    "Business & Finance": {
        "education_path": "Explore B.Com, BBA, Economics, Finance or another business-related undergraduate pathway.",
        "beginner_action": "Practice numerical reasoning, financial concepts and simple business analysis.",
        "opportunities": [
            "Business case studies",
            "Finance competitions",
            "Entrepreneurship clubs",
            "Business projects"
        ]
    },

    "Law": {
        "education_path": "Explore an integrated law pathway such as BA LLB, BBA LLB or B.Com LLB.",
        "beginner_action": "Develop reading, logical reasoning, writing and communication skills.",
        "opportunities": [
            "Debates",
            "Mock parliament activities",
            "Legal-awareness projects",
            "Writing competitions"
        ]
    },

    "Government & Public Service": {
        "education_path": "Choose an undergraduate pathway in humanities, social sciences, economics, public administration or another suitable field.",
        "beginner_action": "Build reading, writing, general-awareness and analytical-thinking habits.",
        "opportunities": [
            "Essay competitions",
            "Debates",
            "Civic projects",
            "General-awareness activities"
        ]
    },

    "Defence": {
        "education_path": "Choose an undergraduate pathway compatible with your defence career goal while maintaining strong academics and physical fitness.",
        "beginner_action": "Develop discipline, fitness, teamwork and leadership through structured activities.",
        "opportunities": [
            "Sports and fitness activities",
            "Leadership activities",
            "Team projects",
            "Defence-awareness activities"
        ]
    },

    "Research & Science": {
        "education_path": "Explore B.Sc., integrated science programs, B.Tech or other research-oriented undergraduate pathways.",
        "beginner_action": "Practice scientific problem-solving and complete small experiments or data projects.",
        "opportunities": [
            "Science exhibitions",
            "Research projects",
            "Science competitions",
            "Laboratory activities"
        ]
    }
})

DOMAIN_GUIDANCE.update({
    "Design & Architecture": {
        "education_path": "Explore B.Arch, B.Des, BFA or another design-focused undergraduate pathway.",
        "beginner_action": "Build a small portfolio and practice sketching, visual thinking or digital design.",
        "opportunities": [
            "Design competitions",
            "Portfolio projects",
            "Creative clubs",
            "Design exhibitions"
        ]
    },

    "Media & Communication": {
        "education_path": "Explore journalism, mass communication, media, communication or related undergraduate study.",
        "beginner_action": "Practice writing, storytelling, presentation and basic content creation.",
        "opportunities": [
            "School publications",
            "Writing competitions",
            "Interview projects",
            "Media clubs"
        ]
    },

    "Education": {
        "education_path": "Choose an undergraduate subject pathway followed by an appropriate teacher-education route.",
        "beginner_action": "Practice explaining concepts clearly and create a small educational resource.",
        "opportunities": [
            "Peer teaching",
            "Tutoring activities",
            "Educational content projects",
            "Academic clubs"
        ]
    },

    "Agriculture & Environment": {
        "education_path": "Explore agriculture, environmental science, horticulture, forestry or related undergraduate study.",
        "beginner_action": "Investigate a local agriculture or environmental problem through observation and research.",
        "opportunities": [
            "Environmental projects",
            "Sustainability activities",
            "Science exhibitions",
            "Nature and agriculture clubs"
        ]
    },

    "Psychology & Social Sciences": {
        "education_path": "Explore psychology, sociology, social work, political science or related social-science pathways.",
        "beginner_action": "Develop observation, communication and research skills through a small survey or social-behaviour project.",
        "opportunities": [
            "Social research projects",
            "Community activities",
            "Psychology clubs",
            "Survey projects"
        ]
    }
})
