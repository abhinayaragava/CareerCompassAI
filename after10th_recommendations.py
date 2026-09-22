# ============================================================
# CareerCompass AI
# After 10th Recommendation Engine
# ============================================================

import re


AFTER_10TH_PATHWAYS = [

    {
        "pathway": "Science & Mathematics",
        "icon": "🔬",
        "description": "Physics, Chemistry, Mathematics and pure sciences",
        "careers": [
            "Engineering",
            "Pure Sciences",
            "Data Science",
            "Research",
            "Technology"
        ],
        "next_step": "Consider Science with Mathematics in Classes 11 and 12."
    },

    {
        "pathway": "Commerce & Business",
        "icon": "💼",
        "description": "Business, accounting, finance and economics",
        "careers": [
            "Chartered Accountancy",
            "Finance",
            "Banking",
            "Business Management",
            "Economics"
        ],
        "next_step": "Consider Commerce and develop an interest in mathematics, economics and business."
    },

    {
        "pathway": "Humanities & Social Sciences",
        "icon": "📚",
        "description": "History, geography, politics, psychology and society",
        "careers": [
            "Law",
            "Civil Services",
            "Psychology",
            "Journalism",
            "Social Sciences"
        ],
        "next_step": "Consider Humanities and explore subjects such as history, political science, geography and psychology."
    },

    {
        "pathway": "Computer & Technology",
        "icon": "💻",
        "description": "Programming, IT, AI and digital technologies",
        "careers": [
            "Software Development",
            "Artificial Intelligence",
            "Cybersecurity",
            "Data Science",
            "Information Technology"
        ],
        "next_step": "Develop basic programming and computer skills while choosing your higher-secondary pathway."
    },

    {
        "pathway": "Engineering & Technical",
        "icon": "⚙️",
        "description": "Engineering, electronics, mechanics and technical fields",
        "careers": [
            "Mechanical Engineering",
            "Electrical Engineering",
            "Civil Engineering",
            "Electronics",
            "Automation"
        ],
        "next_step": "Consider Science with Mathematics or a technical diploma pathway."
    },

    {
        "pathway": "Medicine & Healthcare",
        "icon": "🩺",
        "description": "Medicine, nursing, pharmacy and healthcare",
        "careers": [
            "Medicine",
            "Nursing",
            "Pharmacy",
            "Physiotherapy",
            "Medical Laboratory Science"
        ],
        "next_step": "Build strong foundations in Biology and Chemistry and explore healthcare careers."
    },

    {
        "pathway": "Defence & Armed Forces",
        "icon": "🛡️",
        "description": "Army, Navy, Air Force and defence careers",
        "careers": [
            "Indian Army",
            "Indian Navy",
            "Indian Air Force",
            "Defence Technology",
            "Defence Services"
        ],
        "next_step": "Maintain strong academics, physical fitness and discipline while exploring defence pathways."
    },

    {
        "pathway": "Police & Uniformed Services",
        "icon": "👮",
        "description": "Police, paramilitary and uniformed careers",
        "careers": [
            "Police Services",
            "Paramilitary Services",
            "Public Safety",
            "Security Services"
        ],
        "next_step": "Develop physical fitness, discipline and awareness of public-service career pathways."
    },

    {
        "pathway": "Arts, Design & Architecture",
        "icon": "🎨",
        "description": "Design, architecture, fine arts and creative careers",
        "careers": [
            "Architecture",
            "Graphic Design",
            "UI/UX Design",
            "Fine Arts",
            "Fashion Design"
        ],
        "next_step": "Build a creative portfolio and explore design, architecture and visual-arts pathways."
    },

    {
        "pathway": "Agriculture & Environment",
        "icon": "🌱",
        "description": "Agriculture, environmental science and sustainability",
        "careers": [
            "Agriculture",
            "Environmental Science",
            "Forestry",
            "Food Technology",
            "Sustainability"
        ],
        "next_step": "Explore agriculture, biology, environmental science and sustainability-related opportunities."
    },

    {
        "pathway": "Sports & Fitness",
        "icon": "🏃",
        "description": "Sports, fitness, physical education and athletics",
        "careers": [
            "Professional Sports",
            "Physical Education",
            "Fitness Training",
            "Sports Management",
            "Sports Science"
        ],
        "next_step": "Develop your sporting ability, physical fitness and knowledge of sports-related careers."
    },

    {
        "pathway": "Vocational & Skill-Based",
        "icon": "🛠️",
        "description": "Practical and industry-oriented career pathways",
        "careers": [
            "Technical Services",
            "Healthcare Support",
            "IT Support",
            "Hospitality",
            "Skilled Services"
        ],
        "next_step": "Explore practical skill-based courses and vocational education opportunities."
    },

    {
        "pathway": "ITI & Skilled Trades",
        "icon": "🔧",
        "description": "Electrical, mechanical, automotive and other trades",
        "careers": [
            "Electrician",
            "Automobile Technician",
            "Fitter",
            "Welder",
            "Mechanic"
        ],
        "next_step": "Explore ITI trades and practical technical training options."
    },

    {
        "pathway": "Diploma & Polytechnic",
        "icon": "🏗️",
        "description": "Technical diploma and practical engineering pathways",
        "careers": [
            "Diploma Engineering",
            "Civil Engineering",
            "Mechanical Engineering",
            "Electrical Engineering",
            "Computer Engineering"
        ],
        "next_step": "Explore Polytechnic diploma programs and their progression opportunities."
    },

    {
        "pathway": "Aviation",
        "icon": "✈️",
        "description": "Aircraft, aviation operations and related careers",
        "careers": [
            "Aviation Operations",
            "Aircraft Maintenance",
            "Airport Management",
            "Cabin Crew",
            "Aerospace"
        ],
        "next_step": "Explore aviation-related education, technical training and eligibility requirements."
    }
]



def recommend_after10th_pathways(
    interests=None,
    favorite_subjects=None,
    career_interests=None,
    activity_interest=None,
    selected_pathways=None
):




    """
    Recommend suitable pathways after Class 10.

    The function uses the student's interests, subjects,
    career interests and activities to identify relevant
    pathways.
    """

    def normalize(value):
        if not value:
            return []
        if isinstance(value, (list, tuple, set)):
            return [str(item).strip() for item in value if str(item).strip()]
        return [item.strip() for item in str(value).split(",") if item.strip()]

    interests = normalize(interests)
    favorite_subjects = normalize(favorite_subjects)
    career_interests = normalize(career_interests)
    activity_interest = normalize(activity_interest)
    selected_pathways = normalize(selected_pathways)

    # Normalize pathway names coming from the HTML form
    # to the canonical names used by the recommendation engine.
    pathway_aliases = {
        "Arts Design Architecture": "Arts, Design & Architecture",
        "Vocational & Skill Based": "Vocational & Skill-Based"
    }

    selected_pathways = [
        pathway_aliases.get(pathway, pathway)
        for pathway in selected_pathways
    ]

    # Convert everything into searchable text.
    student_text = " ".join(
        [str(item) for item in interests]
        + [str(item) for item in favorite_subjects]
        + [str(item) for item in career_interests]
        + [str(activity_interest)]
    ).lower()

    keyword_map = {

        "Science & Mathematics": [
            "science",
            "math",
            "mathematics",
            "physics",
            "chemistry",
            "research"
        ],

        "Commerce & Business": [
            "commerce",
            "business",
            "finance",
            "accounting",
            "economics",
            "money"
        ],

        "Humanities & Social Sciences": [
            "humanities",
            "history",
            "geography",
            "politics",
            "psychology",
            "society",
            "social"
        ],

        "Computer & Technology": [
            "computer",
            "technology",
            "programming",
            "coding",
            "software",
            "ai",
            "artificial intelligence",
            "cybersecurity",
            "data"
        ],

        "Engineering & Technical": [
            "engineering",
            "technical",
            "electronics",
            "mechanical",
            "machines",
            "robotics"
        ],

        "Medicine & Healthcare": [
            "medicine",
            "medical",
            "healthcare",
            "doctor",
            "nursing",
            "pharmacy",
            "biology"
        ],

        "Defence & Armed Forces": [
            "defence",
            "army",
            "navy",
            "air force",
            "military",
            "armed forces"
        ],

        "Police & Uniformed Services": [
            "police",
            "paramilitary",
            "uniform",
            "security"
        ],

        "Arts, Design & Architecture": [
            "art",
            "design",
            "drawing",
            "creative",
            "architecture",
            "fashion",
            "ui",
            "ux"
        ],

        "Agriculture & Environment": [
            "agriculture",
            "farming",
            "environment",
            "nature",
            "sustainability",
            "forestry"
        ],

        "Sports & Fitness": [
            "sports",
            "sport",
            "fitness",
            "athletics",
            "football",
            "cricket",
            "running"
        ],

        "Vocational & Skill-Based": [
            "vocational",
            "practical",
            "skill",
            "hands-on"
        ],

        "ITI & Skilled Trades": [
            "iti",
            "electrician",
            "mechanic",
            "automobile",
            "fitter",
            "welding"
        ],

        "Diploma & Polytechnic": [
            "diploma",
            "polytechnic",
            "technical diploma"
        ],

        "Aviation": [
            "aviation",
            "aircraft",
            "airport",
            "pilot",
            "aerospace"
        ]
    }

    # Activity-based signals from the profile form.
    activity_pathway_map = {
        "Solving mathematical problems": [
            "Science & Mathematics",
            "Computer & Technology",
            "Engineering & Technical",
            "Diploma & Polytechnic"
        ],
        "Using computers and technology": [
            "Computer & Technology",
            "Science & Mathematics",
            "Engineering & Technical"
        ],
        "Building or repairing things": [
            "Engineering & Technical",
            "ITI & Skilled Trades",
            "Vocational & Skill-Based",
            "Diploma & Polytechnic"
        ],
        "Helping and caring for people": [
            "Medicine & Healthcare",
            "Humanities & Social Sciences",
            "Police & Uniformed Services"
        ],
        "Drawing and designing": [
            "Arts, Design & Architecture"
        ],
        "Reading and writing": [
            "Humanities & Social Sciences"
        ],
        "Business and managing money": [
            "Commerce & Business"
        ],
        "Understanding society and people": [
            "Humanities & Social Sciences"
        ],
        "Nature and environment": [
            "Agriculture & Environment",
            "Science & Mathematics"
        ]
    }

    def find_matches(items, keywords, limit=2):
        matches = []

        for item in items:
            item_text = str(item).lower()

            for keyword in keywords:
                pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

                if re.search(pattern, item_text):
                    if keyword not in matches:
                        matches.append(keyword)

        return matches[:limit]

    scored_pathways = []

    for pathway in AFTER_10TH_PATHWAYS:

        name = pathway["pathway"]
        keywords = keyword_map.get(name, [])

        score = 0

        # Explicitly selected pathway = strongest signal.
        if name in selected_pathways:
            score += 10

        subject_matches = find_matches(
            favorite_subjects,
            keywords,
            limit=2
        )

        interest_matches = find_matches(
            interests,
            keywords,
            limit=2
        )

        career_matches = find_matches(
            career_interests,
            keywords,
            limit=2
        )

        score += len(subject_matches) * 3
        score += len(interest_matches) * 4
        score += len(career_matches) * 5

        if activity_interest:
            if name in activity_pathway_map.get(
                activity_interest[0],
                []
            ):
                score += 2

        signals = []

        if name in selected_pathways:
            signals.append("your selected pathway")

        if career_matches:
            signals.append(
                "career interests: " + ", ".join(career_matches)
            )

        if interest_matches:
            signals.append(
                "interests: " + ", ".join(interest_matches)
            )

        if subject_matches:
            signals.append(
                "subjects: " + ", ".join(subject_matches)
            )

        if activity_interest and name in activity_pathway_map.get(
            activity_interest[0],
            []
        ):
            signals.append(
                "activity: " + activity_interest[0]
            )

        if signals:
            why_recommended = (
                "Recommended based on " +
                "; ".join(signals[:3]) +
                "."
            )
        else:
            why_recommended = (
                "This pathway may be worth exploring "
                "based on your broader profile."
            )

        scored_pathways.append(
            {
                "pathway": name,
                "icon": pathway["icon"],
                "description": pathway["description"],
                "careers": pathway["careers"],
                "next_step": pathway["next_step"],
                "why_recommended": why_recommended,
                "score": score
            }
        )

    # Sort by relevance.
    scored_pathways.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    # If no specific match exists, provide broad options.
    matched = [
        item for item in scored_pathways
        if item["score"] > 0
    ]

    if not matched:
        return scored_pathways[:5]

    return matched[:5]




