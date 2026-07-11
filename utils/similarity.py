from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_embedding,job_embedding):
    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    return float(round(similarity *100,2))
