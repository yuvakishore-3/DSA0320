from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["running", "happier", "cats", "studies", "better", "flying"]
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
