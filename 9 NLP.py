import re
rules = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'\bthe\b', 'DT'), (r'\bI\b', 'PRP'), (r'\d+', 'CD')]
def pos_tag(sentence):
    return [(word, next((tag for pattern, tag in rules if re.fullmatch(pattern, word)), 'NN')) for word in sentence.split()]
print(pos_tag("The quick dog is running"))
