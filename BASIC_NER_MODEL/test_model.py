import spacy

# Load the fine-tuned NER model
nlp = spacy.load("fine_tuned_model")  # Change to your model path


# Test the model with an example text
text = "The patient was diagnosed with Diabetes and prescribed Metformin."
doc = nlp(text)

# Print the extracted entities
for ent in doc.ents:
    print(f"Entity: {ent.text} - Label: {ent.label_}")
