def calculate_score(text, skills):

    score = 0
    text = text.lower()

    #  Length (0–20)
    length = len(text)
    if length > 1500:
        score += 20
    elif length > 800:
        score += 15
    else:
        score += 8

    #  Skills (0–25)
    score += min(len(skills) * 3, 25)

    #  Sections (0–30)
    sections = ["experience","project","education","skill"]
    for sec in sections:
        if sec in text:
            score += 7

    #  Diversity (0–25)
    unique_words = len(set(text.split()))
    if unique_words > 200:
        score += 25
    elif unique_words > 100:
        score += 15
    else:
        score += 5

    return min(score, 95)  # never 100