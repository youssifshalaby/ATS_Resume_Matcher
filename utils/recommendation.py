def generate_recommendations(missing_skills,semantic_score,skill_score):
    recommendations = []
    if missing_skills:
        recommendations.append(f"Consider adding these skills to your resume: {', '.join(missing_skills)}")

        # Semantic score analysis

    if semantic_score < 50:

        recommendations.append(
            "Your resume content is not strongly aligned with the job description. Try adding more relevant experience and project descriptions."
        )

    elif semantic_score < 75:

        recommendations.append(
            "Improve your resume wording to better match the job requirements."
        )

    # Skill score analysis

    if skill_score < 50:

        recommendations.append(
            "Your resume is missing many required skills. Focus on gaining and mentioning relevant technical skills."
        )

    elif skill_score < 75:

        recommendations.append(
            "Add more details about your experience with the required technologies."
        )


    if not recommendations:

        recommendations.append(
            "Excellent match! Your resume is strongly aligned with this job description."
        )


    return recommendations   