from nltk import word_tokenize
sentence = "Alice said she would arrive by noon."
tokens = word_tokenize(sentence)
references = {'she': 'Alice'}
resolved_sentence = " ".join([references.get(word, word) for word in tokens])
print("Resolved:", resolved_sentence)
