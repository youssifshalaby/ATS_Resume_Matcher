from utils.skill_extractor import load_skills, extract_skills
from utils.spacy_matcher import build_matcher, extract_skills_spacy
from utils.semantic_matcher import SemanticMatcher


skills_dict = load_skills("data/skills.json")


build_matcher(skills_dict)

semantic_matcher = SemanticMatcher(skills_dict)

def extract_all_skills(text):
    regex_skills = extract_skills(text, skills_dict)

    spacy_skills = extract_skills_spacy(text)

    semantic_skills = semantic_matcher.extract(text)

    all_skills = sorted(
        set(regex_skills) | set(spacy_skills) | set(semantic_skills)
    )

    return all_skills