import re
expression = "forall x (Human(x) -> Mortal(x))"
variables = re.findall(r"\b\w+\b", expression)
predicates = re.findall(r"\b[A-Z][a-zA-Z]*\b", expression)
connectives = re.findall(r"[->&|]", expression)
quantifiers = re.findall(r"\bforall\b|\bexists\b", expression)
print("Variables:", variables, "\nPredicates:", predicates, "\nConnectives:", connectives, "\nQuantifiers:", quantifiers)
