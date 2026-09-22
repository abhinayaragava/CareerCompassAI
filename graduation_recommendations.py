import re


GRADUATION_CAREERS = [
    {
        "career": "Software Developer",
        "domain": "Technology & Software",
        "degree_keywords": [
            "computer", "cse", "software", "information technology",
            "it", "bca", "mca", "engineering"
        ],
        "interest_keywords": [
            "software", "programming", "coding", "web", "app",
            "technology", "development", "computer"
        ],
        "skills": [
            "Python", "JavaScript", "Data Structures",
            "Git", "Problem Solving"
        ],
        "work_styles": [
            "Technology / Computer",
            "Independent / Innovation"
        ],
        "goals": [
            "Get a job",
            "Build a startup or business"
        ],
        "education_path": "B.Tech/B.E. CSE, IT, Software Engineering, BCA/MCA or related computer degree.",
        "beginner_action": "Build one small software project and publish it in a GitHub portfolio.",
        "opportunities": [
            "Software companies",
            "Startups",
            "Freelancing",
            "Web and mobile development"
        ]
    },

    {
        "career": "AI / Machine Learning Engineer",
        "domain": "Technology & Software",
        "degree_keywords": [
            "computer", "cse", "ai", "machine learning", "data",
            "statistics", "mathematics", "information technology",
            "engineering"
        ],
        "interest_keywords": [
            "ai", "artificial intelligence", "machine learning",
            "deep learning", "data", "automation", "python"
        ],
        "skills": [
            "Python", "Mathematics", "Statistics",
            "Machine Learning", "Problem Solving"
        ],
        "work_styles": [
            "Technology / Computer",
            "Research / Lab",
            "Independent / Innovation"
        ],
        "goals": [
            "Get a job",
            "Higher studies",
            "Build a startup or business"
        ],
        "education_path": "Computer Science, AI/ML, Data Science, Mathematics, Statistics or related postgraduate study can strengthen this pathway.",
        "beginner_action": "Learn Python and build a small machine-learning project using a public dataset.",
        "opportunities": [
            "AI startups",
            "Technology companies",
            "Research labs",
            "AI product teams"
        ]
    },

    {
        "career": "Data Analyst / Data Scientist",
        "domain": "Data & Analytics",
        "degree_keywords": [
            "data", "statistics", "mathematics", "computer",
            "computer science", "economics", "commerce", "business",
            "engineering"
        ],
        "interest_keywords": [
            "data", "analytics", "statistics", "business intelligence",
            "research", "numbers", "dashboards"
        ],
        "skills": [
            "Python", "SQL", "Statistics", "Excel",
            "Data Visualization"
        ],
        "work_styles": [
            "Numbers / Data",
            "Research / Lab",
            "Technology / Computer"
        ],
        "goals": [
            "Get a job",
            "Higher studies"
        ],
        "education_path": "Statistics, Mathematics, Computer Science, Data Science, Economics, Engineering or related degrees are useful foundations.",
        "beginner_action": "Learn SQL and Excel/Python, then complete a small real-world data analysis project.",
        "opportunities": [
            "Analytics teams",
            "FinTech",
            "Business intelligence",
            "Research organizations"
        ]
    },

    {
        "career": "Cybersecurity Analyst",
        "domain": "Technology & Software",
        "degree_keywords": [
            "computer", "cse", "information technology", "it",
            "cyber", "security", "engineering"
        ],
        "interest_keywords": [
            "cybersecurity", "security", "ethical hacking",
            "networking", "privacy", "cyber"
        ],
        "skills": [
            "Networking", "Linux", "Python",
            "Cybersecurity Fundamentals", "Problem Solving"
        ],
        "work_styles": [
            "Technology / Computer",
            "Structured Rules",
            "Independent / Innovation"
        ],
        "goals": [
            "Get a job",
            "Higher studies"
        ],
        "education_path": "Computer Science, IT, Cybersecurity or related engineering degrees followed by cybersecurity specialization or certifications.",
        "beginner_action": "Learn networking and Linux fundamentals and practice safely in beginner cybersecurity labs.",
        "opportunities": [
            "Security operations",
            "Cybersecurity companies",
            "Banks and FinTech",
            "Government security teams"
        ]
    },

    {
        "career": "Cloud / DevOps Engineer",
        "domain": "Technology & Software",
        "degree_keywords": [
            "computer", "cse", "information technology",
            "it", "engineering", "software"
        ],
        "interest_keywords": [
            "cloud", "devops", "servers", "automation",
            "infrastructure", "technology"
        ],
        "skills": [
            "Linux", "Networking", "Git",
            "Cloud Fundamentals", "Automation"
        ],
        "work_styles": [
            "Technology / Computer",
            "Independent / Innovation"
        ],
        "goals": [
            "Get a job",
            "Higher studies"
        ],
        "education_path": "Computer Science, IT, Software Engineering or related degrees with cloud and DevOps specialization.",
        "beginner_action": "Learn Linux, Git and basic cloud services and deploy a small application.",
        "opportunities": [
            "Cloud companies",
            "Technology firms",
            "DevOps teams",
            "Infrastructure engineering"
        ]
    },

    {
        "career": "Business Analyst",
        "domain": "Business & Finance",
        "degree_keywords": [
            "business", "bba", "mba", "commerce", "economics",
            "management", "engineering", "computer", "information technology"
        ],
        "interest_keywords": [
            "business", "analytics", "management", "strategy",
            "finance", "problem solving", "process"
        ],
        "skills": [
            "Excel", "SQL", "Communication",
            "Business Analysis", "Presentation"
        ],
        "work_styles": [
            "Numbers / Data",
            "Managing / Leading",
            "Speaking / Writing"
        ],
        "goals": [
            "Get a job",
            "Higher studies",
            "Build a startup or business"
        ],
        "education_path": "Business, Commerce, Economics, Management, Engineering and Computer-related degrees can lead into business analysis with suitable skills.",
        "beginner_action": "Learn Excel and business analysis basics and solve a small business case study.",
        "opportunities": [
            "Consulting",
            "Technology companies",
            "Banks and FinTech",
            "Business operations"
        ]
    },

    {
        "career": "Financial Analyst",
        "domain": "Business & Finance",
        "degree_keywords": [
            "finance", "commerce", "accounting", "economics",
            "business", "bcom", "mba", "management"
        ],
        "interest_keywords": [
            "finance", "investment", "accounting", "markets",
            "banking", "money", "economics"
        ],
        "skills": [
            "Excel", "Financial Analysis",
            "Accounting", "Statistics", "Communication"
        ],
        "work_styles": [
            "Numbers / Data",
            "Structured Rules",
            "Speaking / Writing"
        ],
        "goals": [
            "Get a job",
            "Higher studies",
            "Prepare for competitive exams"
        ],
        "education_path": "Commerce, Finance, Economics, Accounting or Management degrees with finance specialization can support this pathway.",
        "beginner_action": "Strengthen accounting and Excel and analyze a simple company's financial statements.",
        "opportunities": [
            "Banks",
            "Investment firms",
            "FinTech",
            "Corporate finance"
        ]
    },

    {
        "career": "UI / UX Designer",
        "domain": "Design & Creative Careers",
        "degree_keywords": [
            "design", "fine arts", "visual", "computer",
            "multimedia", "communication", "engineering"
        ],
        "interest_keywords": [
            "design", "ui", "ux", "creative", "visual",
            "graphics", "user experience", "art"
        ],
        "skills": [
            "Figma", "Design Thinking",
            "Visual Design", "Communication", "User Research"
        ],
        "work_styles": [
            "Creative / Design",
            "Technology / Computer",
            "Independent / Innovation"
        ],
        "goals": [
            "Get a job",
            "Build a startup or business"
        ],
        "education_path": "Design, visual communication, computer or related degrees can be combined with UI/UX specialization and portfolio work.",
        "beginner_action": "Learn Figma and redesign one familiar app or website as a portfolio project.",
        "opportunities": [
            "Product companies",
            "Design studios",
            "Startups",
            "Freelancing"
        ]
    },

    {
        "career": "Research Scientist / Researcher",
        "domain": "Research & Science",
        "degree_keywords": [
            "science", "physics", "chemistry", "biology",
            "mathematics", "statistics", "biotechnology",
            "computer science", "engineering"
        ],
        "interest_keywords": [
            "research", "science", "experiments", "laboratory",
            "discovery", "mathematics", "physics", "biology"
        ],
        "skills": [
            "Research", "Statistics", "Scientific Writing",
            "Problem Solving", "Data Analysis"
        ],
        "work_styles": [
            "Research / Lab",
            "Independent / Innovation"
        ],
        "goals": [
            "Higher studies",
            "Get a job"
        ],
        "education_path": "Bachelor's degree followed by master's/PhD or specialized research training depending on the research field.",
        "beginner_action": "Choose a research topic, read beginner papers and complete a small structured research project.",
        "opportunities": [
            "Universities",
            "Research institutes",
            "R&D teams",
            "Scientific organizations"
        ]
    },

    {
        "career": "Mechanical Engineer",
        "domain": "Engineering & Technical",
        "degree_keywords": [
            "mechanical", "manufacturing", "automobile",
            "production", "engineering"
        ],
        "interest_keywords": [
            "mechanical", "machines", "manufacturing",
            "automobile", "design", "mechanics"
        ],
        "skills": [
            "CAD", "Engineering Mathematics",
            "Mechanical Design", "Problem Solving", "Manufacturing"
        ],
        "work_styles": [
            "Hands-on / Practical",
            "Outdoors / Field",
            "Technology / Computer"
        ],
        "goals": [
            "Get a job",
            "Higher studies"
        ],
        "education_path": "B.E./B.Tech Mechanical Engineering or related engineering degree, followed by specialization where useful.",
        "beginner_action": "Build a small CAD or mechanical design project and document the engineering process.",
        "opportunities": [
            "Manufacturing",
            "Automotive",
            "Industrial engineering",
            "Product development"
        ]
    },

    {
        "career": "Electrical / Electronics Engineer",
        "domain": "Engineering & Technical",
        "degree_keywords": [
            "electrical", "electronics", "eee", "ece",
            "embedded", "engineering"
        ],
        "interest_keywords": [
            "electronics", "electrical", "circuits",
            "embedded", "robotics", "hardware"
        ],
        "skills": [
            "Circuit Design", "Electronics",
            "Programming", "Problem Solving", "Embedded Systems"
        ],
        "work_styles": [
            "Hands-on / Practical",
            "Technology / Computer",
            "Research / Lab"
        ],
        "goals": [
            "Get a job",
            "Higher studies"
        ],
        "education_path": "B.E./B.Tech Electrical, Electronics, ECE or related engineering degree with specialization.",
        "beginner_action": "Build a small electronics or embedded project and document the circuit and code.",
        "opportunities": [
            "Electronics companies",
            "Embedded systems",
            "Power sector",
            "Robotics and automation"
        ]
    },

    {
        "career": "Education / EdTech Specialist",
        "domain": "Education",
        "degree_keywords": [
            "education", "english", "mathematics",
            "science", "computer", "psychology",
            "communication"
        ],
        "interest_keywords": [
            "teaching", "education", "learning",
            "students", "training", "edtech"
        ],
        "skills": [
            "Communication", "Teaching",
            "Presentation", "Content Creation", "Technology"
        ],
        "work_styles": [
            "People / Helping",
            "Speaking / Writing",
            "Technology / Computer"
        ],
        "goals": [
            "Get a job",
            "Higher studies",
            "Build a startup or business"
        ],
        "education_path": "Subject expertise plus teacher training, education, instructional design or EdTech specialization depending on the target role.",
        "beginner_action": "Create a short educational lesson or learning resource and test it with learners.",
        "opportunities": [
            "Schools and colleges",
            "EdTech companies",
            "Training organizations",
            "Educational content teams"
        ]
    },

    {
        "career": "Public Policy / Government Analyst",
        "domain": "Government & Public Service",
        "degree_keywords": [
            "political science", "economics", "public administration",
            "law", "social science", "history", "commerce",
            "business"
        ],
        "interest_keywords": [
            "government", "policy", "public service",
            "civil services", "society", "governance",
            "administration"
        ],
        "skills": [
            "Research", "Communication",
            "Policy Analysis", "Writing", "Data Analysis"
        ],
        "work_styles": [
            "Structured Rules",
            "Speaking / Writing",
            "Research / Lab"
        ],
        "goals": [
            "Prepare for competitive exams",
            "Get a job",
            "Higher studies"
        ],
        "education_path": "Social Sciences, Economics, Law, Public Administration and related degrees can lead into policy and public-service pathways.",
        "beginner_action": "Choose one public issue and prepare a short evidence-based policy analysis.",
        "opportunities": [
            "Government departments",
            "Policy organizations",
            "Think tanks",
            "Public-sector projects"
        ]
    }
]


