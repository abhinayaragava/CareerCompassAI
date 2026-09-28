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


CAREER_GUIDANCE.update({
    "Army Technical Officer": {
        "education_path": "Build a strong foundation in mathematics, physics and computer science, then pursue a relevant technical undergraduate pathway such as engineering or another suitable technical degree.",
        "beginner_action": "Strengthen mathematics and physics while exploring electronics, computing, problem solving and structured technical activities.",
        "opportunities": [
            "Technical projects",
            "Robotics and electronics activities",
            "Programming practice",
            "STEM competitions"
        ]
    },

    "Army Engineering Officer": {
        "education_path": "Pursue an engineering-oriented undergraduate pathway with strong mathematics and physics preparation.",
        "beginner_action": "Build fundamentals in mathematics, physics and engineering problem solving through practical projects.",
        "opportunities": [
            "Engineering projects",
            "Robotics activities",
            "STEM competitions",
            "Technical clubs"
        ]
    },

    "Army Signals / Communications Officer": {
        "education_path": "Develop strong foundations in mathematics, physics and computer science and consider a relevant technology or engineering degree.",
        "beginner_action": "Explore programming, networking, communication systems and basic electronics.",
        "opportunities": [
            "Programming projects",
            "Networking practice",
            "Electronics projects",
            "Technology clubs"
        ]
    },

    "Army Logistics Officer": {
        "education_path": "Build knowledge in mathematics, economics and business-related subjects and consider a suitable undergraduate pathway in management, commerce or a related field.",
        "beginner_action": "Practice planning, organization, budgeting and problem solving through small projects.",
        "opportunities": [
            "Business projects",
            "Event planning",
            "Budgeting activities",
            "Leadership activities"
        ]
    },

    "Naval Engineering Officer": {
        "education_path": "Develop strong mathematics and physics foundations and pursue a relevant engineering or technical undergraduate pathway.",
        "beginner_action": "Explore mechanical systems, engineering concepts, physics and practical problem solving.",
        "opportunities": [
            "Engineering projects",
            "Robotics activities",
            "Physics projects",
            "Technical clubs"
        ]
    },

    "Naval Electrical / Electronics Officer": {
        "education_path": "Build strong foundations in mathematics, physics and computer science and consider an electrical, electronics or related engineering pathway.",
        "beginner_action": "Explore circuits, electronics, programming and basic communication systems.",
        "opportunities": [
            "Electronics projects",
            "Arduino or microcontroller projects",
            "Programming practice",
            "STEM clubs"
        ]
    },

    "Naval Technical Officer": {
        "education_path": "Develop mathematics, physics and computer science skills and pursue a suitable technical or engineering undergraduate pathway.",
        "beginner_action": "Work on technical problem solving through programming, electronics and engineering activities.",
        "opportunities": [
            "Technical projects",
            "Robotics",
            "Programming",
            "Engineering competitions"
        ]
    },

    "Naval Aviation Officer": {
        "education_path": "Build strong mathematics and physics foundations and explore aviation-related education and technical pathways.",
        "beginner_action": "Strengthen physics, mathematics, spatial awareness and disciplined decision making.",
        "opportunities": [
            "Aviation awareness activities",
            "Physics projects",
            "STEM competitions",
            "Fitness activities"
        ]
    },

    "Air Force Flying Officer": {
        "education_path": "Develop strong mathematics and physics foundations and pursue an appropriate undergraduate pathway while maintaining physical fitness.",
        "beginner_action": "Strengthen mathematics, physics, communication, decision making and physical fitness.",
        "opportunities": [
            "Sports and fitness",
            "STEM activities",
            "Leadership activities",
            "Aviation awareness"
        ]
    },

    "Air Force Technical Officer": {
        "education_path": "Build strong mathematics, physics and computer science foundations and pursue a relevant technical or engineering degree.",
        "beginner_action": "Explore engineering, programming, electronics and structured technical problem solving.",
        "opportunities": [
            "Engineering projects",
            "Programming",
            "Electronics activities",
            "STEM competitions"
        ]
    },

    "Air Force Ground Duty Technical Officer": {
        "education_path": "Develop mathematics, physics and computer science skills and pursue a suitable technical or engineering undergraduate pathway.",
        "beginner_action": "Practice programming, electronics, mathematics and technical problem solving.",
        "opportunities": [
            "Programming projects",
            "Electronics projects",
            "Robotics",
            "Technical clubs"
        ]
    },

    "Air Force Ground Duty Non-Technical Officer": {
        "education_path": "Build strong communication, analytical and organizational abilities through an appropriate undergraduate pathway in areas such as humanities, commerce, management or related disciplines.",
        "beginner_action": "Develop communication, leadership, general awareness, organization and analytical skills.",
        "opportunities": [
            "Debates and public speaking",
            "Leadership activities",
            "Current-affairs learning",
            "Management projects"
        ]
    },

    "Coast Guard Officer": {
        "education_path": "Build strong mathematics and science foundations and explore an appropriate technical, maritime or undergraduate pathway.",
        "beginner_action": "Develop physical fitness, discipline, teamwork, mathematics and science skills.",
        "opportunities": [
            "Swimming and fitness",
            "Science projects",
            "Team activities",
            "Leadership activities"
        ]
    },

    "Defence Scientist": {
        "education_path": "Build strong foundations in mathematics, physics, chemistry and computer science and pursue a relevant science or engineering degree.",
        "beginner_action": "Develop scientific thinking through experiments, mathematics, programming and technical projects.",
        "opportunities": [
            "Science projects",
            "Research activities",
            "Programming",
            "STEM competitions"
        ]
    },

    "Defence Research & Technology Professional": {
        "education_path": "Develop strong mathematics, physics and computer science foundations and pursue a relevant science, engineering or technology pathway.",
        "beginner_action": "Explore research methods, programming, engineering concepts and experimental problem solving.",
        "opportunities": [
            "Research projects",
            "Engineering projects",
            "Programming",
            "Science competitions"
        ]
    },

    "Defence Cybersecurity Professional": {
        "education_path": "Build strong foundations in computer science and mathematics and pursue a relevant cybersecurity, computer science or technology pathway.",
        "beginner_action": "Learn programming, networking, cybersecurity fundamentals and logical problem solving in safe learning environments.",
        "opportunities": [
            "Programming projects",
            "Cybersecurity learning labs",
            "Networking practice",
            "Technology clubs"
        ]
    },

    "Defence Electronics / Communications Professional": {
        "education_path": "Build strong mathematics and physics foundations with computer science and pursue an electronics, communications or related engineering pathway.",
        "beginner_action": "Explore electronics, communication systems, programming and signal-related concepts.",
        "opportunities": [
            "Electronics projects",
            "Communication-system projects",
            "Programming",
            "STEM activities"
        ]
    },

    "Defence Logistics Professional": {
        "education_path": "Develop mathematics, economics and business knowledge and pursue a suitable undergraduate pathway in logistics, management, commerce or a related field.",
        "beginner_action": "Practice planning, organization, resource management, budgeting and analytical problem solving.",
        "opportunities": [
            "Logistics projects",
            "Business activities",
            "Event planning",
            "Leadership activities"
        ]
    },

    "Defence Medical Professional": {
        "education_path": "Build strong biology, chemistry and physics foundations and pursue an appropriate healthcare or medical undergraduate pathway.",
        "beginner_action": "Strengthen biology and chemistry while developing empathy, communication and disciplined study habits.",
        "opportunities": [
            "Biology projects",
            "Health-awareness activities",
            "Science competitions",
            "Community service activities"
        ]
    }
})

