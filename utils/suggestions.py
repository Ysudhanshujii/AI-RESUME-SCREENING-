def get_suggestions(text, skills, category=None):

    text = text.lower() if text else ""
    skills = skills if skills else []
    suggestions = []

    # 🔹 1. Skill Gap (safe check)
    required_skills = {
        "DATA SCIENCE": ["python", "machine learning", "pandas", "numpy"],
        "WEB DEVELOPMENT": ["html", "css", "javascript", "react"],
        "FINANCE": ["excel", "accounting", "analysis", "tax"],
        "ENGINEERING": ["c++", "java", "problem solving"]
    }

    if category and category in required_skills:
        missing = [s for s in required_skills[category] if s not in text]
        if missing:
            suggestions.append(f"Add skills like: {', '.join(missing[:3])}")

    # 🔹 2. Section detection (better matching)
    section_keywords = {
        "projects": ["project", "projects"],
        "experience": ["experience", "work experience"],
        "education": ["education", "degree", "college"],
        "internship": ["internship", "intern"]
    }

    for sec, keywords in section_keywords.items():
        if not any(k in text for k in keywords):
            suggestions.append(f"Add {sec} section")

    # 🔹 3. Resume length
    if len(text.split()) < 120:
        suggestions.append("Increase resume content with more details")

    # 🔹 4. Weak words detection
    weak_words = ["hardworking", "good", "responsible", "dedicated"]
    if any(w in text for w in weak_words):
        suggestions.append("Replace weak words with strong action verbs")

    # 🔹 5. Skills count
    if len(skills) < 5:
        suggestions.append("Add more technical skills relevant to your domain")

    # 🔹 6. Project quality
    if "project" in text and len(text.split()) < 200:
        suggestions.append("Improve project descriptions with impact/results")

    # 🔹 Remove duplicates safely (without losing order)
    final_suggestions = []
    for s in suggestions:
        if s not in final_suggestions:
            final_suggestions.append(s)

    return final_suggestions[:5]