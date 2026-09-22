def recommend_graduation_higher_education(
    degree="",
    branch="",
    domain="",
    career=""
):
    text = f"{degree} {branch} {domain} {career}".lower()

    recommendations = []

    def add(title, category, reason, focus, suitable_for):
        recommendations.append({
            "title": title,
            "category": category,
            "reason": reason,
            "focus": focus,
            "suitable_for": suitable_for
        })

    # Technology / Computer
    if any(k in text for k in [
        "computer", "cse", "software", "information technology",
        "technology", "ai", "machine learning", "cyber",
        "data", "cloud", "devops"
    ]):
        add(
            "M.Tech / M.E. in Computer Science",
            "Technical Postgraduate Degree",
            "Build deeper technical knowledge for advanced computing careers.",
            "Advanced computing, software engineering and technical specialization.",
            "Students targeting software, AI, cloud, cybersecurity or technical R&D."
        )

        add(
            "M.Tech / M.Sc. in Artificial Intelligence & Machine Learning",
            "AI / ML Specialization",
            "Useful for students targeting AI and machine-learning pathways.",
            "Machine learning, deep learning, intelligent systems and applied AI.",
            "Students interested in AI, automation and data-driven systems."
        )

        add(
            "M.Sc. / M.Tech. in Data Science",
            "Data Specialization",
            "Provides a structured path into analytics and data science.",
            "Statistics, Python, machine learning, analytics and data engineering.",
            "Students interested in data, analytics and decision systems."
        )

        add(
            "Cybersecurity / Information Security Specialization",
            "Security Specialization",
            "Builds specialized knowledge for cybersecurity careers.",
            "Network security, secure systems, cyber defense and security operations.",
            "Students interested in cybersecurity and information security."
        )

        add(
            "Cloud Computing / DevOps Specialization",
            "Cloud & Infrastructure",
            "Useful for students interested in scalable software infrastructure.",
            "Cloud platforms, Linux, automation, containers and DevOps.",
            "Students targeting cloud, DevOps and infrastructure roles."
        )

        add(
            "MCA",
            "Computing Postgraduate Degree",
            "A computing-focused postgraduate option for eligible graduates.",
            "Software development, application systems and computing concepts.",
            "Graduates who want to strengthen their computing/software foundation."
        )

    # Business / Commerce / Finance
    if any(k in text for k in [
        "business", "finance", "commerce", "economics",
        "management", "bba", "bcom", "financial"
    ]):
        add(
            "MBA in Finance",
            "Management Specialization",
            "Strengthens finance and management knowledge for business careers.",
            "Corporate finance, financial analysis, strategy and management.",
            "Students targeting finance, banking or corporate roles."
        )

        add(
            "MBA in Business Analytics",
            "Analytics & Management",
            "Combines business decision-making with analytical skills.",
            "Business analytics, data interpretation and decision support.",
            "Students interested in analytics and business strategy."
        )

        add(
            "M.Com",
            "Commerce Postgraduate Degree",
            "Provides advanced study in commerce and related subjects.",
            "Accounting, taxation, finance and commerce.",
            "Commerce graduates seeking deeper academic specialization."
        )

    # Engineering
    if any(k in text for k in [
        "mechanical", "civil", "electrical", "electronics",
        "ece", "eee", "engineering", "manufacturing"
    ]):
        add(
            "M.Tech / M.E. in Engineering Specialization",
            "Engineering Postgraduate Degree",
            "Allows deeper specialization in the student's engineering field.",
            "Advanced engineering concepts, design, systems and technical research.",
            "Engineering graduates targeting advanced technical roles."
        )

        add(
            "Engineering Design / Automation Specialization",
            "Applied Engineering",
            "Useful for graduates interested in technical design and automation.",
            "CAD, automation, control systems and engineering applications.",
            "Students interested in practical and industrial engineering work."
        )

    # Research
    if any(k in text for k in [
        "research", "science", "mathematics", "physics",
        "chemistry", "biology", "researcher"
    ]):
        add(
            "M.Sc. in a Relevant Science / Research Field",
            "Research Postgraduate Degree",
            "Provides a stronger foundation for advanced study and research.",
            "Advanced subject knowledge, experimentation and research methods.",
            "Students considering research, teaching or scientific careers."
        )

        add(
            "PhD / Doctoral Research Path",
            "Research Path",
            "A doctoral path may be considered after the required postgraduate preparation.",
            "Original research, specialization and academic contribution.",
            "Students with strong interest in research and higher education."
        )

    # Management fallback / broad option
    add(
        "MBA / Management Path",
        "Cross-Disciplinary Option",
        "A management degree can complement many undergraduate backgrounds.",
        "Business, strategy, leadership, operations and management.",
        "Graduates interested in management, business or leadership."
    )

    # Remove duplicates while preserving order
    unique = []
    seen = set()

    for item in recommendations:
        if item["title"] not in seen:
            seen.add(item["title"])
            unique.append(item)

    return unique[:8]