# ==========================================
# AFTER 10TH INDIVIDUAL CAREER RECOMMENDATIONS
# ==========================================

AFTER_10TH_CAREERS = {

    "Science & Mathematics": [
        {
            "career": "Research Scientist",
            "keywords": ["research", "science", "physics", "chemistry", "biology", "experiments"],
            "subjects": ["science", "physics", "chemistry", "biology", "mathematics"],
            "activities": ["Solving mathematical problems", "Nature and environment"]
        },
        {
            "career": "Data Scientist",
            "keywords": ["data", "mathematics", "analytics", "artificial intelligence", "ai"],
            "subjects": ["mathematics", "science", "computer science"],
            "activities": ["Solving mathematical problems", "Using computers and technology"]
        },
        {
            "career": "Physicist",
            "keywords": ["physics", "science", "research", "space"],
            "subjects": ["physics", "science", "mathematics"],
            "activities": ["Solving mathematical problems", "Nature and environment"]
        },
        {
            "career": "Mathematician",
            "keywords": ["mathematics", "math", "numbers", "logical"],
            "subjects": ["mathematics", "math"],
            "activities": ["Solving mathematical problems"]
        }
    ],

    "Commerce & Business": [
        {
            "career": "Chartered Accountant",
            "keywords": ["accounting", "finance", "commerce", "business", "money"],
            "subjects": ["mathematics", "commerce", "economics"],
            "activities": ["Business and managing money"]
        },
        {
            "career": "Financial Analyst",
            "keywords": ["finance", "financial", "economics", "data", "investment"],
            "subjects": ["mathematics", "economics", "commerce"],
            "activities": ["Business and managing money", "Solving mathematical problems"]
        },
        {
            "career": "Business Manager",
            "keywords": ["business", "management", "entrepreneurship", "leadership"],
            "subjects": ["commerce", "economics", "mathematics"],
            "activities": ["Business and managing money"]
        },
        {
            "career": "Economist",
            "keywords": ["economics", "finance", "policy", "business", "data"],
            "subjects": ["economics", "mathematics", "commerce"],
            "activities": ["Business and managing money", "Understanding society and people"]
        }
    ],

    "Humanities & Social Sciences": [
        {
            "career": "Lawyer",
            "keywords": ["law", "legal", "justice", "rights", "politics"],
            "subjects": ["history", "politics", "social science", "humanities"],
            "activities": ["Reading and writing", "Understanding society and people"]
        },
        {
            "career": "Psychologist",
            "keywords": ["psychology", "people", "behaviour", "mental", "counseling"],
            "subjects": ["psychology", "biology", "social science"],
            "activities": ["Understanding society and people", "Helping and caring for people"]
        },
        {
            "career": "Journalist",
            "keywords": ["journalism", "media", "writing", "news", "communication"],
            "subjects": ["language", "english", "humanities", "social science"],
            "activities": ["Reading and writing", "Understanding society and people"]
        },
        {
            "career": "Civil Services Professional",
            "keywords": ["civil services", "government", "public service", "administration", "policy"],
            "subjects": ["history", "politics", "geography", "social science"],
            "activities": ["Reading and writing", "Understanding society and people"]
        }
    ],

    "Computer & Technology": [
        {
            "career": "Software Developer",
            "keywords": ["coding", "programming", "software", "computer", "technology", "app", "web"],
            "subjects": ["mathematics", "computer science", "science"],
            "activities": ["Using computers and technology", "Solving mathematical problems"]
        },
        {
            "career": "AI / Machine Learning Engineer",
            "keywords": ["ai", "artificial intelligence", "machine learning", "programming", "data"],
            "subjects": ["mathematics", "computer science", "science"],
            "activities": ["Using computers and technology", "Solving mathematical problems"]
        },
        {
            "career": "Cybersecurity Analyst",
            "keywords": ["cybersecurity", "security", "hacking", "computer", "network"],
            "subjects": ["mathematics", "computer science", "science"],
            "activities": ["Using computers and technology", "Solving mathematical problems"]
        },
        {
            "career": "Data Scientist",
            "keywords": ["data", "analytics", "mathematics", "ai", "artificial intelligence"],
            "subjects": ["mathematics", "computer science", "science"],
            "activities": ["Using computers and technology", "Solving mathematical problems"]
        }
    ],

    "Engineering & Technical": [
        {
            "career": "Mechanical Engineer",
            "keywords": ["mechanical", "machines", "engineering", "automobile", "robotics"],
            "subjects": ["mathematics", "physics", "science"],
            "activities": ["Building or repairing things", "Solving mathematical problems"]
        },
        {
            "career": "Electrical Engineer",
            "keywords": ["electrical", "electronics", "circuits", "engineering"],
            "subjects": ["mathematics", "physics", "science"],
            "activities": ["Building or repairing things", "Solving mathematical problems"]
        },
        {
            "career": "Civil Engineer",
            "keywords": ["civil", "construction", "architecture", "infrastructure", "engineering"],
            "subjects": ["mathematics", "physics", "science"],
            "activities": ["Building or repairing things", "Solving mathematical problems"]
        },
        {
            "career": "Electronics Engineer",
            "keywords": ["electronics", "circuits", "embedded", "engineering", "technology"],
            "subjects": ["mathematics", "physics", "science"],
            "activities": ["Building or repairing things", "Using computers and technology"]
        }
    ],

    "Medicine & Healthcare": [
        {
            "career": "Doctor",
            "keywords": ["medicine", "doctor", "health", "biology", "medical"],
            "subjects": ["biology", "chemistry", "science"],
            "activities": ["Helping and caring for people"]
        },
        {
            "career": "Pharmacist",
            "keywords": ["pharmacy", "medicine", "health", "biology", "chemistry"],
            "subjects": ["biology", "chemistry", "science"],
            "activities": ["Helping and caring for people"]
        },
        {
            "career": "Physiotherapist",
            "keywords": ["physiotherapy", "health", "fitness", "rehabilitation", "medical"],
            "subjects": ["biology", "science"],
            "activities": ["Helping and caring for people"]
        },
        {
            "career": "Medical Laboratory Professional",
            "keywords": ["laboratory", "medical", "biology", "diagnostic", "science"],
            "subjects": ["biology", "chemistry", "science"],
            "activities": ["Helping and caring for people", "Nature and environment"]
        }
    ],

    "Defence & Armed Forces": [
        {
            "career": "Indian Army Officer",
            "keywords": ["army", "defence", "military", "leadership", "service"],
            "subjects": ["mathematics", "science", "social science"],
            "activities": ["Building or repairing things", "Helping and caring for people"]
        },
        {
            "career": "Indian Navy Officer",
            "keywords": ["navy", "defence", "military", "maritime", "engineering"],
            "subjects": ["mathematics", "physics", "science"],
            "activities": ["Solving mathematical problems", "Building or repairing things"]
        },
        {
            "career": "Indian Air Force Officer",
            "keywords": ["air force", "defence", "aviation", "military", "pilot"],
            "subjects": ["mathematics", "physics", "science"],
            "activities": ["Solving mathematical problems", "Using computers and technology"]
        },
        {
            "career": "Defence Technology Professional",
            "keywords": ["defence technology", "engineering", "technology", "robotics"],
            "subjects": ["mathematics", "physics", "computer science"],
            "activities": ["Using computers and technology", "Building or repairing things"]
        }
    ],

    "Police & Uniformed Services": [
        {
            "career": "Police Services",
            "keywords": ["police", "law", "security", "public safety"],
            "subjects": ["social science", "history", "politics"],
            "activities": ["Understanding society and people", "Helping and caring for people"]
        },
        {
            "career": "Paramilitary Services",
            "keywords": ["paramilitary", "security", "defence", "public safety"],
            "subjects": ["social science", "science"],
            "activities": ["Helping and caring for people"]
        },
        {
            "career": "Public Safety Professional",
            "keywords": ["public safety", "emergency", "security", "service"],
            "subjects": ["science", "social science"],
            "activities": ["Helping and caring for people"]
        }
    ],

    "Arts, Design & Architecture": [
        {
            "career": "Architect",
            "keywords": ["architecture", "architect", "design", "drawing"],
            "subjects": ["mathematics", "physics", "art", "design"],
            "activities": ["Drawing and designing"]
        },
        {
            "career": "UI / UX Designer",
            "keywords": ["ui", "ux", "design", "digital", "creative"],
            "subjects": ["computer science", "art", "design"],
            "activities": ["Drawing and designing", "Using computers and technology"]
        },
        {
            "career": "Graphic Designer",
            "keywords": ["graphic", "design", "creative", "visual", "art"],
            "subjects": ["art", "design", "humanities"],
            "activities": ["Drawing and designing"]
        },
        {
            "career": "Fashion Designer",
            "keywords": ["fashion", "design", "creative", "textile"],
            "subjects": ["art", "design"],
            "activities": ["Drawing and designing"]
        }
    ],

    "Agriculture & Environment": [
        {
            "career": "Agricultural Scientist",
            "keywords": ["agriculture", "farming", "biology", "crop", "science"],
            "subjects": ["biology", "science", "chemistry"],
            "activities": ["Nature and environment"]
        },
        {
            "career": "Environmental Scientist",
            "keywords": ["environment", "climate", "sustainability", "science"],
            "subjects": ["science", "biology", "geography"],
            "activities": ["Nature and environment"]
        },
        {
            "career": "Forestry Professional",
            "keywords": ["forestry", "forest", "nature", "environment"],
            "subjects": ["biology", "science", "geography"],
            "activities": ["Nature and environment"]
        }
    ],

    "Sports & Fitness": [
        {
            "career": "Professional Athlete",
            "keywords": ["sports", "athletics", "football", "cricket", "running"],
            "subjects": ["physical education", "science"],
            "activities": ["Sports", "Fitness"]
        },
        {
            "career": "Fitness Trainer",
            "keywords": ["fitness", "training", "exercise", "health"],
            "subjects": ["physical education", "biology"],
            "activities": ["Sports", "Fitness"]
        },
        {
            "career": "Sports Management Professional",
            "keywords": ["sports management", "sports", "business", "management"],
            "subjects": ["commerce", "economics", "physical education"],
            "activities": ["Sports", "Business and managing money"]
        }
    ],

    "Vocational & Skill-Based": [
        {
            "career": "IT Support Professional",
            "keywords": ["it support", "computer", "technical", "technology"],
            "subjects": ["computer science", "mathematics"],
            "activities": ["Using computers and technology"]
        },
        {
            "career": "Hospitality Professional",
            "keywords": ["hospitality", "hotel", "tourism", "service"],
            "subjects": ["commerce", "languages"],
            "activities": ["Helping and caring for people"]
        },
        {
            "career": "Technical Services Professional",
            "keywords": ["technical", "repair", "maintenance", "practical"],
            "subjects": ["mathematics", "science"],
            "activities": ["Building or repairing things"]
        }
    ],

    "ITI & Skilled Trades": [
        {
            "career": "Electrician",
            "keywords": ["electrician", "electrical", "wiring", "circuits"],
            "subjects": ["mathematics", "science"],
            "activities": ["Building or repairing things"]
        },
        {
            "career": "Automobile Technician",
            "keywords": ["automobile", "automotive", "vehicle", "mechanic"],
            "subjects": ["mathematics", "science"],
            "activities": ["Building or repairing things"]
        },
        {
            "career": "Fitter",
            "keywords": ["fitter", "mechanical", "machines", "technical"],
            "subjects": ["mathematics", "science"],
            "activities": ["Building or repairing things"]
        }
    ],

    "Diploma & Polytechnic": [
        {
            "career": "Diploma Engineering Professional",
            "keywords": ["diploma", "engineering", "technical"],
            "subjects": ["mathematics", "science"],
            "activities": ["Building or repairing things", "Solving mathematical problems"]
        },
        {
            "career": "Diploma Computer Engineer",
            "keywords": ["computer", "programming", "software", "technology"],
            "subjects": ["mathematics", "computer science"],
            "activities": ["Using computers and technology"]
        },
        {
            "career": "Diploma Civil Engineer",
            "keywords": ["civil", "construction", "engineering"],
            "subjects": ["mathematics", "physics"],
            "activities": ["Building or repairing things"]
        }
    ],

    "Aviation": [
        {
            "career": "Pilot",
            "keywords": ["pilot", "aviation", "aircraft", "flying"],
            "subjects": ["mathematics", "physics", "science"],
            "activities": ["Solving mathematical problems", "Using computers and technology"]
        },
        {
            "career": "Aircraft Maintenance Professional",
            "keywords": ["aircraft", "maintenance", "aviation", "mechanical"],
            "subjects": ["mathematics", "physics", "science"],
            "activities": ["Building or repairing things"]
        },
        {
            "career": "Airport Operations Professional",
            "keywords": ["airport", "aviation", "operations", "management"],
            "subjects": ["commerce", "mathematics"],
            "activities": ["Business and managing money"]
        }
    ]
}



