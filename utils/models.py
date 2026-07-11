import streamlit as st
import spacy
from sentence_transformers import SentenceTransformer


@st.cache_resource
def load_spacy_model():

    return spacy.load(
        "en_core_web_sm",
        disable=[
            "parser",
            "ner"
        ]
    )


@st.cache_resource
def load_embedding_model():

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


nlp = load_spacy_model()

embedding_model = load_embedding_model()
