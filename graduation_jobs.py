CAREER_JOB_ROLES = {
    "Software Developer": {
        "roles": [
            "Software Developer",
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Junior Application Developer"
        ],
        "skills": [
            "Python",
            "JavaScript",
            "Data Structures",
            "Git",
            "Problem Solving"
        ],
        "work_areas": [
            "Web application development",
            "Software product development",
            "Application engineering",
            "Startup technology teams"
        ],
        "entry_level": [
            "Junior Software Developer",
            "Graduate Software Engineer",
            "Associate Developer",
            "Software Intern"
        ]
    },

    "AI / Machine Learning Engineer": {
        "roles": [
            "AI Engineer",
            "Machine Learning Engineer",
            "Junior ML Engineer",
            "AI Application Developer",
            "Data/AI Associate"
        ],
        "skills": [
            "Python",
            "Statistics",
            "Machine Learning",
            "Mathematics",
            "Data Analysis"
        ],
        "work_areas": [
            "AI applications",
            "Machine learning systems",
            "Automation",
            "Data-driven products"
        ],
        "entry_level": [
            "AI Intern",
            "ML Intern",
            "Junior AI Engineer",
            "Machine Learning Associate"
        ]
    },

    "Data Analyst / Data Scientist": {
        "roles": [
            "Data Analyst",
            "Business Data Analyst",
            "Junior Data Scientist",
            "Reporting Analyst",
            "Analytics Associate"
        ],
        "skills": [
            "SQL",
            "Python",
            "Statistics",
            "Excel",
            "Data Visualization"
        ],
        "work_areas": [
            "Business analytics",
            "Reporting",
            "Data interpretation",
            "Decision support"
        ],
        "entry_level": [
            "Data Analyst Intern",
            "Junior Data Analyst",
            "Reporting Associate",
            "Analytics Trainee"
        ]
    },

    "Cybersecurity Analyst": {
        "roles": [
            "Cybersecurity Analyst",
            "SOC Analyst",
            "Security Analyst",
            "Information Security Associate",
            "Junior Security Engineer"
        ],
        "skills": [
            "Networking",
            "Linux",
            "Python",
            "Cybersecurity Fundamentals",
            "Problem Solving"
        ],
        "work_areas": [
            "Security monitoring",
            "Incident response",
            "Network security",
            "Security operations"
        ],
        "entry_level": [
            "SOC Analyst Trainee",
            "Cybersecurity Intern",
            "Junior Security Analyst",
            "Security Operations Associate"
        ]
    },

    "Cloud / DevOps Engineer": {
        "roles": [
            "Cloud Engineer",
            "DevOps Engineer",
            "Cloud Support Engineer",
            "Site Reliability Associate",
            "Infrastructure Engineer"
        ],
        "skills": [
            "Linux",
            "Networking",
            "Git",
            "Cloud Fundamentals",
            "Automation"
        ],
        "work_areas": [
            "Cloud infrastructure",
            "Deployment automation",
            "System administration",
            "Infrastructure operations"
        ],
        "entry_level": [
            "Cloud Support Associate",
            "Junior DevOps Engineer",
            "Cloud Intern",
            "Infrastructure Trainee"
        ]
    },

    "Business Analyst": {
        "roles": [
            "Business Analyst",
            "Junior Business Analyst",
            "Operations Analyst",
            "Process Analyst",
            "Business Operations Associate"
        ],
        "skills": [
            "Excel",
            "SQL",
            "Communication",
            "Business Analysis",
            "Presentation"
        ],
        "work_areas": [
            "Business operations",
            "Process improvement",
            "Requirements analysis",
            "Decision support"
        ],
        "entry_level": [
            "Business Analyst Trainee",
            "Operations Associate",
            "Business Analyst Intern",
            "Junior Analyst"
        ]
    },

    "Financial Analyst": {
        "roles": [
            "Financial Analyst",
            "Investment Research Associate",
            "Junior Finance Analyst",
            "Credit Analyst",
            "Financial Planning Associate"
        ],
        "skills": [
            "Excel",
            "Financial Analysis",
            "Accounting",
            "Statistics",
            "Communication"
        ],
        "work_areas": [
            "Financial analysis",
            "Corporate finance",
            "Banking",
            "Investment research"
        ],
        "entry_level": [
            "Finance Analyst Trainee",
            "Financial Analyst Intern",
            "Junior Finance Associate",
            "Research Associate"
        ]
    },

    "UI / UX Designer": {
        "roles": [
            "UI Designer",
            "UX Designer",
            "Product Designer",
            "UX Research Assistant",
            "Visual/Product Design Associate"
        ],
        "skills": [
            "Figma",
            "Design Thinking",
            "Visual Design",
            "Communication",
            "User Research"
        ],
        "work_areas": [
            "Product design",
            "User experience",
            "Interface design",
            "Digital products"
        ],
        "entry_level": [
            "UI/UX Intern",
            "Junior UI Designer",
            "Junior UX Designer",
            "Design Associate"
        ]
    },

    "Mechanical Engineer": {
        "roles": [
            "Mechanical Engineer",
            "Design Engineer",
            "Manufacturing Engineer",
            "Production Engineer",
            "CAD Engineer"
        ],
        "skills": [
            "CAD",
            "Mechanical Design",
            "Engineering Mathematics",
            "Manufacturing",
            "Problem Solving"
        ],
        "work_areas": [
            "Mechanical design",
            "Manufacturing",
            "Production",
            "Automotive and industrial systems"
        ],
        "entry_level": [
            "Graduate Engineer Trainee",
            "Junior Design Engineer",
            "Production Engineer Trainee",
            "Mechanical Engineering Intern"
        ]
    },

    "Electrical / Electronics Engineer": {
        "roles": [
            "Electrical Engineer",
            "Electronics Engineer",
            "Embedded Engineer",
            "Hardware Engineer",
            "Control Systems Associate"
        ],
        "skills": [
            "Circuit Design",
            "Electronics",
            "Programming",
            "Embedded Systems",
            "Problem Solving"
        ],
        "work_areas": [
            "Electronics systems",
            "Embedded systems",
            "Hardware development",
            "Automation"
        ],
        "entry_level": [
            "Graduate Engineer Trainee",
            "Embedded Engineer Intern",
            "Junior Electronics Engineer",
            "Hardware Engineering Associate"
        ]
    }
}


def recommend_graduation_jobs(graduation_recommendations):
    results = []
    seen_careers = set()

    for recommendation in graduation_recommendations[:5]:

        career = recommendation.get("career", "")

        if career in seen_careers:
            continue

        data = CAREER_JOB_ROLES.get(career)

        if not data:
            continue

        seen_careers.add(career)

        results.append({
            "career": career,
            "roles": data["roles"],
            "skills": data["skills"],
            "work_areas": data["work_areas"],
            "entry_level": data["entry_level"]
        })

    return results