# ==========================================
# AFTER 10TH CAREER-SPECIFIC GUIDANCE
# ==========================================

AFTER_10TH_CAREER_GUIDANCE = {

    "Software Developer": {
        "education": "Class 11–12 with Mathematics and Computer Science, followed by a computer science or software-related degree or diploma.",
        "skills": ["Programming", "Problem Solving", "Logical Thinking", "Computer Fundamentals"],
        "action": "Start with a beginner programming project such as a calculator, quiz app or simple webpage."
    },

    "AI / Machine Learning Engineer": {
        "education": "Class 11–12 with Mathematics and Computer Science, followed by higher education in computer science, AI, data science or a related field.",
        "skills": ["Python", "Mathematics", "Data Analysis", "Problem Solving"],
        "action": "Learn basic Python and begin exploring simple data and AI concepts."
    },

    "Cybersecurity Analyst": {
        "education": "Class 11–12 with Mathematics and Computer Science, followed by cybersecurity, computer science or related higher education.",
        "skills": ["Computer Networks", "Cybersecurity Basics", "Problem Solving", "Digital Safety"],
        "action": "Learn computer and network fundamentals and explore beginner cybersecurity concepts."
    },

    "Data Scientist": {
        "education": "Class 11–12 with Mathematics and Computer Science, followed by higher education in data science, statistics, mathematics or computer science.",
        "skills": ["Mathematics", "Statistics", "Programming", "Data Analysis"],
        "action": "Start learning spreadsheets or Python and practice simple data-analysis problems."
    },

    "Mechanical Engineer": {
        "education": "Class 11–12 with Mathematics and Physics, followed by mechanical engineering or a related technical pathway.",
        "skills": ["Mathematics", "Physics", "Problem Solving", "Mechanical Reasoning"],
        "action": "Build or study a simple mechanical project and learn how basic machines work."
    },

    "Electrical Engineer": {
        "education": "Class 11–12 with Mathematics and Physics, followed by electrical engineering or a related technical pathway.",
        "skills": ["Mathematics", "Physics", "Circuit Fundamentals", "Problem Solving"],
        "action": "Learn basic electrical circuits and document a simple circuit experiment."
    },

    "Electronics Engineer": {
        "education": "Class 11–12 with Mathematics and Physics, followed by electronics, electrical engineering or a related technical pathway.",
        "skills": ["Electronics", "Circuits", "Problem Solving", "Programming Basics"],
        "action": "Begin with simple electronics concepts and a small microcontroller or circuit project."
    },

    "Civil Engineer": {
        "education": "Class 11–12 with Mathematics and Physics, followed by civil engineering or a related technical pathway.",
        "skills": ["Mathematics", "Physics", "Technical Drawing", "Problem Solving"],
        "action": "Explore basic structural concepts and create a small model or technical drawing."
    },

    "Research Scientist": {
        "education": "Class 11–12 with strong Science subjects, followed by higher education and research in a chosen scientific field.",
        "skills": ["Scientific Thinking", "Research", "Mathematics", "Data Interpretation"],
        "action": "Choose a science topic you enjoy and conduct a small observation or experiment."
    },

    "Physicist": {
        "education": "Class 11–12 with Mathematics and Physics, followed by higher education in physics or a related science field.",
        "skills": ["Mathematics", "Physics", "Scientific Reasoning", "Problem Solving"],
        "action": "Practice physics problems and explore simple experiments that connect theory to real life."
    },

    "Mathematician": {
        "education": "Class 11–12 with strong Mathematics, followed by higher education in mathematics or a related quantitative field.",
        "skills": ["Mathematics", "Logical Reasoning", "Proof Thinking", "Problem Solving"],
        "action": "Solve progressively harder mathematical and logical problems."
    },

    "Chartered Accountant": {
        "education": "Class 11–12 with Commerce, followed by professional accounting education and training.",
        "skills": ["Accounting", "Numerical Ability", "Financial Understanding", "Attention to Detail"],
        "action": "Build a foundation in accounting and practice basic financial calculations."
    },

    "Financial Analyst": {
        "education": "Class 11–12 with Commerce and/or Mathematics, followed by higher education in finance, economics, business or a related field.",
        "skills": ["Financial Analysis", "Mathematics", "Data Analysis", "Decision Making"],
        "action": "Learn basic financial concepts and practice analysing simple tables or datasets."
    },

    "Business Manager": {
        "education": "Class 11–12 with Commerce or another suitable stream, followed by business or management education.",
        "skills": ["Communication", "Leadership", "Decision Making", "Business Awareness"],
        "action": "Start a small project or activity where you plan, organize and manage tasks."
    },

    "Economist": {
        "education": "Class 11–12 with Economics and Mathematics where available, followed by higher education in economics or a related field.",
        "skills": ["Economics", "Mathematics", "Data Analysis", "Critical Thinking"],
        "action": "Follow a simple economic issue and explain it using data or graphs."
    },

    "Lawyer": {
        "education": "Class 11–12 in a suitable stream, followed by legal education and professional training.",
        "skills": ["Reading", "Writing", "Logical Reasoning", "Communication"],
        "action": "Develop strong reading and writing habits and discuss current issues using evidence."
    },

    "Psychologist": {
        "education": "Class 11–12 with subjects suitable for psychology and social science interests, followed by higher education in psychology.",
        "skills": ["Observation", "Communication", "Empathy", "Analytical Thinking"],
        "action": "Read beginner psychology material and practise careful observation and reflective writing."
    },

    "Journalist": {
        "education": "Class 11–12 in a suitable stream, followed by journalism, media or communication-related higher education.",
        "skills": ["Writing", "Research", "Communication", "Critical Thinking"],
        "action": "Write a short article or school-news story based on verified information."
    },

    "Civil Services Professional": {
        "education": "Choose a suitable Class 11–12 stream, then pursue higher education in an area that supports the student's interests before preparing for relevant public-service examinations.",
        "skills": ["General Awareness", "Reading", "Writing", "Analytical Thinking"],
        "action": "Build a daily habit of reading reliable current-affairs and general-knowledge material."
    },

    "Doctor": {
        "education": "Class 11–12 with Biology, Physics and Chemistry, followed by medical education and professional training.",
        "skills": ["Biology", "Scientific Thinking", "Communication", "Attention to Detail"],
        "action": "Strengthen Biology and Chemistry fundamentals and explore how the human body works."
    },

    "Pharmacist": {
        "education": "Class 11–12 with Science subjects including Biology or other subjects appropriate to the chosen pharmacy pathway, followed by pharmacy education.",
        "skills": ["Chemistry", "Biology", "Attention to Detail", "Scientific Thinking"],
        "action": "Build strong foundations in Chemistry and Biology and explore basic medicine-related science."
    },

    "Physiotherapist": {
        "education": "Class 11–12 with Science subjects suitable for allied-health pathways, followed by physiotherapy education.",
        "skills": ["Biology", "Communication", "Observation", "Patient Care"],
        "action": "Learn basic human anatomy and explore the role of exercise and rehabilitation in health."
    },

    "Medical Laboratory Professional": {
        "education": "Class 11–12 with Science subjects, followed by medical laboratory or allied-health education.",
        "skills": ["Biology", "Chemistry", "Observation", "Accuracy"],
        "action": "Explore basic laboratory science and practise careful observation and recording."
    },

    "Architect": {
        "education": "Choose Class 11–12 subjects that support mathematics, design and spatial reasoning, followed by architecture education.",
        "skills": ["Mathematics", "Drawing", "Spatial Thinking", "Design"],
        "action": "Start a design sketchbook and practise basic drawing, shapes and spatial layouts."
    },

    "UI / UX Designer": {
        "education": "Class 11–12 with a suitable academic or creative pathway, followed by design, technology or related higher education.",
        "skills": ["Visual Design", "Problem Solving", "User Research", "Communication"],
        "action": "Redesign a simple app or webpage on paper and explain why your design is easier to use."
    },

    "Graphic Designer": {
        "education": "Class 11–12 in a suitable academic or creative pathway, followed by design, visual communication or related higher education.",
        "skills": ["Visual Design", "Typography", "Creativity", "Communication"],
        "action": "Create a small poster or digital design collection and explain the design choices."
    },

    "Fashion Designer": {
        "education": "Class 11–12 in a suitable academic or creative pathway, followed by fashion or design education.",
        "skills": ["Drawing", "Creativity", "Visual Thinking", "Material Awareness"],
        "action": "Create simple clothing sketches and explore colour, pattern and material choices."
    }

}