CAREER_GUIDANCE.update({

    "Full Stack Developer": {
        "education_path": "Consider B.Tech/B.E. Computer Science, BCA, B.Sc Computer Science or a related software development pathway.",
        "beginner_action": "Build a small full-stack website using a frontend, backend and database.",
        "opportunities": [
            "Web development projects",
            "Coding clubs",
            "Hackathons",
            "Portfolio websites"
        ]
    },

    "Mobile App Developer": {
        "education_path": "Consider Computer Science, Information Technology, BCA or a related software development degree.",
        "beginner_action": "Create a simple Android or cross-platform mobile application.",
        "opportunities": [
            "Mobile app projects",
            "Hackathons",
            "App development clubs",
            "Portfolio projects"
        ]
    },

    "Web Developer": {
        "education_path": "Consider Computer Science, Information Technology, BCA or a related technology pathway.",
        "beginner_action": "Build a responsive website using HTML, CSS and JavaScript.",
        "opportunities": [
            "Web projects",
            "Coding competitions",
            "Technology clubs",
            "Portfolio development"
        ]
    },

    "Data Analyst": {
        "education_path": "Consider B.Sc Data Science, B.Sc Computer Science, BCA, Economics, Statistics or a related data-focused pathway.",
        "beginner_action": "Analyze a small dataset using spreadsheets or Python and create simple charts.",
        "opportunities": [
            "Data analysis projects",
            "Statistics competitions",
            "Data clubs",
            "Portfolio dashboards"
        ]
    },

    "Business Intelligence Analyst": {
        "education_path": "Consider Computer Science, Data Science, Business Analytics, Economics or a related undergraduate pathway.",
        "beginner_action": "Create a simple dashboard from a public dataset and practice interpreting business metrics.",
        "opportunities": [
            "Analytics projects",
            "Business case competitions",
            "Data clubs",
            "Dashboard projects"
        ]
    },

    "Database Administrator": {
        "education_path": "Consider Computer Science, Information Technology, BCA or a related computing pathway.",
        "beginner_action": "Learn basic SQL and create a small database with tables, relationships and queries.",
        "opportunities": [
            "Database projects",
            "SQL practice",
            "Coding clubs",
            "Technology competitions"
        ]
    },

    "Network Engineer": {
        "education_path": "Consider Computer Science, Information Technology, Computer Engineering or a related networking pathway.",
        "beginner_action": "Learn networking fundamentals such as IP addresses, routing, switching and network security.",
        "opportunities": [
            "Networking labs",
            "Technology clubs",
            "Networking projects",
            "Technical competitions"
        ]
    },

    "Cybersecurity Engineer": {
        "education_path": "Consider B.Tech Cybersecurity, Computer Science, Information Technology or a related security pathway.",
        "beginner_action": "Learn cybersecurity fundamentals and practice in safe, authorized lab environments.",
        "opportunities": [
            "Cybersecurity clubs",
            "Capture-the-flag learning events",
            "Security projects",
            "Technology competitions"
        ]
    },

    "Ethical Hacker / Penetration Tester": {
        "education_path": "Consider Cybersecurity, Computer Science, Information Technology or a related security-focused degree.",
        "beginner_action": "Learn networking, operating systems and defensive security concepts before practicing ethical security testing in authorized labs.",
        "opportunities": [
            "Cybersecurity labs",
            "Capture-the-flag events",
            "Security clubs",
            "Defensive security projects"
        ]
    },

    "Cloud Engineer": {
        "education_path": "Consider Computer Science, Information Technology, Cloud Computing or a related technology degree.",
        "beginner_action": "Learn Linux, networking and basic cloud concepts and deploy a small practice application.",
        "opportunities": [
            "Cloud projects",
            "Technology clubs",
            "Cloud learning labs",
            "Hackathons"
        ]
    },

    "DevOps Engineer": {
        "education_path": "Consider Computer Science, Information Technology or a related software and infrastructure pathway.",
        "beginner_action": "Learn Linux, Git, basic automation and software deployment concepts.",
        "opportunities": [
            "Automation projects",
            "Cloud labs",
            "Coding clubs",
            "Technology projects"
        ]
    },

    "Blockchain Developer": {
        "education_path": "Consider Computer Science, Information Technology, Software Engineering or a related computing pathway.",
        "beginner_action": "Learn programming fundamentals and explore blockchain concepts through a small educational project.",
        "opportunities": [
            "Programming projects",
            "Blockchain learning communities",
            "Hackathons",
            "Technology clubs"
        ]
    },

    "Robotics Engineer": {
        "education_path": "Consider Robotics, Mechatronics, Electronics, Computer Science or a related engineering pathway.",
        "beginner_action": "Build a simple sensor-based robotics project using a beginner-friendly development board.",
        "opportunities": [
            "Robotics competitions",
            "Maker clubs",
            "Science exhibitions",
            "Engineering projects"
        ]
    },

    "IoT Engineer": {
        "education_path": "Consider Electronics, Computer Science, Electrical Engineering, IoT or a related technology pathway.",
        "beginner_action": "Build a simple sensor-based IoT project that collects and displays data.",
        "opportunities": [
            "IoT projects",
            "Electronics clubs",
            "Maker events",
            "Technology competitions"
        ]
    },

    "Game Developer": {
        "education_path": "Consider Computer Science, Software Engineering, Game Development or a related technology pathway.",
        "beginner_action": "Create a small 2D game and learn basic programming, game logic and digital design.",
        "opportunities": [
            "Game development projects",
            "Game jams",
            "Coding clubs",
            "Digital creation communities"
        ]
    },

    "UI / UX Technology Specialist": {
        "education_path": "Consider Computer Science, Information Technology, Interaction Design, UI/UX or a related interdisciplinary pathway.",
        "beginner_action": "Design a simple app or website interface and create a small usability-focused prototype.",
        "opportunities": [
            "Design projects",
            "UI/UX clubs",
            "Design competitions",
            "Portfolio projects"
        ]
    },

    "Software Tester / QA Engineer": {
        "education_path": "Consider Computer Science, Information Technology, Software Engineering or a related computing degree.",
        "beginner_action": "Learn software testing concepts and create test cases for a small application.",
        "opportunities": [
            "Software testing projects",
            "Coding clubs",
            "Technology competitions",
            "Quality-assurance practice"
        ]
    },

    "Systems Analyst": {
        "education_path": "Consider Computer Science, Information Technology, Business Information Systems or a related pathway.",
        "beginner_action": "Study how software systems solve real problems and document requirements for a small project.",
        "opportunities": [
            "Technology projects",
            "Business case competitions",
            "System design exercises",
            "Coding clubs"
        ]
    },

    "IT Support / Systems Administrator": {
        "education_path": "Consider Computer Science, Information Technology, Computer Applications or a related computing pathway.",
        "beginner_action": "Learn computer hardware, operating systems, networking and basic troubleshooting.",
        "opportunities": [
            "Computer labs",
            "Technology clubs",
            "System administration projects",
            "Technical support activities"
        ]
    },

    "Technical Product Manager": {
        "education_path": "Consider Computer Science, Information Technology, Engineering, Business or an interdisciplinary technology pathway.",
        "beginner_action": "Choose a real problem and create a simple product idea with user needs, features and a basic development plan.",
        "opportunities": [
            "Innovation competitions",
            "Startup projects",
            "Hackathons",
            "Technology entrepreneurship activities"
        ]
    }

})

