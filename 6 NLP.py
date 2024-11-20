import random
text = "this is a bigram model for text generation"
bigrams = {text.split()[i]: text.split()[i + 1] for i in range(len(text.split()) - 1)}
word, n = "bigram", 10
print(' '.join([word := random.choice([bigrams.get(word, '')]) for _ in range(n) if word]))