# ==========================================
# AFTER 10TH CAREER-SPECIFIC OPPORTUNITIES
# ==========================================

AFTER_10TH_CAREER_OPPORTUNITIES = {

    "Software Developer": [
        "Coding competitions and hackathons",
        "Beginner programming projects",
        "School technology clubs",
        "Web-development learning challenges"
    ],

    "AI / Machine Learning Engineer": [
        "Programming and AI learning challenges",
        "Mathematics and science competitions",
        "Beginner data projects",
        "Technology clubs and project exhibitions"
    ],

    "Cybersecurity Analyst": [
        "Cybersecurity awareness competitions",
        "Networking and computer clubs",
        "Beginner security challenges",
        "Technology project exhibitions"
    ],

    "Data Scientist": [
        "Mathematics and statistics competitions",
        "Data-analysis projects",
        "Coding competitions",
        "Science and technology project exhibitions"
    ],

    "Mechanical Engineer": [
        "Robotics projects",
        "Science and engineering exhibitions",
        "Model-building activities",
        "Technical clubs and competitions"
    ],

    "Electrical Engineer": [
        "Electronics projects",
        "Science exhibitions",
        "Circuit-building activities",
        "Technical clubs"
    ],

    "Electronics Engineer": [
        "Electronics and robotics projects",
        "Science exhibitions",
        "Embedded-systems learning activities",
        "Technical competitions"
    ],

    "Civil Engineer": [
        "Model-building projects",
        "Science and engineering exhibitions",
        "Technical drawing activities",
        "Infrastructure and design projects"
    ],

    "Research Scientist": [
        "Science exhibitions",
        "Science and mathematics competitions",
        "Independent observation projects",
        "School research clubs"
    ],

    "Physicist": [
        "Physics problem-solving competitions",
        "Science exhibitions",
        "Physics projects",
        "Astronomy and science clubs"
    ],

    "Mathematician": [
        "Mathematics competitions",
        "Logical reasoning challenges",
        "Mathematics clubs",
        "Independent problem-solving projects"
    ],

    "Chartered Accountant": [
        "Commerce and accounting competitions",
        "Business clubs",
        "Financial-literacy projects",
        "Entrepreneurship activities"
    ],

    "Financial Analyst": [
        "Mathematics and business competitions",
        "Financial-literacy activities",
        "Spreadsheet and data projects",
        "Business clubs"
    ],

    "Business Manager": [
        "Entrepreneurship projects",
        "Business-plan competitions",
        "Student leadership activities",
        "School enterprise projects"
    ],

    "Economist": [
        "Economics competitions",
        "Data and statistics projects",
        "Debates and policy discussions",
        "Business and economics clubs"
    ],

    "Lawyer": [
        "Debates",
        "Public-speaking activities",
        "Essay and writing competitions",
        "Mock-trial or legal-awareness activities"
    ],

    "Psychologist": [
        "Psychology clubs",
        "Social-science projects",
        "Observation and research activities",
        "Essay and presentation competitions"
    ],

    "Journalist": [
        "School journalism",
        "Writing competitions",
        "Debates and public speaking",
        "Student media projects"
    ],

    "Civil Services Professional": [
        "General-knowledge competitions",
        "Debates and essay competitions",
        "Current-affairs discussions",
        "Community and civic projects"
    ],

    "Doctor": [
        "Science and biology competitions",
        "Health-awareness projects",
        "Science exhibitions",
        "Biology clubs"
    ],

    "Pharmacist": [
        "Science exhibitions",
        "Chemistry and biology projects",
        "Health-science activities",
        "Science clubs"
    ],

    "Physiotherapist": [
        "Health and fitness activities",
        "Biology projects",
        "Sports-science activities",
        "Wellness awareness projects"
    ],

    "Medical Laboratory Professional": [
        "Science exhibitions",
        "Biology and chemistry projects",
        "Laboratory-skill activities",
        "Science clubs"
    ],

    "Architect": [
        "Drawing and design competitions",
        "Architecture aptitude practice",
        "Model-making projects",
        "Design portfolios"
    ],

    "UI / UX Designer": [
        "Design challenges",
        "App and website redesign projects",
        "Digital design portfolios",
        "Technology and design clubs"
    ],

    "Graphic Designer": [
        "Poster and visual-design competitions",
        "Digital design projects",
        "Creative portfolios",
        "Art and design clubs"
    ],

    "Fashion Designer": [
        "Fashion and design projects",
        "Sketching activities",
        "Creative exhibitions",
        "Design portfolios"
    ]
}