CAREER_GUIDANCE.update({

    "Software Developer": {
        "education_path": "Consider B.Tech/B.E. Computer Science, Information Technology, BCA or B.Sc Computer Science.",
        "beginner_action": "Learn one programming language and build a small practical application.",
        "opportunities": [
            "Coding competitions",
            "Hackathons",
            "Programming clubs",
            "Portfolio projects"
        ]
    },

    "AI / Machine Learning Engineer": {
        "education_path": "Consider B.Tech Artificial Intelligence & Machine Learning, Computer Science, Data Science or a related computing pathway.",
        "beginner_action": "Strengthen Mathematics and Python and build a beginner machine-learning project using a small dataset.",
        "opportunities": [
            "AI projects",
            "Machine-learning competitions",
            "AI clubs",
            "Research projects"
        ]
    },

    "Data Scientist": {
        "education_path": "Consider Data Science, Computer Science, Statistics, Mathematics, Economics or a related data-focused degree.",
        "beginner_action": "Learn Python, statistics and data visualization and analyze a small real-world dataset.",
        "opportunities": [
            "Data projects",
            "Analytics competitions",
            "Research activities",
            "Data-science clubs"
        ]
    },

    "Cybersecurity Analyst": {
        "education_path": "Consider B.Tech Cybersecurity, Computer Science, Information Technology or a related security pathway.",
        "beginner_action": "Learn networking, operating systems and basic cybersecurity concepts through authorized practice environments.",
        "opportunities": [
            "Cybersecurity clubs",
            "Capture-the-flag learning events",
            "Security projects",
            "Technology competitions"
        ]
    },

    "Cloud / DevOps Engineer": {
        "education_path": "Consider Computer Science, Information Technology, Cloud Computing or a related technology degree.",
        "beginner_action": "Learn Linux, networking, Git and basic cloud deployment concepts.",
        "opportunities": [
            "Cloud projects",
            "DevOps practice labs",
            "Technology clubs",
            "Hackathons"
        ]
    }

})

CAREER_GUIDANCE.update({

    "Mechanical Engineer": {
        "education_path": "Consider B.Tech/B.E. Mechanical Engineering or related mechanical and manufacturing programs.",
        "beginner_action": "Strengthen Mathematics and Physics and explore basic mechanical design, CAD and engineering projects.",
        "opportunities": [
            "Robotics and engineering clubs",
            "CAD projects",
            "Engineering competitions",
            "Hands-on technical projects"
        ]
    },

    "Civil Engineer": {
        "education_path": "Consider B.Tech/B.E. Civil Engineering or related construction and infrastructure programs.",
        "beginner_action": "Strengthen Mathematics and Physics and explore basic structural design, surveying and construction concepts.",
        "opportunities": [
            "Civil engineering projects",
            "Infrastructure competitions",
            "CAD and design activities",
            "Technical clubs"
        ]
    },

    "Electrical Engineer": {
        "education_path": "Consider B.Tech/B.E. Electrical Engineering or related electrical and power engineering programs.",
        "beginner_action": "Strengthen Mathematics and Physics and learn basic electrical circuits, electronics and power-system concepts.",
        "opportunities": [
            "Electronics projects",
            "Engineering competitions",
            "Technical clubs",
            "Hands-on circuit projects"
        ]
    },

    "Electronics Engineer": {
        "education_path": "Consider B.Tech/B.E. Electronics and Communication Engineering or related electronics programs.",
        "beginner_action": "Learn basic circuits, digital electronics, microcontrollers and communication concepts.",
        "opportunities": [
            "Electronics projects",
            "Robotics clubs",
            "Embedded-system projects",
            "Engineering competitions"
        ]
    },

    "Computer Science Engineer": {
        "education_path": "Consider B.Tech/B.E. Computer Science Engineering, Information Technology or related computing programs.",
        "beginner_action": "Learn programming, problem solving and fundamental computer science concepts and build small software projects.",
        "opportunities": [
            "Coding competitions",
            "Hackathons",
            "Programming clubs",
            "Software projects"
        ]
    },

    "Chemical Engineer": {
        "education_path": "Consider B.Tech/B.E. Chemical Engineering or related chemical and process engineering programs.",
        "beginner_action": "Strengthen Mathematics, Physics and Chemistry and explore basic chemical processes and laboratory concepts.",
        "opportunities": [
            "Science projects",
            "Chemistry competitions",
            "Laboratory activities",
            "Engineering clubs"
        ]
    },

    "Aerospace Engineer": {
        "education_path": "Consider B.Tech/B.E. Aerospace Engineering, Aeronautical Engineering or Mechanical Engineering.",
        "beginner_action": "Strengthen Mathematics and Physics and explore aircraft, aerodynamics and aerospace systems through beginner projects.",
        "opportunities": [
            "Aerospace projects",
            "Model aircraft activities",
            "Engineering competitions",
            "Science and technology clubs"
        ]
    },

    "Automobile Engineer": {
        "education_path": "Consider B.Tech/B.E. Automobile Engineering, Mechanical Engineering or related automotive programs.",
        "beginner_action": "Learn basic vehicle systems, mechanics and engineering principles and explore simple automotive projects.",
        "opportunities": [
            "Automotive projects",
            "Engineering clubs",
            "Vehicle design activities",
            "Technical competitions"
        ]
    },

    "Biomedical Engineer": {
        "education_path": "Consider B.Tech/B.E. Biomedical Engineering or related engineering and healthcare technology programs.",
        "beginner_action": "Build a foundation in Mathematics, Physics and Biology and explore how engineering is applied to healthcare.",
        "opportunities": [
            "Healthcare technology projects",
            "Science competitions",
            "Biomedical innovation activities",
            "Research projects"
        ]
    },

    "Environmental Engineer": {
        "education_path": "Consider B.Tech/B.E. Environmental Engineering, Civil Engineering or related environmental programs.",
        "beginner_action": "Learn about environmental systems, pollution control, water management and sustainable engineering.",
        "opportunities": [
            "Environmental projects",
            "Sustainability activities",
            "Science competitions",
            "Environmental clubs"
        ]
    },

    "Industrial Engineer": {
        "education_path": "Consider B.Tech/B.E. Industrial Engineering, Production Engineering or related engineering programs.",
        "beginner_action": "Strengthen Mathematics and analytical thinking and explore process improvement, operations and productivity concepts.",
        "opportunities": [
            "Process-improvement projects",
            "Operations competitions",
            "Engineering clubs",
            "Business and technology projects"
        ]
    },

    "Mechatronics Engineer": {
        "education_path": "Consider B.Tech/B.E. Mechatronics Engineering, Robotics or related interdisciplinary engineering programs.",
        "beginner_action": "Learn the basics of mechanical systems, electronics, programming and automation.",
        "opportunities": [
            "Robotics projects",
            "Automation competitions",
            "Engineering clubs",
            "Embedded-system projects"
        ]
    },

    "Manufacturing Engineer": {
        "education_path": "Consider B.Tech/B.E. Manufacturing Engineering, Mechanical Engineering, Production Engineering or related programs.",
        "beginner_action": "Explore manufacturing processes, CAD, materials and basic production-system concepts.",
        "opportunities": [
            "Manufacturing projects",
            "CAD activities",
            "Engineering competitions",
            "Industrial visits and workshops"
        ]
    },

    "Petroleum Engineer": {
        "education_path": "Consider B.Tech/B.E. Petroleum Engineering or related petroleum and energy engineering programs.",
        "beginner_action": "Strengthen Mathematics, Physics and Chemistry and learn basic concepts of energy resources and petroleum systems.",
        "opportunities": [
            "Energy-related projects",
            "Science competitions",
            "Engineering clubs",
            "Energy and sustainability activities"
        ]
    },

    "Mining Engineer": {
        "education_path": "Consider B.Tech/B.E. Mining Engineering or related mining and mineral engineering programs.",
        "beginner_action": "Strengthen Mathematics, Physics and Chemistry and explore mineral resources, mining systems and mine safety concepts.",
        "opportunities": [
            "Earth-science projects",
            "Engineering competitions",
            "Mining and geology activities",
            "Technical workshops"
        ]
    },

    "Metallurgical Engineer": {
        "education_path": "Consider B.Tech/B.E. Metallurgical Engineering, Materials Engineering or related materials programs.",
        "beginner_action": "Strengthen Chemistry and Physics and explore metals, materials, material properties and basic laboratory concepts.",
        "opportunities": [
            "Materials science projects",
            "Science competitions",
            "Laboratory activities",
            "Engineering clubs"
        ]
    },

    "Marine Engineer": {
        "education_path": "Consider B.Tech/B.E. Marine Engineering or related marine and mechanical engineering programs.",
        "beginner_action": "Strengthen Mathematics and Physics and explore marine propulsion, ship systems and basic maritime engineering.",
        "opportunities": [
            "Marine technology activities",
            "Engineering projects",
            "Technical workshops",
            "Science and engineering clubs"
        ]
    },

    "Agricultural Engineer": {
        "education_path": "Consider B.Tech/B.E. Agricultural Engineering or related agricultural technology and engineering programs.",
        "beginner_action": "Explore irrigation, farm machinery, agricultural technology, renewable energy and sustainable farming systems.",
        "opportunities": [
            "Agricultural technology projects",
            "Sustainability activities",
            "Innovation competitions",
            "Agriculture and engineering clubs"
        ]
    },

    "Instrumentation & Control Engineer": {
        "education_path": "Consider B.Tech/B.E. Instrumentation and Control Engineering, Electronics or related automation programs.",
        "beginner_action": "Learn basic sensors, measurement systems, electronics, programming and industrial automation concepts.",
        "opportunities": [
            "Automation projects",
            "Electronics competitions",
            "Robotics clubs",
            "Industrial technology projects"
        ]
    }

})

