def fsa_accepts(s):
    state = 'q0'
    for c in s:
        state = {'q0': {'a': 'q1', 'b': 'q0'},
                 'q1': {'a': 'q1', 'b': 'q2'},
                 'q2': {'a': 'q1', 'b': 'q0'}}[state].get(c, 'q0')
    return state == 'q2'
print([f"'{s}': {'Accepted' if fsa_accepts(s) else 'Rejected'}" for s in ['ab', 'aab', 'b', 'abab', 'abc', 'babab']])