def get_after10th_career_guidance(career):
    return AFTER_10TH_CAREER_GUIDANCE.get(
        career,
        {
            "education": "Explore a suitable Class 11–12 pathway and compare relevant higher-education options for this career.",
            "skills": ["Communication", "Problem Solving", "Digital Literacy", "Learning Skills"],
            "action": "Research the career, its education requirements and beginner skills, then try a small related activity."
        }
    )


def recommend_after10th_careers(
    pathway_recommendations,
    interests=None,
    favorite_subjects=None,
    career_interests=None,
    activity_interest=None
):
    """Rank individual careers within the student's strongest pathways."""

    if not pathway_recommendations:
        return []

    def normalize_items(value):
        if not value:
            return []
        if isinstance(value, (list, tuple, set)):
            return [str(item).strip().lower() for item in value if str(item).strip()]
        return [item.strip().lower() for item in str(value).split(",") if item.strip()]

    interests = normalize_items(interests)
    favorite_subjects = normalize_items(favorite_subjects)
    career_interests = normalize_items(career_interests)
    activity_interest = normalize_items(activity_interest)

    career_recommendations = []

    for pathway in pathway_recommendations[:3]:
        pathway_name = pathway["pathway"]

        # Skip generic "Not Sure" as a career container.
        careers = AFTER_10TH_CAREERS.get(pathway_name, [])

        for career_data in careers:
            score = 0
            reasons = []

            career_interest_points = 0
            interest_points = 0
            subject_points = 0
            activity_points = 0

            career_keywords = [item.lower() for item in career_data["keywords"]]
            subject_keywords = [item.lower() for item in career_data["subjects"]]
            activity_options = [item.lower() for item in career_data["activities"]]

            for item in career_interests:
                if any(
                    re.search(r"\b" + re.escape(keyword) + r"\b", item)
                    for keyword in career_keywords
                ):
                    score += 5
                    career_interest_points += 5
                    reasons.append("your career interests")

            for item in interests:
                if any(
                    re.search(r"\b" + re.escape(keyword) + r"\b", item)
                    for keyword in career_keywords
                ):
                    score += 4
                    interest_points += 4
                    reasons.append("your interests")

            for item in favorite_subjects:
                if any(
                    re.search(r"\b" + re.escape(keyword) + r"\b", item)
                    for keyword in subject_keywords
                ):
                    score += 3
                    subject_points += 3
                    reasons.append("your subjects")

            if activity_interest:
                if any(
                    activity == item
                    for activity in activity_options
                    for item in activity_interest
                ):
                    score += 2
                    activity_points += 2
                    reasons.append("your preferred activity")

            # Carry a small portion of the pathway score into career ranking.
            pathway_score = pathway.get("score", 0)
            pathway_points = min(pathway_score, 10)
            score += pathway_points

            # Prevent zero-score careers from appearing.
            if score <= 0:
                continue

            unique_reasons = []
            for reason in reasons:
                if reason not in unique_reasons:
                    unique_reasons.append(reason)

            if not unique_reasons:
                unique_reasons.append("your selected pathway")

            guidance = get_after10th_career_guidance(
                career_data["career"]
            )

            opportunities = AFTER_10TH_CAREER_OPPORTUNITIES.get(
                career_data["career"],
                []
            )

            career_recommendations.append(
                {
                    "career": career_data["career"],
                    "pathway": pathway_name,
                    "score": score,
                    "score_breakdown": {
                        "Career Interest": career_interest_points,
                        "Interest Match": interest_points,
                        "Subject Match": subject_points,
                        "Activity Match": activity_points,
                        "Pathway Alignment": pathway_points
                    },
                    "why_match": "Matched " + ", ".join(unique_reasons) + ".",
                    "keywords": career_data["keywords"],
                    "subjects": career_data["subjects"],
                    "activities": career_data["activities"],
                    "education": guidance["education"],
                    "skills_to_build": guidance["skills"],
                    "beginner_action": guidance["action"],
                    "opportunities": opportunities
                }
            )

    career_recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    # Keep only the strongest match for each career.
    unique_careers = []
    seen_careers = set()

    for recommendation in career_recommendations:
        career_name = recommendation["career"]

        if career_name in seen_careers:
            continue

        seen_careers.add(career_name)
        unique_careers.append(recommendation)

    return unique_careers[:8]


# ==========================================
# AFTER 10TH STREAM / PATHWAY GUIDANCE
# ==========================================

AFTER_10TH_STREAM_GUIDANCE = {
    "Science & Mathematics": {
        "streams": [
            "MPC / PCM",
            "BiPC / PCB",
            "PCMB"
        ],
        "description": "Suitable for students interested in mathematics, engineering, technology, medicine, pure sciences and research.",
        "next_step": "Choose subjects in Classes 11 and 12 that match your intended career direction and strengthen Mathematics or Biology as required."
    },

    "Commerce & Business": {
        "streams": [
            "Commerce with Mathematics",
            "Commerce without Mathematics"
        ],
        "description": "Suitable for students interested in business, finance, accounting, economics, management and entrepreneurship.",
        "next_step": "Explore Commerce subjects and identify whether Mathematics is useful for your intended higher-education or career path."
    },

    "Humanities & Social Sciences": {
        "streams": [
            "Humanities / Arts",
            "Social Sciences"
        ],
        "description": "Suitable for students interested in society, history, politics, psychology, languages, law, education and public service.",
        "next_step": "Explore Humanities subjects and identify the areas that match your interests and future career goals."
    },

    "Computer & Technology": {
        "streams": [
            "Science with Mathematics and Computer Science",
            "Computer-related vocational courses",
            "Diploma / Polytechnic routes"
        ],
        "description": "Suitable for students interested in programming, artificial intelligence, cybersecurity, data and digital technologies.",
        "next_step": "Build foundational computer and programming skills and choose a Class 11–12 or diploma route that supports technology careers."
    },

    "Engineering & Technical": {
        "streams": [
            "Science with Mathematics",
            "Diploma / Polytechnic",
            "ITI and technical trades"
        ],
        "description": "Suitable for students interested in engineering, machines, electronics, infrastructure and technical problem-solving.",
        "next_step": "Strengthen Mathematics and Science and explore engineering, diploma and technical education routes."
    },

    "Medicine & Healthcare": {
        "streams": [
            "BiPC / PCB",
            "PCMB"
        ],
        "description": "Suitable for students interested in medicine, healthcare, biology, pharmacy and allied health sciences.",
        "next_step": "Focus on Biology, Chemistry and Physics and explore healthcare-related education pathways."
    },

    "Defence & Armed Forces": {
        "streams": [
            "Science with Mathematics",
            "Science with Biology",
            "Any suitable higher-secondary stream depending on the future entry route"
        ],
        "description": "Suitable for students interested in defence services, disciplined careers, leadership and national service.",
        "next_step": "Build strong academics, physical fitness, communication and general-awareness skills while exploring future defence-entry requirements."
    },

    "Police & Uniformed Services": {
        "streams": [
            "Science",
            "Commerce",
            "Humanities"
        ],
        "description": "Suitable for students interested in police, public safety, administration and other uniformed services.",
        "next_step": "Maintain strong academics and physical fitness while exploring the eligibility requirements for future uniformed-service opportunities."
    },

    "Arts, Design & Architecture": {
        "streams": [
            "Humanities / Arts",
            "Science with Mathematics",
            "Design-focused vocational routes"
        ],
        "description": "Suitable for students interested in creativity, visual communication, architecture, design and related fields.",
        "next_step": "Develop creative skills and build a portfolio while selecting subjects that support your intended design or architecture pathway."
    },

    "Agriculture & Environment": {
        "streams": [
            "Science with Biology",
            "Science with Agriculture",
            "Agriculture-focused vocational routes"
        ],
        "description": "Suitable for students interested in agriculture, environment, food systems, natural resources and sustainability.",
        "next_step": "Explore Biology, Agriculture and Environmental Science-related subjects and education routes."
    },

    "Sports & Fitness": {
        "streams": [
            "Any suitable higher-secondary stream",
            "Sports-focused vocational routes"
        ],
        "description": "Suitable for students interested in sports, fitness, physical education and sports-related careers.",
        "next_step": "Continue academic studies while developing your sporting skills, fitness and participation record."
    },

    "Vocational & Skill-Based": {
        "streams": [
            "Vocational higher-secondary courses",
            "ITI",
            "Diploma / Polytechnic"
        ],
        "description": "Suitable for students who prefer practical, skill-oriented learning and faster entry into technical or service careers.",
        "next_step": "Explore vocational, ITI and diploma options that match your preferred occupation."
    },

    "ITI & Skilled Trades": {
        "streams": [
            "ITI trades",
            "Skill-development programs"
        ],
        "description": "Suitable for students interested in practical technical trades and hands-on careers.",
        "next_step": "Identify an ITI trade that matches your interests and compare its training, apprenticeship and career opportunities."
    },

    "Diploma & Polytechnic": {
        "streams": [
            "Engineering Diploma",
            "Technical Diploma",
            "Other Polytechnic programs"
        ],
        "description": "Suitable for students interested in practical technical education and diploma-level engineering or technology.",
        "next_step": "Explore diploma specializations and their eligibility, duration and progression opportunities."
    },

    "Aviation": {
        "streams": [
            "Science with Mathematics",
            "Science with Biology",
            "Aviation-focused vocational routes"
        ],
        "description": "Suitable for students interested in aviation, airport operations, aircraft-related careers and aviation services.",
        "next_step": "Explore aviation careers and check the academic and physical requirements for the specific role you are interested in."
    },

    "Not Sure": {
        "streams": [
            "Science",
            "Commerce",
            "Humanities",
            "Vocational / Diploma routes"
        ],
        "description": "You do not need to decide immediately. Exploring different subject areas can help you identify a suitable direction.",
        "next_step": "Compare your strongest subjects, interests and preferred work style before choosing your Class 11–12 pathway."
    }
}


