from nltk import CFG
from nltk.parse import RecursiveDescentParser
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'cats' | 'dogs'
    V -> 'chases' | 'chase'
""")
parser = RecursiveDescentParser(grammar)
def check_sentence(sentence):
    words = sentence.lower().split()
    try:
        trees = list(parser.parse(words))
        if trees:
            print("The sentence is grammatically valid.")
            for tree in trees:
                print(tree) 
        else:
            print("The sentence does not conform to the grammar.")
    except ValueError as e:
        print(f"Error in parsing: {e}")
sentence = "The cat chases a dog"
check_sentence(sentence)
