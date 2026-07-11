from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy

class SemanticMatcher:

    def __init__(self, skills):
        self.nlp = spacy.load("en_core_web_sm")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.skills = skills

        self.skill_embeddings = {}

        for skill in skills.keys():

            self.skill_embeddings[skill] = self.model.encode(skill)
    
    def split_text(self,text):
        doc = self.nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 2]
        return sentences
    
    def extract(self, text, threshold=0.60):

        sentences = self.split_text(text)
        if not sentences:
            return []
        
        sentence_embeddings = self.model.encode(sentences)
        found = []

        for skill, embedding in self.skill_embeddings.items():

            similarities  = cosine_similarity(
                sentence_embeddings,
                [embedding]
            )
            max_similarity = np.max(similarities)

            if max_similarity >= threshold:

                found.append(skill)

        return sorted(found)