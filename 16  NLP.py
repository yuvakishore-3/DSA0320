import spacy
nlp = spacy.load("en_core_web_sm")
text = "Barack Obama was born in Hawaii and was the President of the United States."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