def generate_after10th_stream_guidance(recommendations):

    if not recommendations:
        return []

    guidance = []

    for recommendation in recommendations[:5]:

        pathway = recommendation["pathway"]

        if pathway in AFTER_10TH_STREAM_GUIDANCE:

            information = AFTER_10TH_STREAM_GUIDANCE[pathway]

            guidance.append(
                {
                    "pathway": pathway,
                    "icon": recommendation["icon"],
                    "streams": information["streams"],
                    "description": information["description"],
                    "next_step": information["next_step"]
                }
            )

    return guidance


# ==========================================
# AFTER 10TH COMPETITIVE EXAM GUIDANCE
# ==========================================

AFTER_10TH_EXAM_GUIDANCE = {
    "Science & Mathematics": [
        {
            "exam": "NTSE-style scholarship and aptitude exams",
            "focus": "Academic aptitude, mathematics, science and general reasoning",
            "purpose": "Useful for strengthening academic aptitude and exploring scholarship-oriented opportunities."
        },
        {
            "exam": "Olympiads",
            "focus": "Mathematics, science and logical problem-solving",
            "purpose": "Useful for students who enjoy subject-based challenges and competitive academic learning."
        }
    ],

    "Computer & Technology": [
        {
            "exam": "Computer and coding competitions",
            "focus": "Programming, computational thinking and problem-solving",
            "purpose": "Useful for developing programming ability and exploring technology interests."
        },
        {
            "exam": "Science and mathematics Olympiads",
            "focus": "Mathematics, science and logical reasoning",
            "purpose": "Useful for strengthening the academic foundation needed for future technology studies."
        }
    ],

    "Commerce & Business": [
        {
            "exam": "Commerce and aptitude competitions",
            "focus": "Mathematics, economics, business awareness and reasoning",
            "purpose": "Useful for developing an early foundation for commerce and business-related studies."
        }
    ],

    "Humanities & Social Sciences": [
        {
            "exam": "General aptitude and scholarship examinations",
            "focus": "Reasoning, language, social awareness and general knowledge",
            "purpose": "Useful for strengthening academic aptitude and broad knowledge."
        }
    ],

    "Engineering & Technical": [
        {
            "exam": "Science and mathematics Olympiads",
            "focus": "Mathematics, physics, science and problem-solving",
            "purpose": "Useful for strengthening the academic foundation for future technical studies."
        }
    ],

    "Medicine & Healthcare": [
        {
            "exam": "Science and biology Olympiads",
            "focus": "Biology, chemistry, science and scientific reasoning",
            "purpose": "Useful for students interested in biology and healthcare-related learning."
        }
    ],

    "Defence & Armed Forces": [
        {
            "exam": "Defence awareness and aptitude preparation",
            "focus": "General knowledge, reasoning, mathematics, discipline and physical fitness",
            "purpose": "Useful for beginning early preparation for future defence-service opportunities."
        }
    ],

    "Police & Uniformed Services": [
        {
            "exam": "General aptitude and physical-readiness preparation",
            "focus": "Reasoning, general knowledge, communication and physical fitness",
            "purpose": "Useful for developing foundational skills relevant to future uniformed-service opportunities."
        }
    ],

    "Arts, Design & Architecture": [
        {
            "exam": "Design and creative aptitude competitions",
            "focus": "Creative thinking, visual reasoning and problem-solving",
            "purpose": "Useful for developing creative aptitude and exploring design-related education."
        }
    ],

    "Agriculture & Environment": [
        {
            "exam": "Science and agriculture-related competitions",
            "focus": "Biology, environmental science, agriculture and scientific reasoning",
            "purpose": "Useful for strengthening knowledge related to agriculture and environmental studies."
        }
    ],

    "Sports & Fitness": [
        {
            "exam": "Sports scholarship and talent-selection opportunities",
            "focus": "Sports performance, fitness and academic eligibility",
            "purpose": "Useful for students who want to combine education with competitive sports."
        }
    ],

    "Vocational & Skill-Based": [
        {
            "exam": "Skill competitions and vocational selection tests",
            "focus": "Practical skills, technical knowledge and problem-solving",
            "purpose": "Useful for exploring skill-based education and vocational career pathways."
        }
    ],

    "ITI & Skilled Trades": [
        {
            "exam": "ITI entrance and trade-selection opportunities",
            "focus": "Technical aptitude and trade-specific preparation",
            "purpose": "Useful for students considering ITI and skilled-trade education."
        }
    ],

    "Diploma & Polytechnic": [
        {
            "exam": "Polytechnic entrance examinations",
            "focus": "Mathematics, science and technical aptitude",
            "purpose": "Useful for students considering diploma-level technical education."
        }
    ],

    "Aviation": [
        {
            "exam": "Aviation aptitude and career-selection opportunities",
            "focus": "Mathematics, science, communication and aptitude",
            "purpose": "Useful for exploring aviation-related education and career routes."
        }
    ],

    "Not Sure": [
        {
            "exam": "Scholarship and aptitude examinations",
            "focus": "Reasoning, mathematics, science and general aptitude",
            "purpose": "Useful for exploring strengths before choosing a specific academic or career direction."
        }
    ]
}


def recommend_after10th_exams(recommendations):

    if not recommendations:
        return []

    exams = []

    seen = set()

    for recommendation in recommendations[:5]:

        pathway = recommendation["pathway"]

        for exam in AFTER_10TH_EXAM_GUIDANCE.get(pathway, []):

            if exam["exam"] not in seen:

                exams.append(
                    {
                        "pathway": pathway,
                        "icon": recommendation["icon"],
                        "exam": exam["exam"],
                        "focus": exam["focus"],
                        "purpose": exam["purpose"]
                    }
                )

                seen.add(exam["exam"])

    return exams[:8]

def generate_after10th_next_steps(recommendations):

    if not recommendations:
        return []

    next_steps = []

    for index, recommendation in enumerate(
        recommendations[:5],
        start=1
    ):

        next_steps.append(
            {
                "number": index,
                "icon": recommendation["icon"],
                "title": recommendation["pathway"],
                "focus": recommendation["description"],
                "action": recommendation["next_step"]
            }
        )

    return next_steps

def generate_after10th_career_roadmap(recommendations):

    if not recommendations:
        return []

    roadmap = []

    for index, recommendation in enumerate(
        recommendations[:5],
        start=1
    ):

        pathway = recommendation["pathway"]

        roadmap.append(
            {
                "step": index,
                "icon": recommendation["icon"],
                "title": pathway,
                "description": recommendation["description"],
                "action": recommendation["next_step"],
                "careers": recommendation["careers"]
            }
        )

    return roadmap

# ==========================================
# AFTER 10TH SKILL DEVELOPMENT GUIDANCE
# ==========================================