def _clean(value):
    if value is None:
        return ""
    return str(value).strip().lower()


def _tokens(value):
    text = _clean(value)
    return set(re.findall(r"[a-z0-9+#./&-]+", text))


def _keyword_match(text, keywords):
    normalized = _clean(text)
    return any(keyword.lower() in normalized for keyword in keywords)


def recommend_graduation_careers(
    degree="",
    branch="",
    cgpa="",
    domain="",
    goal="",
    work_style="",
    interests="",
    skills=""
):
    degree_text = f"{degree} {branch}"
    interest_text = interests
    skill_text = skills

    results = []

    # Convert CGPA / percentage into a supporting score.
    try:
        cgpa_value = float(str(cgpa).strip())
    except (ValueError, TypeError):
        cgpa_value = 0

    for item in GRADUATION_CAREERS:

        breakdown = {
            "Career Domain": 0,
            "Career Goal": 0,
            "Work Style": 0,
            "Career Interests": 0,
            "Degree / Branch": 0,
            "Skills": 0
        }

        # --------------------------------------
        # 1. CAREER DOMAIN: maximum 25
        # --------------------------------------
        selected_domain = _clean(domain)

        if selected_domain == _clean(item["domain"]):
            breakdown["Career Domain"] = 25

        elif selected_domain == "not sure — help me decide":
            breakdown["Career Domain"] = 10

        # --------------------------------------
        # 2. CAREER GOAL: maximum 15
        # --------------------------------------
        if any(
            _clean(goal) == _clean(g)
            for g in item["goals"]
        ):
            breakdown["Career Goal"] = 15

        # --------------------------------------
        # 3. WORK STYLE: maximum 15
        # --------------------------------------
        if any(
            _clean(work_style) == _clean(w)
            for w in item["work_styles"]
        ):
            breakdown["Work Style"] = 15

        # --------------------------------------
        # 4. CAREER INTERESTS: maximum 20
        # --------------------------------------
        matched_interests = [
            keyword
            for keyword in item["interest_keywords"]
            if _keyword_match(interest_text, [keyword])
        ]

        if matched_interests:
            breakdown["Career Interests"] = min(
                20,
                5 * len(matched_interests)
            )

        # --------------------------------------
        # 5. DEGREE / BRANCH: maximum 15
        # --------------------------------------
        if _keyword_match(
            degree_text,
            item["degree_keywords"]
        ):
            breakdown["Degree / Branch"] = 10

            # CGPA provides a small additional
            # academic-support score.
            if cgpa_value >= 8.0:
                breakdown["Degree / Branch"] += 5

            elif cgpa_value >= 7.0:
                breakdown["Degree / Branch"] += 3

            elif cgpa_value >= 6.0:
                breakdown["Degree / Branch"] += 1

        # --------------------------------------
        # 6. SKILLS: maximum 10
        # --------------------------------------
        matched_skills = [
            skill
            for skill in item["skills"]
            if _keyword_match(skill_text, [skill])
        ]

        if matched_skills:
            breakdown["Skills"] = min(
                10,
                2 * len(matched_skills)
            )

        # --------------------------------------
        # FINAL SCORE
        # --------------------------------------
        score = min(
            100,
            sum(breakdown.values())
        )

        matched_factors = [
            name
            for name, value in breakdown.items()
            if value > 0
        ]

        # --------------------------------------
        # WHY THIS CAREER MATCHES
        # --------------------------------------
        why_match = []

        if breakdown["Career Domain"]:
            if selected_domain == _clean(item["domain"]):
                why_match.append(
                    f"Your selected domain aligns with {item['career']}."
                )
            else:
                why_match.append(
                    "Your profile indicates flexibility across career domains."
                )

        if breakdown["Career Goal"]:
            why_match.append(
                f"Your career goal matches the typical pathway for {item['career']}."
            )

        if breakdown["Work Style"]:
            why_match.append(
                f"Your preferred work style is relevant to {item['career']}."
            )

        if matched_interests:
            interest_names = ", ".join(matched_interests[:4])
            why_match.append(
                f"Your interests match areas such as {interest_names}."
            )

        if breakdown["Degree / Branch"]:
            why_match.append(
                f"Your {degree} / {branch} background is relevant to this career."
            )

        if matched_skills:
            skill_names = ", ".join(matched_skills[:4])
            why_match.append(
                f"Your current skills include relevant areas such as {skill_names}."
            )

        if not why_match:
            why_match.append(
                "This career is included as an exploratory option based on your profile."
            )

        # --------------------------------------
        # ADD RESULT
        # --------------------------------------
        results.append({
            "career": item["career"],
            "domain": item["domain"],
            "score": score,
            "degree_paths": item["education_path"],
            "skills": item["skills"],
            "why_match": why_match,
            "matched_factors": matched_factors,
            "match_breakdown": breakdown,
            "beginner_action": item["beginner_action"],
            "opportunities": item["opportunities"]
        })

    # Highest score first
    results.sort(
        key=lambda item: (
            item["score"],
            len(item["matched_factors"])
        ),
        reverse=True
    )

    return results[:8]
