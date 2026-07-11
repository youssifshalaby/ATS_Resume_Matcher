import re

def analyze_resume_structure(text):

    text = text.lower()
    results = {}

    word_count = len(text.split())
    char_count = len(text)
    results["word_count"] = word_count
    results["character_count"] = char_count

    # Detect sections

    sections = {
        "Experience": [
            "experience",
            "work experience",
            "employment"
        ],

        "Education": [
            "education",
            "degree",
            "university"
        ],

        "Projects": [
            "projects",
            "project experience"
        ],

        "Skills": [
            "skills",
            "technical skills"
        ],

        "Certifications": [
            "certification",
            "certificate"
        ]
    }

    detected_sections = []

    for section, keywords in sections.items():
        for keyword in keywords:
            if keyword in text:
                detected_sections.append(section)
                break
    
    results["sections"] = detected_sections

    return results
    