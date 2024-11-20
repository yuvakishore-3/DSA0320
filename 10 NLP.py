import re
def tag_sentence(sentence):
    rules = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'\bthe\b', 'DT')]
    tagged = [(w, next((t for p, t in rules if re.fullmatch(p, w)), 'NN')) for w in sentence.split()]
    return [(w, 'JJ' if t == 'DT' and tagged[i+1][1] == 'NN' else t) for i, (w, t) in enumerate(tagged)]
print(tag_sentence("The dog is running"))
