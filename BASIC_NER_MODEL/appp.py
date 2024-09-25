import streamlit as st
import spacy

# Load the fine-tuned model
nlp = spacy.load("fine_tuned_model")

# Streamlit input
text = st.text_area("Enter Medical Text:")

if st.button("Extract Entities"):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    st.write(entities)
