import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn

sentence = "I went to the bank to deposit money"
words = nltk.word_tokenize(sentence)
for word in words:
    synset = lesk(words, word)
    if synset:
        print(word, "-", synset.definition())
