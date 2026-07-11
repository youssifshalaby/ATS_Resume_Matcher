import json
from spacy.matcher import PhraseMatcher
from utils.models import nlp

matcher = PhraseMatcher(
    nlp.vocab,
    attr="LOWER"
)

skill_map = {}
    

def build_matcher(skills: dict):
    patterns = []
    for skill , aliases in skills.items():
        for alias in aliases:
            patterns.append(nlp.make_doc(alias))
            skill_map[alias.lower()] = skill
    matcher.add(skill,patterns)

def extract_skills_spacy(text:str):
    doc = nlp(text)
    matches = matcher(doc)
    found_skills = set()

    for _, start, end in matches:

        alias = doc[start:end].text.lower()

        found_skills.add(
            skill_map[alias]
        )
    return sorted(found_skills)