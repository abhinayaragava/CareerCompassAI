def normalize_skill(value):
    return str(value or "").strip().lower()


def analyze_graduation_skill_gap(current_skills, career_data):
    """
    Compare the student's current skills with the skills
    suggested for the selected Graduation career.
    """

    current = {
        normalize_skill(skill)
        for skill in str(current_skills or "").split(",")
        if skill.strip()
    }

    required = career_data.get("skills", []) if career_data else []

    possessed = []
    missing = []

    for skill in required:
        if normalize_skill(skill) in current:
            possessed.append(skill)
        else:
            missing.append(skill)

    total_required = len(required)
    total_possessed = len(possessed)

    if total_required:
        coverage = round(
            (total_possessed / total_required) * 100
        )
    else:
        coverage = 0

    priority = missing[:3]

    return {
        "career": career_data.get("career", "") if career_data else "",
        "required": required,
        "possessed": possessed,
        "missing": missing,
        "priority": priority,
        "coverage": coverage
    }
