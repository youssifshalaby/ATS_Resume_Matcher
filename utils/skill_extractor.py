import json
import re

def load_skills(path):

    with open(path, encoding="utf-8") as file:

        return json.load(file)

def extract_skills(text, skills):
    text = text.lower()
    found_skills = set()

    for skill in skills:
        pattern = rf"(?<!\w){re.escape(skill.lower())}(?!\w)"

        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)