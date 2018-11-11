'''
Knuth-Morris-Pratt: Substring search

Clever method to avoid backups. Builds deterministic finite machine for substring searching

Based on Deterministic Finite Automata
'''
from collections import Counter

a = Counter('abcad')
b = Counter('acadb')