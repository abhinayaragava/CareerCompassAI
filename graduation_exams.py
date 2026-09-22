def recommend_graduation_exams(
    degree="",
    branch="",
    domain="",
    goal="",
    career=""
):
    text = f"{degree} {branch} {domain} {goal} {career}".lower()

    exams = []

    def add(name, category, relevance, preparation):
        exams.append({
            "name": name,
            "category": category,
            "relevance": relevance,
            "preparation": preparation
        })

    if any(k in text for k in [
        "computer", "technology", "software", "information technology",
        "engineering", "data", "ai", "cyber"
    ]):
        add(
            "GATE",
            "Higher Studies / Technical",
            "Relevant to graduates considering postgraduate technical study and related opportunities.",
            "Build strong fundamentals in the relevant engineering or technical subject and practice previous questions."
        )

    if any(k in text for k in [
        "government", "public service", "policy",
        "administration", "civil"
    ]) or "competitive exams" in goal.lower():
        add(
            "Civil Services Examination",
            "Government / Public Service",
            "A major graduate-level pathway for students interested in public administration and civil services.",
            "Build a structured foundation in the examination syllabus, current affairs, writing and practice tests."
        )

    if any(k in text for k in [
        "finance", "commerce", "business", "economics",
        "banking", "management"
    ]):
        add(
            "Banking and Financial-Sector Recruitment Exams",
            "Banking / Finance",
            "Relevant for graduates targeting banking and financial-sector roles.",
            "Strengthen quantitative aptitude, reasoning, English and general/business awareness."
        )

    if any(k in text for k in [
        "law", "public policy", "government", "social science"
    ]):
        add(
            "Government Recruitment Examinations",
            "Government",
            "Can be relevant to graduates seeking government-sector recruitment pathways.",
            "Build aptitude, reasoning, language, general awareness and role-specific knowledge."
        )

    if "higher studies" in goal.lower():
        add(
            "Postgraduate Admission Examinations",
            "Higher Studies",
            "Useful for graduates applying to postgraduate programs where an entrance examination is required.",
            "Identify target institutions and syllabus, then prepare subject-specific concepts and previous papers."
        )

    # Keep order but remove duplicates.
    unique = []
    seen = set()

    for exam in exams:
        if exam["name"] not in seen:
            seen.add(exam["name"])
            unique.append(exam)

    return unique[:6]
