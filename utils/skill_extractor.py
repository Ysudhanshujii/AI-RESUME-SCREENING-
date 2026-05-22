import re

#  curated skill list (balanced)
SKILL_SET = [
    "python","java","c++","html","css","javascript","sql",
    "machine learning","deep learning","data analysis",
    "react","node","flask","django","mongodb",
    "excel","power bi","tableau",
    "communication","management","teamwork","leadership",
    "marketing","sales","recruitment"
]

#  stop/noise words
NOISE_WORDS = [
    "experience","learning","knowledge","skills","ability",
    "responsible","work","team","project","education","communication"
]


def extract_skills(text):
    text = text.lower()

    found = set()

    #  phrase matching (important)
    for skill in SKILL_SET:
        if skill in text:
            found.add(skill)

    #  word-level filtering (backup)
    words = re.findall(r'\b[a-z]+\b', text)

    for word in words:
        if word in SKILL_SET:
            found.add(word)

    #  remove noise
    found = [s for s in found if s not in NOISE_WORDS]

    #  fallback (never empty)
    if len(found) == 0:
        found = ["communication", "teamwork"]

    return list(found)[:10]