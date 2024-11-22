import spacy
nlp = spacy.load("en_core_web_sm")
def extract_noun_phrases(sentence):
    doc = nlp(sentence)
    return {chunk.text: chunk.root.text for chunk in doc.noun_chunks}
sentence = "The intelligent robot in the lab performed a complex task."
result = extract_noun_phrases(sentence)
for phrase, main_noun in result.items():
    print(f"{phrase}: {main_noun}")
