from utils.matcher import extract_all_skills
from utils.embedding import get_embedding
from utils.similarity import calculate_similarity
from utils.scorer import calculate_skill_score, calculate_final_score
from utils.recommendation import generate_recommendations
from utils.resume_analyzer import analyze_resume_structure

def analyze_resume(resume_text,job_description):

    resume_skills = extract_all_skills(resume_text)

    job_skills = extract_all_skills(job_description)

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = sorted(resume_set & job_set)
    missing_skills = sorted(job_set - resume_set)

    semantic_score = calculate_similarity(
        get_embedding(resume_text),
        get_embedding(job_description)
    )
    semantic_score = round(
        semantic_score,
        2
    )
    skill_score = calculate_skill_score(resume_skills, job_skills)
    final_score = calculate_final_score(semantic_score,skill_score)
    recommendations = generate_recommendations(missing_skills,semantic_score,skill_score)
    resume_analysis = analyze_resume_structure(resume_text)

    return {
        "semantic_score": semantic_score,
        "skill_score": skill_score,
        "final_score": final_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_skills":resume_skills,
        "job_skills":job_skills,
        "recommendations":recommendations,
        "resume_analysis": resume_analysis
    }