from utils.models import embedding_model


def get_embedding(text):
    return embedding_model.encode(text,convert_to_numpy=True,normalize_embeddings=True)
