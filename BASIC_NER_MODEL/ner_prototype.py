import spacy
from spacy.training import Example

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Training data with medical entities
TRAIN_DATA = [
    ("The patient was diagnosed with Diabetes.", {"entities": [(29, 37, "DISEASE")]}),
    ("He was prescribed Metformin.", {"entities": [(16, 25, "DRUG")]}),
    ("John has Hypertension and takes Amlodipine.", {"entities": [(9, 21, "DISEASE"), (32, 43, "DRUG")]}),
    ("The doctor found the patient had Asthma.", {"entities": [(32, 38, "DISEASE")]}),
    ("The diagnosis was Chronic Obstructive Pulmonary Disease.", {"entities": [(18, 54, "DISEASE")]}),
    ("She was given Ibuprofen for pain relief.", {"entities": [(13, 22, "DRUG")]}),
    ("The patient was diagnosed with Diabetes and prescribed Metformin.", {"entities": [(34, 42, "DISEASE"), (51, 60, "DRUG")]}),
]

# Adding the 'DISEASE' and 'DRUG' labels to the NER model
ner = nlp.get_pipe("ner")
ner.add_label("DISEASE")
ner.add_label("DRUG")

# Disable other components of the pipeline to only train NER
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.resume_training()
    
    # Training loop
    for epoch in range(20):  # Train for 20 iterations
        losses = {}
        for text, annotations in TRAIN_DATA:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.35, losses=losses)
        print(f"Epoch {epoch} Losses: {losses}")

# Save the fine-tuned model
nlp.to_disk("fine_tuned_model")
print("Model trained and saved as 'fine_tuned_model'")