AFTER_10TH_SKILL_GUIDANCE = {

    "Science & Mathematics": {
        "technical_skills": [
            "Mathematics fundamentals",
            "Scientific problem-solving",
            "Basic programming",
            "Data interpretation"
        ],
        "soft_skills": [
            "Logical thinking",
            "Analytical thinking",
            "Time management",
            "Problem-solving"
        ],
        "learning_areas": [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Programming fundamentals"
        ],
        "activity": "Solve mathematics and science problems regularly and build a small beginner programming project."
    },

    "Computer & Technology": {
        "technical_skills": [
            "Computer fundamentals",
            "Programming basics",
            "Problem-solving",
            "Digital literacy"
        ],
        "soft_skills": [
            "Logical thinking",
            "Creativity",
            "Communication",
            "Continuous learning"
        ],
        "learning_areas": [
            "Python or another beginner programming language",
            "Web development basics",
            "Artificial intelligence fundamentals",
            "Cybersecurity awareness"
        ],
        "activity": "Create a small beginner project such as a calculator, quiz application or simple webpage."
    },

    "Commerce & Business": {
        "technical_skills": [
            "Basic accounting",
            "Financial literacy",
            "Spreadsheet skills",
            "Business fundamentals"
        ],
        "soft_skills": [
            "Communication",
            "Decision-making",
            "Leadership",
            "Numerical reasoning"
        ],
        "learning_areas": [
            "Accounting",
            "Economics",
            "Business studies",
            "Entrepreneurship"
        ],
        "activity": "Create a simple monthly budget or design a small business idea and calculate its basic costs."
    },

    "Humanities & Social Sciences": {
        "technical_skills": [
            "Research skills",
            "Writing",
            "Information analysis",
            "Basic presentation skills"
        ],
        "soft_skills": [
            "Communication",
            "Critical thinking",
            "Empathy",
            "Public speaking"
        ],
        "learning_areas": [
            "History",
            "Political science",
            "Psychology",
            "Languages"
        ],
        "activity": "Choose a social topic, research it using reliable sources and prepare a short presentation."
    },

    "Engineering & Technical": {
        "technical_skills": [
            "Mathematics",
            "Basic electronics",
            "Technical problem-solving",
            "Computer fundamentals"
        ],
        "soft_skills": [
            "Analytical thinking",
            "Teamwork",
            "Time management",
            "Problem-solving"
        ],
        "learning_areas": [
            "Mathematics",
            "Physics",
            "Electronics",
            "Programming"
        ],
        "activity": "Build a simple technical or electronics project and document how it works."
    },

    "Medicine & Healthcare": {
        "technical_skills": [
            "Biology fundamentals",
            "Scientific observation",
            "Basic research",
            "Health awareness"
        ],
        "soft_skills": [
            "Empathy",
            "Communication",
            "Attention to detail",
            "Discipline"
        ],
        "learning_areas": [
            "Biology",
            "Chemistry",
            "Human health",
            "Scientific reasoning"
        ],
        "activity": "Study a basic human-biology topic and create a simple visual explanation or presentation."
    },

    "Defence & Armed Forces": {
        "technical_skills": [
            "Mathematics",
            "General knowledge",
            "Reasoning",
            "Basic computer skills"
        ],
        "soft_skills": [
            "Discipline",
            "Leadership",
            "Teamwork",
            "Communication"
        ],
        "learning_areas": [
            "Mathematics",
            "General awareness",
            "Reasoning",
            "Physical fitness"
        ],
        "activity": "Create a weekly study and fitness routine while developing general knowledge and reasoning skills."
    },

    "Police & Uniformed Services": {
        "technical_skills": [
            "General knowledge",
            "Reasoning",
            "Basic computer skills",
            "Communication"
        ],
        "soft_skills": [
            "Discipline",
            "Leadership",
            "Teamwork",
            "Decision-making"
        ],
        "learning_areas": [
            "General awareness",
            "Reasoning",
            "Communication",
            "Physical fitness"
        ],
        "activity": "Build a regular fitness routine and practice reasoning and general-awareness questions."
    },

    "Arts, Design & Architecture": {
        "technical_skills": [
            "Drawing fundamentals",
            "Visual communication",
            "Design basics",
            "Digital creativity"
        ],
        "soft_skills": [
            "Creativity",
            "Communication",
            "Observation",
            "Presentation"
        ],
        "learning_areas": [
            "Drawing",
            "Design principles",
            "Architecture basics",
            "Digital design"
        ],
        "activity": "Create a small design portfolio containing sketches, posters or digital designs."
    },

    "Agriculture & Environment": {
        "technical_skills": [
            "Biology fundamentals",
            "Environmental awareness",
            "Data observation",
            "Basic research"
        ],
        "soft_skills": [
            "Observation",
            "Problem-solving",
            "Teamwork",
            "Responsibility"
        ],
        "learning_areas": [
            "Biology",
            "Agriculture",
            "Environmental science",
            "Sustainability"
        ],
        "activity": "Start a small plant-growth or environmental observation project and record your findings."
    },

    "Sports & Fitness": {
        "technical_skills": [
            "Sports fundamentals",
            "Fitness training",
            "Performance tracking",
            "Basic nutrition awareness"
        ],
        "soft_skills": [
            "Discipline",
            "Teamwork",
            "Leadership",
            "Goal setting"
        ],
        "learning_areas": [
            "Physical education",
            "Fitness",
            "Sports science",
            "Nutrition basics"
        ],
        "activity": "Choose one sport or fitness activity and track your progress with weekly goals."
    },

    "Vocational & Skill-Based": {
        "technical_skills": [
            "Practical problem-solving",
            "Tool handling",
            "Digital literacy",
            "Workplace basics"
        ],
        "soft_skills": [
            "Discipline",
            "Communication",
            "Teamwork",
            "Reliability"
        ],
        "learning_areas": [
            "Vocational skills",
            "Digital tools",
            "Workplace safety",
            "Practical training"
        ],
        "activity": "Choose one practical skill and complete a beginner hands-on project."
    },

    "ITI & Skilled Trades": {
        "technical_skills": [
            "Basic tool usage",
            "Technical drawing",
            "Safety practices",
            "Practical problem-solving"
        ],
        "soft_skills": [
            "Discipline",
            "Attention to detail",
            "Teamwork",
            "Reliability"
        ],
        "learning_areas": [
            "Electrical basics",
            "Mechanical basics",
            "Workshop safety",
            "Trade fundamentals"
        ],
        "activity": "Explore one ITI trade and complete a safe beginner practical activity related to it."
    },

    "Diploma & Polytechnic": {
        "technical_skills": [
            "Mathematics",
            "Technical drawing",
            "Computer fundamentals",
            "Practical problem-solving"
        ],
        "soft_skills": [
            "Analytical thinking",
            "Time management",
            "Teamwork",
            "Communication"
        ],
        "learning_areas": [
            "Mathematics",
            "Engineering fundamentals",
            "Computer applications",
            "Technical drawing"
        ],
        "activity": "Explore diploma specializations and build a small technical project related to one area."
    },

    "Aviation": {
        "technical_skills": [
            "Mathematics",
            "Science fundamentals",
            "Computer skills",
            "Communication"
        ],
        "soft_skills": [
            "Discipline",
            "Attention to detail",
            "Teamwork",
            "Responsibility"
        ],
        "learning_areas": [
            "Physics",
            "Mathematics",
            "Aviation basics",
            "English communication"
        ],
        "activity": "Research different aviation careers and prepare a simple comparison of the skills each role requires."
    },

    "Not Sure": {
        "technical_skills": [
            "Digital literacy",
            "Basic problem-solving",
            "Research skills",
            "Communication"
        ],
        "soft_skills": [
            "Self-awareness",
            "Curiosity",
            "Decision-making",
            "Communication"
        ],
        "learning_areas": [
            "Mathematics and science",
            "Technology",
            "Business",
            "Humanities and creative fields"
        ],
        "activity": "Try small activities from different domains and note which subjects and tasks you enjoy most."
    }
}


def generate_after10th_skill_guidance(recommendations):

    if not recommendations:
        return []

    guidance = []

    for recommendation in recommendations[:5]:

        pathway = recommendation["pathway"]

        if pathway in AFTER_10TH_SKILL_GUIDANCE:

            information = AFTER_10TH_SKILL_GUIDANCE[pathway]

            guidance.append(
                {
                    "pathway": pathway,
                    "icon": recommendation["icon"],
                    "technical_skills": information["technical_skills"],
                    "soft_skills": information["soft_skills"],
                    "learning_areas": information["learning_areas"],
                    "activity": information["activity"]
                }
            )

    return guidance

# ==========================================
# AFTER 10TH FREE LEARNING RESOURCES
# ==========================================

