from utils.embedding import get_embedding
from utils.similarity import calculate_similarity

resume = """
Python
SQL
TensorFlow
Machine Learning
"""

job = """
Looking for Machine Learning Engineer.

Skills:
Python
SQL
TensorFlow
"""

resume_embedding = get_embedding(resume)
job_embedding = get_embedding(job)

print(calculate_similarity(resume_embedding,job_embedding))