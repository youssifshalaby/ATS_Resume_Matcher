SEMANTIC_WEIGHT = 0.7
SKILL_WEIGHT = 0.3


def calculate_skill_score(resume_skills, job_skills):

    if not job_skills:
        return 0.0

    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    matched_skills = resume_skills.intersection(
        job_skills
    )

    score = (
        len(matched_skills)
        /
        len(job_skills)
    ) * 100

    return round(score, 2)



def calculate_final_score(semantic_score,skill_score):
    final_score = (
        semantic_score * SEMANTIC_WEIGHT
        +
        skill_score * SKILL_WEIGHT
    )

    return round(final_score, 2)