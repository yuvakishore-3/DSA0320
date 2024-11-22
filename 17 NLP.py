import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn
word = "dog"
synsets = wn.synsets(word)
if synsets:
    for syn in synsets:
        print("Synset:", syn.name())
        print("Definition:", syn.definition())
        print("Examples:", syn.examples())
        print()
else:
    print(f"No synsets found for the word '{word}'.")
