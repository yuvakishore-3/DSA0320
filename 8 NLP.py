from collections import defaultdict, Counter
data = [("The", "DT"), ("dog", "NN"), ("barked", "VB")]
model = defaultdict(Counter)
for word, tag in data:
    model[word][tag] += 1
def tag_sentence(sentence):
    return [(word, max(model[word], key=model[word].get, default="NN")) for word in sentence.split()]
print(tag_sentence("The dog barked"))