# ============================================================
# MEDICINE & HEALTHCARE — CAREER-SPECIFIC GUIDANCE
# ============================================================

CAREER_GUIDANCE.update({

    "Doctor": {
        "education_path": "Explore an undergraduate medical pathway such as MBBS and review the admission requirements applicable to your region.",
        "beginner_action": "Strengthen Biology, Chemistry and Physics while exploring basic anatomy, health science and scientific thinking.",
        "opportunities": [
            "Science projects",
            "Health-awareness activities",
            "Biology competitions",
            "First-aid awareness programs"
        ]
    },

    "Dentist": {
        "education_path": "Explore a BDS pathway and review the admission requirements applicable to your region.",
        "beginner_action": "Build a strong foundation in Biology and Chemistry and learn about oral health and dental science.",
        "opportunities": [
            "Health-awareness activities",
            "Biology projects",
            "Oral-health awareness programs",
            "Science competitions"
        ]
    },

    "Pharmacist": {
        "education_path": "Explore a pharmacy degree such as B.Pharm and review the admission requirements applicable to your region.",
        "beginner_action": "Strengthen Chemistry and Biology and learn basic concepts of medicines, drug safety and pharmaceutical science.",
        "opportunities": [
            "Chemistry projects",
            "Biology activities",
            "Pharmaceutical science exploration",
            "Science competitions"
        ]
    },

    "Physiotherapist": {
        "education_path": "Explore a Bachelor of Physiotherapy (BPT) pathway.",
        "beginner_action": "Study Biology and Physics while learning basic concepts of human anatomy, movement and physical rehabilitation.",
        "opportunities": [
            "Sports and fitness activities",
            "Biology projects",
            "Health-awareness activities",
            "Human anatomy exploration"
        ]
    },

    "Healthcare Professional": {
        "education_path": "Explore healthcare and allied-health undergraduate programs based on your interests and preferred area of patient care.",
        "beginner_action": "Develop Biology knowledge, communication skills, empathy and attention to detail.",
        "opportunities": [
            "Health-awareness activities",
            "Volunteer activities",
            "Science projects",
            "Patient-care awareness programs"
        ]
    },

    "Nurse": {
        "education_path": "Explore undergraduate nursing pathways such as B.Sc. Nursing and review applicable admission requirements.",
        "beginner_action": "Strengthen Biology and develop communication, empathy, teamwork and patient-care awareness.",
        "opportunities": [
            "First-aid awareness",
            "Health-awareness activities",
            "Biology projects",
            "Teamwork activities"
        ]
    },

    "Medical Laboratory Technologist": {
        "education_path": "Explore B.Sc. Medical Laboratory Technology or related laboratory science programs.",
        "beginner_action": "Strengthen Biology and Chemistry and learn about laboratory safety, observation and basic sample-analysis concepts.",
        "opportunities": [
            "Laboratory science projects",
            "Biology experiments",
            "Chemistry activities",
            "Science competitions"
        ]
    },

    "Radiology / Medical Imaging Technologist": {
        "education_path": "Explore undergraduate medical imaging or radiology technology programs.",
        "beginner_action": "Build a strong foundation in Physics and Biology and explore basic medical imaging concepts and safety awareness.",
        "opportunities": [
            "Physics projects",
            "Biology activities",
            "Medical technology exploration",
            "Science competitions"
        ]
    },

    "Occupational Therapist": {
        "education_path": "Explore a Bachelor of Occupational Therapy (BOT) or related rehabilitation program.",
        "beginner_action": "Learn about Biology, human behaviour, daily activities and rehabilitation while developing empathy and communication.",
        "opportunities": [
            "Community activities",
            "Biology projects",
            "Accessibility-awareness activities",
            "Rehabilitation-related exploration"
        ]
    },

    "Optometrist": {
        "education_path": "Explore a Bachelor of Optometry or related vision-science pathway.",
        "beginner_action": "Strengthen Biology and Physics while exploring vision, optics and basic eye-health concepts.",
        "opportunities": [
            "Physics projects",
            "Biology activities",
            "Vision-awareness programs",
            "Science competitions"
        ]
    },

    "Nutritionist / Dietitian": {
        "education_path": "Explore undergraduate programs in Nutrition, Dietetics, Food Science or related health sciences.",
        "beginner_action": "Build knowledge of Biology, Chemistry, nutrition, food science and healthy lifestyle principles.",
        "opportunities": [
            "Nutrition-awareness activities",
            "Food science projects",
            "Health campaigns",
            "Biology projects"
        ]
    },

    "Speech & Language Therapist": {
        "education_path": "Explore undergraduate speech-language pathology or related communication-health programs.",
        "beginner_action": "Develop communication and listening skills while exploring Biology, Psychology, language and human communication.",
        "opportunities": [
            "Communication activities",
            "Public speaking",
            "Language-related projects",
            "Community activities"
        ]
    },

    "Audiologist": {
        "education_path": "Explore undergraduate audiology or hearing and speech-related health programs.",
        "beginner_action": "Strengthen Biology and Physics while exploring hearing science, communication and basic sound concepts.",
        "opportunities": [
            "Physics projects",
            "Communication activities",
            "Hearing-awareness programs",
            "Science competitions"
        ]
    },

    "Respiratory Therapist": {
        "education_path": "Explore undergraduate respiratory therapy or related allied-health programs.",
        "beginner_action": "Strengthen Biology and Physics and learn about the respiratory system, health science and patient-care principles.",
        "opportunities": [
            "Biology projects",
            "Health-awareness activities",
            "Science competitions",
            "Respiratory-system exploration"
        ]
    },

    "Emergency Medical Professional": {
        "education_path": "Explore undergraduate emergency medical services or related healthcare programs.",
        "beginner_action": "Build Biology knowledge, communication, teamwork and emergency-response awareness through appropriate training.",
        "opportunities": [
            "First-aid awareness",
            "Emergency-response training",
            "Teamwork activities",
            "Health-awareness programs"
        ]
    },

    "Public Health Professional": {
        "education_path": "Explore undergraduate Public Health or related health-science programs.",
        "beginner_action": "Develop Biology, statistics, communication and community-health awareness skills.",
        "opportunities": [
            "Community-health activities",
            "Health-awareness campaigns",
            "Data and statistics projects",
            "Public-service activities"
        ]
    },

    "Clinical Psychologist": {
        "education_path": "Explore Psychology and later specialized clinical psychology education according to the requirements applicable to your region.",
        "beginner_action": "Study Psychology and Biology while developing listening, communication, research and ethical-awareness skills.",
        "opportunities": [
            "Psychology projects",
            "Mental-health awareness activities",
            "Research activities",
            "Communication and listening activities"
        ]
    },

    "Genetic Counselor": {
        "education_path": "Explore undergraduate study in Genetics, Biology, Biotechnology or related life sciences before pursuing specialized genetics-related education.",
        "beginner_action": "Strengthen Biology and Chemistry while learning basic genetics and developing communication skills.",
        "opportunities": [
            "Genetics projects",
            "Biology competitions",
            "Life-science activities",
            "Research projects"
        ]
    },

    "Medical Microbiologist": {
        "education_path": "Explore undergraduate Microbiology, Medical Microbiology or related life-science programs.",
        "beginner_action": "Build strong Biology and Chemistry foundations and explore microorganisms, laboratory science and scientific research.",
        "opportunities": [
            "Microbiology projects",
            "Biology experiments",
            "Science competitions",
            "Laboratory-science activities"
        ]
    },

    "Biotechnology Professional": {
        "education_path": "Explore B.Sc. Biotechnology, B.Tech Biotechnology or related life-science programs.",
        "beginner_action": "Strengthen Biology, Chemistry and Physics while exploring biotechnology, laboratory methods and scientific research.",
        "opportunities": [
            "Biotechnology projects",
            "Science competitions",
            "Biology and chemistry activities",
            "Research projects"
        ]
    },

    "Chartered Accountant": {
        "education_path": "Pursue B.Com or a related commerce degree and prepare for the Chartered Accountancy pathway.",
        "beginner_action": "Strengthen Accountancy, Mathematics and Economics while practicing numerical and financial problem solving.",
        "opportunities": [
            "Accounting projects",
            "Commerce competitions",
            "Financial case studies",
            "Business clubs"
        ]
    },

    "Financial Analyst": {
        "education_path": "Consider B.Com, B.Com Finance, BBA Finance, Economics or another finance-related undergraduate pathway.",
        "beginner_action": "Practice financial analysis, spreadsheets, numerical reasoning and basic economics.",
        "opportunities": [
            "Finance projects",
            "Stock-market simulations",
            "Business case studies",
            "Finance competitions"
        ]
    },

    "Business Analyst": {
        "education_path": "Consider BBA, B.Com, BMS, Economics or Business Analytics-related undergraduate study.",
        "beginner_action": "Develop analytical thinking, spreadsheet skills, business understanding and problem-solving ability.",
        "opportunities": [
            "Business case studies",
            "Data-analysis projects",
            "Business clubs",
            "Analytics competitions"
        ]
    },

    "Investment Professional": {
        "education_path": "Consider B.Com Finance, BBA Finance, Economics, BMS or another finance-related pathway.",
        "beginner_action": "Learn basic financial markets, investment concepts, risk and numerical analysis.",
        "opportunities": [
            "Investment simulations",
            "Finance clubs",
            "Market research projects",
            "Financial case studies"
        ]
    },

    "Entrepreneur": {
        "education_path": "Consider BBA, BMS, B.Com, Economics or Entrepreneurship-related study while developing practical business skills.",
        "beginner_action": "Identify a real-world problem and develop a simple business idea, customer profile and basic business model.",
        "opportunities": [
            "Entrepreneurship clubs",
            "Business-plan competitions",
            "Startup projects",
            "Innovation challenges"
        ]
    },

    "Banking Professional": {
        "education_path": "Consider B.Com, BBA, Economics, Banking & Finance or another commerce-related undergraduate pathway.",
        "beginner_action": "Strengthen Accountancy, Economics and Mathematics while learning basic banking and financial concepts.",
        "opportunities": [
            "Banking-awareness activities",
            "Commerce competitions",
            "Financial literacy projects",
            "Aptitude practice"
        ]
    },

    "Investment Banker": {
        "education_path": "Consider B.Com, BBA Finance, Economics or BMS followed by relevant finance specialization.",
        "beginner_action": "Develop strong numerical reasoning, financial analysis, business understanding and communication skills.",
        "opportunities": [
            "Finance case competitions",
            "Business analysis projects",
            "Investment simulations",
            "Presentation activities"
        ]
    },

    "Financial Planner / Advisor": {
        "education_path": "Consider B.Com, BBA Finance, B.Sc Finance, Economics or a related financial-planning pathway.",
        "beginner_action": "Learn budgeting, saving, investment basics and financial decision-making.",
        "opportunities": [
            "Financial-literacy projects",
            "Budgeting activities",
            "Investment simulations",
            "Finance clubs"
        ]
    },

    "Risk Analyst": {
        "education_path": "Consider B.Com, BBA Finance, Economics, Statistics or another quantitative finance pathway.",
        "beginner_action": "Strengthen Mathematics, Statistics and Economics while learning how businesses identify and manage risk.",
        "opportunities": [
            "Statistics projects",
            "Risk-analysis case studies",
            "Finance competitions",
            "Data-analysis activities"
        ]
    },

    "Credit Analyst": {
        "education_path": "Consider B.Com, BBA Finance, Economics, Statistics or another banking and finance pathway.",
        "beginner_action": "Practice financial statement analysis, numerical reasoning and basic credit concepts.",
        "opportunities": [
            "Banking case studies",
            "Financial-analysis projects",
            "Commerce competitions",
            "Aptitude practice"
        ]
    },

    "Insurance Professional": {
        "education_path": "Consider B.Com, BBA, Economics, Actuarial Science or another finance-related undergraduate pathway.",
        "beginner_action": "Build Mathematics and Economics foundations while learning about insurance, risk and financial protection.",
        "opportunities": [
            "Insurance-awareness projects",
            "Risk-analysis activities",
            "Finance clubs",
            "Mathematics competitions"
        ]
    },

    "Tax Consultant": {
        "education_path": "Consider B.Com, B.Com Accounting & Finance, Economics or Taxation-related study.",
        "beginner_action": "Strengthen Accountancy and Economics and learn the basic concepts of taxation and financial records.",
        "opportunities": [
            "Accounting projects",
            "Tax-awareness activities",
            "Commerce competitions",
            "Financial case studies"
        ]
    },

    "Management Consultant": {
        "education_path": "Consider BBA, BMS, B.Com, Economics or another business-management pathway.",
        "beginner_action": "Develop structured problem solving, business analysis, communication and decision-making skills.",
        "opportunities": [
            "Business case competitions",
            "Management projects",
            "Debates and presentations",
            "Entrepreneurship clubs"
        ]
    },

    "Marketing Professional": {
        "education_path": "Consider BBA Marketing, BBA, B.Com, Mass Communication or another marketing-related pathway.",
        "beginner_action": "Explore consumer behaviour, communication, branding, digital marketing and basic business analysis.",
        "opportunities": [
            "Marketing projects",
            "Branding activities",
            "Social-media campaigns",
            "Business competitions"
        ]
    },

    "Human Resources Professional": {
        "education_path": "Consider BBA Human Resources, BBA, BMS, Psychology or another people-management pathway.",
        "beginner_action": "Develop communication, empathy, teamwork and understanding of workplace behaviour.",
        "opportunities": [
            "Leadership activities",
            "Team projects",
            "Communication competitions",
            "Student-organizing activities"
        ]
    },

    "Operations Manager": {
        "education_path": "Consider BBA, BMS, B.Com or Operations Management-related undergraduate study.",
        "beginner_action": "Practice planning, numerical reasoning, process improvement and structured problem solving.",
        "opportunities": [
            "Operations projects",
            "Business case studies",
            "Event management activities",
            "Team leadership"
        ]
    },

    "Supply Chain Professional": {
        "education_path": "Consider BBA, B.Com, BMS or Supply Chain Management-related undergraduate study.",
        "beginner_action": "Learn basic logistics, inventory, planning and business operations concepts.",
        "opportunities": [
            "Logistics projects",
            "Business simulations",
            "Operations case studies",
            "Supply-chain awareness activities"
        ]
    },

    "FinTech Professional": {
        "education_path": "Consider B.Com, BBA Finance, B.Sc Finance, Computer Science or another finance-and-technology pathway.",
        "beginner_action": "Combine financial knowledge with technology, data analysis and basic programming skills.",
        "opportunities": [
            "FinTech projects",
            "Coding activities",
            "Financial-data projects",
            "Technology competitions"
        ]
    },

    "Economist": {
        "education_path": "Consider B.A. Economics, B.Sc Economics, B.Com, Mathematics or another economics-related pathway.",
        "beginner_action": "Strengthen Economics and Mathematics and practice interpreting data, graphs and real-world economic trends.",
        "opportunities": [
            "Economics projects",
            "Data-analysis activities",
            "Economic debates",
            "Research competitions"
        ]
    },

    "Business Development Professional": {
        "education_path": "Consider BBA, B.Com, BMS, Marketing or another business-development pathway.",
        "beginner_action": "Develop communication, relationship-building, business analysis and presentation skills.",
        "opportunities": [
            "Business projects",
            "Entrepreneurship clubs",
            "Presentation activities",
            "Marketing competitions"
        ]
    },


    "Lawyer": {
        "education_path": "Consider an integrated law degree such as BA LLB, BBA LLB or B.Com LLB, followed by the required professional steps for legal practice.",
        "beginner_action": "Strengthen reading, logical reasoning, writing, communication and understanding of laws and current affairs.",
        "opportunities": [
            "Debate and public-speaking activities",
            "Mock parliament and legal-awareness programs",
            "Essay and legal-writing competitions",
            "Beginner legal research projects"
        ]
    },

    "Legal Advisor": {
        "education_path": "Consider an integrated law degree such as BA LLB, BBA LLB or B.Com LLB and build knowledge of contracts, regulations and legal procedures.",
        "beginner_action": "Develop analytical reading, writing and communication skills while learning how laws and regulations affect organizations and individuals.",
        "opportunities": [
            "Legal-awareness activities",
            "Case-study analysis",
            "Debates and communication competitions",
            "Basic contract and legal-document exercises"
        ]
    },

    "Corporate Legal Professional": {
        "education_path": "Consider BBA LLB, B.Com LLB, BA LLB or another suitable integrated law pathway with an interest in business and corporate law.",
        "beginner_action": "Build an understanding of business, contracts, company law, communication and analytical reasoning.",
        "opportunities": [
            "Business and legal case studies",
            "Entrepreneurship activities",
            "Debates and presentations",
            "Basic corporate-law research projects"
        ]
    },

    "Legal Researcher": {
        "education_path": "Consider an integrated law degree such as BA LLB, BBA LLB or B.Com LLB, with additional focus on legal research and writing.",
        "beginner_action": "Practice finding reliable information, comparing legal issues, writing structured summaries and developing logical arguments.",
        "opportunities": [
            "Legal research projects",
            "Case-study analysis",
            "Essay and research-writing competitions",
            "Debates and mock parliament"
        ]
    },

    "Public Prosecutor": {
        "education_path": "Consider an integrated law degree such as BA LLB and then follow the applicable professional and legal-service requirements for prosecution work.",
        "beginner_action": "Develop strong legal reasoning, communication, public-speaking, research and understanding of criminal-law concepts.",
        "opportunities": [
            "Mock trials and moot-court activities",
            "Debates and public-speaking competitions",
            "Legal-awareness programs",
            "Criminal-law case-study exercises"
        ]
    },


    "Civil Services Professional": {
        "education_path": "Consider a bachelor's degree in any suitable discipline such as Political Science, History, Economics, Public Administration, Law or another subject, followed by preparation for the relevant civil-services examination.",
        "beginner_action": "Build strong reading, writing, reasoning and general-awareness skills and regularly follow important national and public-policy issues.",
        "opportunities": [
            "Current-affairs activities",
            "Essay-writing competitions",
            "Debates and mock parliament",
            "Civic and public-policy projects"
        ]
    },

    "Government Officer": {
        "education_path": "Choose a bachelor's degree aligned with your interests and explore government recruitment examinations and roles relevant to your qualification.",
        "beginner_action": "Strengthen general awareness, communication, reasoning, quantitative aptitude and understanding of public institutions.",
        "opportunities": [
            "General-awareness activities",
            "Civic projects",
            "Debates and public-speaking",
            "Aptitude and reasoning practice"
        ]
    },

    "Public Administration Professional": {
        "education_path": "Consider a bachelor's degree in Public Administration, Political Science, Economics, Sociology, Law or another social-science discipline.",
        "beginner_action": "Learn how public institutions work and develop skills in policy analysis, communication, research and problem solving.",
        "opportunities": [
            "Public-policy projects",
            "Civic-awareness activities",
            "Research and essay writing",
            "Mock parliament and debates"
        ]
    },

    "Policy Professional": {
        "education_path": "Consider a bachelor's degree in Political Science, Economics, Public Administration, Law, Sociology or another policy-related discipline.",
        "beginner_action": "Develop research, critical-thinking, writing and data-interpretation skills while following real-world public-policy issues.",
        "opportunities": [
            "Policy research projects",
            "Current-affairs analysis",
            "Debates and essay competitions",
            "Community and civic projects"
        ]
    },


    "Army Officer": {
        "education_path": "Consider a bachelor's degree in a suitable discipline and explore the applicable Indian Army officer-entry routes and selection requirements for your qualification and age.",
        "beginner_action": "Build academic consistency, physical fitness, discipline, leadership, teamwork and awareness of national and defence-related issues.",
        "opportunities": [
            "Sports and fitness activities",
            "Leadership and team projects",
            "NCC or similar youth activities where available",
            "General-awareness and defence-awareness activities"
        ]
    },

    "Navy Officer": {
        "education_path": "Choose a bachelor's or engineering pathway appropriate to the naval officer-entry route you are interested in and check the current eligibility requirements.",
        "beginner_action": "Strengthen academics, physical fitness, teamwork, discipline, leadership and awareness of maritime and national-security topics.",
        "opportunities": [
            "Swimming and fitness activities",
            "Leadership and team projects",
            "NCC or similar youth activities where available",
            "Science, mathematics and defence-awareness activities"
        ]
    },

    "Air Force Officer": {
        "education_path": "Consider a bachelor's or engineering pathway suited to the Air Force officer-entry route you are interested in and check the current eligibility requirements.",
        "beginner_action": "Develop academic strength, physical fitness, discipline, leadership, communication and awareness of aviation and national-security topics.",
        "opportunities": [
            "Sports and fitness activities",
            "Leadership and team projects",
            "Science and aviation-related activities",
            "NCC or similar youth activities where available"
        ]
    },

    "Defence Technical Professional": {
        "education_path": "Consider B.Tech/B.E. or another relevant technical degree in areas such as Computer Science, Electronics, Electrical, Mechanical, Aerospace or related engineering disciplines.",
        "beginner_action": "Strengthen Mathematics, Physics and technical problem solving while building practical engineering and technology skills.",
        "opportunities": [
            "Robotics and electronics projects",
            "Coding and technology competitions",
            "Engineering exhibitions",
            "Defence technology and innovation projects"
        ]
    },


    "Research Scientist": {
        "education_path": "Consider B.Sc. or an integrated science program in a relevant subject such as Physics, Chemistry, Biology, Mathematics or another scientific discipline, followed by advanced study for research-oriented careers.",
        "beginner_action": "Strengthen scientific reasoning, Mathematics and subject knowledge while practicing experiments, observation, data collection and evidence-based thinking.",
        "opportunities": [
            "Science exhibitions",
            "Research and science projects",
            "Laboratory activities",
            "Science competitions and olympiads"
        ]
    },

    "Scientific Researcher": {
        "education_path": "Consider a B.Sc. or integrated science pathway related to your interests, followed by higher studies and research training.",
        "beginner_action": "Develop curiosity, scientific reading, experimental thinking, data analysis and structured research skills.",
        "opportunities": [
            "Science research projects",
            "Science fairs and exhibitions",
            "Laboratory activities",
            "Research and science competitions"
        ]
    },

    "Laboratory Professional": {
        "education_path": "Consider B.Sc. or a relevant laboratory-focused undergraduate program in areas such as Biology, Chemistry, Biotechnology or Medical Laboratory Science.",
        "beginner_action": "Build knowledge of laboratory safety, observation, measurement, scientific procedures and accurate record keeping.",
        "opportunities": [
            "School laboratory projects",
            "Science exhibitions",
            "Practical experiments",
            "Laboratory and science clubs"
        ]
    },

    "Research Analyst": {
        "education_path": "Consider a bachelor's degree in Mathematics, Statistics, Economics, Computer Science, Science or another research-oriented discipline.",
        "beginner_action": "Develop analytical thinking, research methods, data interpretation, Mathematics and clear technical writing.",
        "opportunities": [
            "Data-analysis projects",
            "Research and survey projects",
            "Science or economics competitions",
            "Research-writing activities"
        ]
    },


    "Architect": {
        "education_path": "Consider B.Arch or another architecture-related undergraduate pathway and check the current admission and eligibility requirements for the institutions you are interested in.",
        "beginner_action": "Develop spatial thinking, Mathematics, drawing, visual communication and an understanding of buildings and design.",
        "opportunities": [
            "Architecture sketching",
            "Design competitions",
            "Model-making projects",
            "Architecture and design exhibitions"
        ]
    },

    "UI / UX Designer": {
        "education_path": "Consider B.Des, BFA, a technology degree with design specialization or another suitable design pathway.",
        "beginner_action": "Learn user-centered design, visual design, basic interface tools and how to create simple digital prototypes.",
        "opportunities": [
            "UI design projects",
            "Website or app redesign exercises",
            "Design competitions",
            "Beginner portfolio projects"
        ]
    },

    "Product Designer": {
        "education_path": "Consider B.Des, Product Design, Industrial Design, Engineering with design exposure or another relevant undergraduate pathway.",
        "beginner_action": "Practice problem identification, user research, ideation, sketching, prototyping and evaluating practical solutions.",
        "opportunities": [
            "Product-design projects",
            "Prototype-building activities",
            "Design competitions",
            "Innovation and maker projects"
        ]
    },

    "Graphic Designer": {
        "education_path": "Consider B.Des, BFA, Visual Communication, Graphic Design or another suitable design-related pathway.",
        "beginner_action": "Build skills in typography, composition, visual communication and beginner digital-design tools.",
        "opportunities": [
            "Poster and branding projects",
            "School or college publication design",
            "Design competitions",
            "Portfolio-building projects"
        ]
    },

    "Interior Designer": {
        "education_path": "Consider a bachelor's degree or diploma pathway in Interior Design, Interior Architecture or another related design field.",
        "beginner_action": "Develop spatial planning, drawing, color, materials and visual-presentation skills.",
        "opportunities": [
            "Room-layout projects",
            "Interior-design sketches",
            "3D modelling or visualization activities",
            "Design exhibitions and competitions"
        ]
    },


    "Journalist": {
        "education_path": "Consider Journalism, Mass Communication, Media Studies, English or another communication-related bachelor's degree.",
        "beginner_action": "Develop strong writing, interviewing, research, fact-checking and communication skills while following current events.",
        "opportunities": [
            "School or college publications",
            "Interview and reporting projects",
            "Writing competitions",
            "Media and journalism clubs"
        ]
    },

    "Content Creator": {
        "education_path": "Consider Media Studies, Journalism, Communication, Digital Media, Design or another relevant bachelor's pathway.",
        "beginner_action": "Practice storytelling, writing, video or audio production and responsible digital communication while building a small portfolio.",
        "opportunities": [
            "Blogging and article projects",
            "Educational videos or podcasts",
            "School or college media projects",
            "Digital-content portfolio projects"
        ]
    },

    "Media Professional": {
        "education_path": "Consider Journalism, Mass Communication, Media Studies, Film, Digital Media or another relevant media-related degree.",
        "beginner_action": "Build communication, storytelling, research, production and teamwork skills across different forms of media.",
        "opportunities": [
            "Media-club activities",
            "Video and audio projects",
            "School or college publications",
            "Media-production competitions"
        ]
    },

    "Public Relations Professional": {
        "education_path": "Consider Public Relations, Mass Communication, Journalism, Marketing, Communication or another related bachelor's degree.",
        "beginner_action": "Develop writing, presentation, relationship-building, communication and understanding of organizational reputation.",
        "opportunities": [
            "Public-speaking activities",
            "Event-management projects",
            "Communication campaigns",
            "School or college media activities"
        ]
    },

    "Communication Specialist": {
        "education_path": "Consider Communication, Journalism, Mass Communication, English, Media Studies or another communication-focused bachelor's degree.",
        "beginner_action": "Strengthen writing, presentation, storytelling, audience awareness and professional communication skills.",
        "opportunities": [
            "Writing competitions",
            "Public-speaking activities",
            "Presentation and communication projects",
            "School or college publications"
        ]
    },


    "Teacher": {
        "education_path": "Choose a bachelor's degree in the subject you want to teach and then follow the applicable teacher-education and qualification requirements.",
        "beginner_action": "Strengthen subject knowledge, communication and the ability to explain concepts clearly to different learners.",
        "opportunities": [
            "Peer teaching",
            "Tutoring or mentoring activities",
            "Educational projects",
            "Teaching and presentation competitions"
        ]
    },

    "Education Professional": {
        "education_path": "Consider a bachelor's degree in Education, a subject specialization or another relevant discipline, followed by qualifications suited to the education role you want to pursue.",
        "beginner_action": "Develop communication, organization, learning-design and student-support skills.",
        "opportunities": [
            "Educational projects",
            "Peer mentoring",
            "Academic clubs",
            "Learning-resource creation"
        ]
    },

    "Academic Counselor": {
        "education_path": "Consider Psychology, Education, Counseling, Social Sciences or another relevant bachelor's pathway, followed by appropriate counseling-related qualifications.",
        "beginner_action": "Build active listening, communication, empathy, observation and academic guidance skills.",
        "opportunities": [
            "Peer mentoring",
            "Student-support activities",
            "Education-awareness projects",
            "Communication and counseling workshops"
        ]
    },

    "Education Content Developer": {
        "education_path": "Consider Education, English, Media, Design, Computer Science, a subject specialization or another relevant bachelor's pathway.",
        "beginner_action": "Learn how to explain concepts clearly and create useful educational content using writing, visual or digital tools.",
        "opportunities": [
            "Educational videos",
            "Study notes and learning resources",
            "Teaching presentations",
            "Educational-content projects"
        ]
    },


    "Agricultural Scientist": {
        "education_path": "Consider B.Sc. Agriculture, Agricultural Sciences, Horticulture, Soil Science, Biotechnology or another relevant agricultural-science pathway.",
        "beginner_action": "Build knowledge of biology, agriculture, soil, crops, sustainability and scientific observation while exploring local agricultural challenges.",
        "opportunities": [
            "Agriculture and science projects",
            "School or college science exhibitions",
            "Sustainability activities",
            "Agriculture and nature clubs"
        ]
    },

    "Agriculture Officer": {
        "education_path": "Consider B.Sc. Agriculture or another relevant agricultural degree and explore the applicable government or agricultural-sector qualification requirements.",
        "beginner_action": "Develop knowledge of crops, soil, agricultural practices, rural communities and basic agricultural problem solving.",
        "opportunities": [
            "Agriculture awareness projects",
            "Sustainability activities",
            "School or college science projects",
            "Community and rural-development activities"
        ]
    },

    "Environmental Professional": {
        "education_path": "Consider Environmental Science, Environmental Engineering, Biology, Ecology, Geography or another relevant environmental pathway.",
        "beginner_action": "Learn about ecosystems, pollution, sustainability and environmental problem solving through observation and small projects.",
        "opportunities": [
            "Environmental projects",
            "Tree-planting and conservation activities",
            "Waste-management projects",
            "Nature and sustainability clubs"
        ]
    },

    "Food Technology Professional": {
        "education_path": "Consider B.Tech Food Technology, Food Science, Biotechnology, Nutrition or another relevant food-science pathway.",
        "beginner_action": "Strengthen Chemistry, Biology, scientific observation and understanding of food processing, safety and quality.",
        "opportunities": [
            "Food-science projects",
            "Science exhibitions",
            "Food-safety awareness activities",
            "Biology and chemistry practical projects"
        ]
    },


    "Psychologist": {
        "education_path": "Consider a bachelor's degree in Psychology or a related social-science discipline, followed by the additional education and professional qualifications required for the psychology role you want to pursue.",
        "beginner_action": "Develop observation, communication, research and understanding of human behaviour while learning to distinguish evidence-based psychology from unsupported claims.",
        "opportunities": [
            "Psychology projects",
            "Behaviour and observation activities",
            "Research and survey projects",
            "Psychology or social-science clubs"
        ]
    },

    "Social Researcher": {
        "education_path": "Consider Psychology, Sociology, Social Work, Political Science, Economics or another social-science bachelor's degree.",
        "beginner_action": "Build research, observation, communication, survey design, data interpretation and critical-thinking skills.",
        "opportunities": [
            "Social research projects",
            "Survey and observation activities",
            "Community projects",
            "Research-writing competitions"
        ]
    },

    "Counseling Professional": {
        "education_path": "Consider Psychology, Counseling, Education, Social Work or another relevant bachelor's pathway, followed by the additional professional training appropriate to the counseling role.",
        "beginner_action": "Develop active listening, empathy, communication, observation and ethical understanding while learning about human behaviour.",
        "opportunities": [
            "Peer-support activities",
            "Communication and listening workshops",
            "Psychology projects",
            "Community and student-support activities"
        ]
    },

    "Social Science Researcher": {
        "education_path": "Consider Sociology, Psychology, Political Science, Economics, History, Geography or another social-science bachelor's degree, followed by research-oriented higher study if desired.",
        "beginner_action": "Strengthen research methods, critical thinking, writing, observation, data interpretation and understanding of social issues.",
        "opportunities": [
            "Social research projects",
            "Surveys and community studies",
            "Essay and research-writing competitions",
            "Civic and social-awareness projects"
        ]
    },

})