AFTER_10TH_LEARNING_RESOURCES = {

    "Science & Mathematics": [
        {
            "type": "Video Lectures",
            "icon": "📺",
            "resource": "Free mathematics and science video lessons",
            "focus": "Mathematics, Physics and Chemistry fundamentals",
            "purpose": "Strengthen Class 11 and 12 academic foundations."
        },
        {
            "type": "Practice",
            "icon": "📝",
            "resource": "Free practice questions and previous-year style problems",
            "focus": "Mathematics, Physics and logical problem-solving",
            "purpose": "Improve problem-solving speed and accuracy."
        },
        {
            "type": "Programming",
            "icon": "💻",
            "resource": "Free beginner programming courses",
            "focus": "Python, programming logic and computational thinking",
            "purpose": "Build an early technology foundation."
        }
    ],

    "Computer & Technology": [
        {
            "type": "Coding",
            "icon": "💻",
            "resource": "Free beginner coding courses",
            "focus": "Python, programming logic and problem-solving",
            "purpose": "Build practical programming skills."
        },
        {
            "type": "Web Development",
            "icon": "🌐",
            "resource": "Free HTML, CSS and JavaScript learning resources",
            "focus": "Web development fundamentals",
            "purpose": "Create simple websites and understand how the web works."
        },
        {
            "type": "Artificial Intelligence",
            "icon": "🤖",
            "resource": "Free introductory AI and machine-learning lessons",
            "focus": "AI concepts, data and machine-learning basics",
            "purpose": "Explore artificial intelligence before advanced study."
        }
    ],

    "Commerce & Business": [
        {
            "type": "Business Studies",
            "icon": "📚",
            "resource": "Free business and entrepreneurship lessons",
            "focus": "Business concepts and entrepreneurship",
            "purpose": "Develop an early understanding of business."
        },
        {
            "type": "Finance",
            "icon": "💰",
            "resource": "Free financial-literacy resources",
            "focus": "Budgeting, saving and basic finance",
            "purpose": "Build practical financial awareness."
        }
    ],

    "Humanities & Social Sciences": [
        {
            "type": "Social Sciences",
            "icon": "🌍",
            "resource": "Free history, civics and social-science lessons",
            "focus": "Society, history and public affairs",
            "purpose": "Build knowledge and analytical understanding."
        },
        {
            "type": "Communication",
            "icon": "🗣️",
            "resource": "Free writing and communication resources",
            "focus": "Writing, vocabulary and communication",
            "purpose": "Strengthen academic and professional communication."
        }
    ],

    "Engineering & Technical": [
        {
            "type": "Mathematics",
            "icon": "📐",
            "resource": "Free mathematics and problem-solving lessons",
            "focus": "Mathematics and technical reasoning",
            "purpose": "Build the foundation for technical studies."
        },
        {
            "type": "Technical Learning",
            "icon": "⚙️",
            "resource": "Free introductory engineering and electronics resources",
            "focus": "Engineering concepts, electronics and technical systems",
            "purpose": "Explore technical fields through beginner-level learning."
        }
    ],

    "Medicine & Healthcare": [
        {
            "type": "Biology",
            "icon": "🧬",
            "resource": "Free biology and human-body lessons",
            "focus": "Biology, human health and scientific concepts",
            "purpose": "Strengthen the foundation for healthcare-related studies."
        },
        {
            "type": "Science Practice",
            "icon": "🔬",
            "resource": "Free science practice questions",
            "focus": "Biology, Chemistry and scientific reasoning",
            "purpose": "Improve scientific understanding and problem-solving."
        }
    ],

    "Defence & Armed Forces": [
        {
            "type": "General Knowledge",
            "icon": "🌐",
            "resource": "Free general-awareness and current-affairs learning resources",
            "focus": "General knowledge, geography, history and current affairs",
            "purpose": "Develop a broad knowledge foundation."
        },
        {
            "type": "Reasoning",
            "icon": "🧠",
            "resource": "Free reasoning and aptitude practice",
            "focus": "Logical reasoning and quantitative aptitude",
            "purpose": "Build early aptitude skills."
        }
    ],

    "Police & Uniformed Services": [
        {
            "type": "General Awareness",
            "icon": "🌍",
            "resource": "Free general-knowledge learning resources",
            "focus": "General awareness and public affairs",
            "purpose": "Build foundational knowledge."
        },
        {
            "type": "Fitness",
            "icon": "🏃",
            "resource": "Free fitness and physical-training resources",
            "focus": "Fitness, endurance and healthy habits",
            "purpose": "Develop a consistent physical-activity routine."
        }
    ],

    "Arts, Design & Architecture": [
        {
            "type": "Design",
            "icon": "🎨",
            "resource": "Free drawing and design tutorials",
            "focus": "Drawing, visual communication and design fundamentals",
            "purpose": "Develop creative and visual skills."
        },
        {
            "type": "Digital Design",
            "icon": "🖥️",
            "resource": "Free digital-design learning resources",
            "focus": "Digital graphics and creative tools",
            "purpose": "Build an early digital-design portfolio."
        }
    ],

    "Agriculture & Environment": [
        {
            "type": "Agriculture",
            "icon": "🌱",
            "resource": "Free agriculture and environmental-science lessons",
            "focus": "Agriculture, biology and environmental systems",
            "purpose": "Build knowledge related to agriculture and sustainability."
        },
        {
            "type": "Environment",
            "icon": "🌍",
            "resource": "Free environmental-learning resources",
            "focus": "Climate, biodiversity and sustainability",
            "purpose": "Understand environmental challenges and solutions."
        }
    ],

    "Sports & Fitness": [
        {
            "type": "Fitness",
            "icon": "🏃",
            "resource": "Free fitness and training resources",
            "focus": "Fitness, endurance and strength",
            "purpose": "Build healthy and consistent training habits."
        },
        {
            "type": "Sports Learning",
            "icon": "🏅",
            "resource": "Free sports-skill and sports-science resources",
            "focus": "Sports techniques, training and performance",
            "purpose": "Improve sporting knowledge and performance."
        }
    ],

    "Vocational & Skill-Based": [
        {
            "type": "Practical Skills",
            "icon": "🛠️",
            "resource": "Free vocational and practical-skill tutorials",
            "focus": "Hands-on skills and workplace practices",
            "purpose": "Develop practical abilities through beginner projects."
        },
        {
            "type": "Digital Skills",
            "icon": "💻",
            "resource": "Free digital-literacy courses",
            "focus": "Computer basics and digital tools",
            "purpose": "Build essential workplace technology skills."
        }
    ],

    "ITI & Skilled Trades": [
        {
            "type": "Trade Skills",
            "icon": "🔧",
            "resource": "Free introductory technical-trade tutorials",
            "focus": "Electrical, mechanical and workshop fundamentals",
            "purpose": "Explore skilled trades before choosing a specialization."
        },
        {
            "type": "Safety",
            "icon": "🦺",
            "resource": "Free workplace-safety learning resources",
            "focus": "Tools, safety and responsible work practices",
            "purpose": "Develop safe working habits."
        }
    ],

    "Diploma & Polytechnic": [
        {
            "type": "Technical Mathematics",
            "icon": "📐",
            "resource": "Free mathematics and technical-learning resources",
            "focus": "Mathematics and engineering fundamentals",
            "purpose": "Build a foundation for diploma-level technical studies."
        },
        {
            "type": "Engineering Basics",
            "icon": "⚙️",
            "resource": "Free introductory engineering tutorials",
            "focus": "Engineering, electronics and technical systems",
            "purpose": "Explore technical specializations."
        }
    ],

    "Aviation": [
        {
            "type": "Aviation Basics",
            "icon": "✈️",
            "resource": "Free introductory aviation-learning resources",
            "focus": "Aircraft, aviation systems and airport operations",
            "purpose": "Explore different aviation career areas."
        },
        {
            "type": "Communication",
            "icon": "🗣️",
            "resource": "Free English and communication resources",
            "focus": "English communication and professional interaction",
            "purpose": "Develop communication skills useful in aviation."
        }
    ],

    "Not Sure": [
        {
            "type": "Career Exploration",
            "icon": "🧭",
            "resource": "Free career-exploration and aptitude resources",
            "focus": "Interests, strengths and different career domains",
            "purpose": "Explore options before choosing a specific pathway."
        },
        {
            "type": "General Learning",
            "icon": "📚",
            "resource": "Free lessons across science, technology, business and humanities",
            "focus": "Different academic and practical subjects",
            "purpose": "Try different areas and identify what you enjoy."
        }
    ]
}


def recommend_after10th_learning_resources(recommendations):

    if not recommendations:
        return []

    resources = []

    for recommendation in recommendations[:5]:

        pathway = recommendation["pathway"]

        for resource in AFTER_10TH_LEARNING_RESOURCES.get(pathway, []):

            resource_name = resource["resource"].lower()

            # Official free learning-resource links
            if "mathematics and science" in resource_name:
                resource_url = "https://india.khanacademy.org/"

            elif "practice questions" in resource_name:
                resource_url = "https://india.khanacademy.org/"

            elif "programming" in resource_name or "coding" in resource_name:
                resource_url = "https://www.khanacademy.org/computing"

            elif "html, css and javascript" in resource_name:
                resource_url = "https://www.khanacademy.org/computing"

            elif "artificial intelligence" in resource_name or "machine-learning" in resource_name:
                resource_url = "https://www.khanacademy.org/computing"

            elif "english" in resource_name or "communication" in resource_name:
                resource_url = "https://india.khanacademy.org/"

            elif "career-exploration" in resource_name or "aptitude" in resource_name:
                resource_url = "https://india.khanacademy.org/"

            else:
                resource_url = "https://india.khanacademy.org/"

            resources.append(
                {
                    "pathway": pathway,
                    "icon": recommendation["icon"],
                    "type": resource["type"],
                    "resource": resource["resource"],
                    "focus": resource["focus"],
                    "purpose": resource["purpose"],
                    "url": resource_url
                }
            )

    return resources[:12]
