class Parser:
    def __init__(self, grammar, start): self.g, self.s = grammar, start
    def parse(self, tokens): 
        self.tokens, self.index = tokens, 0
        return self._m(self.s) and self.index == len(tokens)
    def _m(self, sym):
        if self.index >= len(self.tokens): return False
        if sym not in self.g:  
            if self.index < len(self.tokens) and self.tokens[self.index] == sym:
                self.index += 1
                return True
            return False
        for rule in self.g[sym]:
            saved_index = self.index
            if all(self._m(s) for s in rule): return True
            self.index = saved_index
        return False
grammar = {"S": [["a", "S", "b"], ["a", "b"]]}
parser = Parser(grammar, "S")
inputs = [["a", "b"], ["a", "a", "b", "b"], ["a", "a", "b"], ["a", "b", "b"]]
for tokens in inputs:
    print(f"{tokens} => {'Accepted' if parser.parse(tokens) else 'Rejected'}")
