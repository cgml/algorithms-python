'''
Copyright 2018 Constantine Gurnov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

'''
Knuth-Morris-Pratt
Substring Search
Time Complexity: O(n)

'''

from collections import defaultdict
def substring(s, p):
    if len(s) < len(p): return -1
    M, pset, dfa, idx, j = len(p), set(p), getdfa(p), 0, 0
    while idx < len(s) and j < M: j, idx = 0 if s[idx] not in pset else dfa[j][s[idx]], idx+1
    return idx-M if j == M else -1

def getdfa(p):
    dfa = defaultdict(dict)
    for c in p: dfa[0][c] = 0
    dfa[0][p[0]], x, j = 1, 0, 1
    while j < len(p):
        for c in p: dfa[j][c] = dfa[x][c]
        dfa[j][p[j]] = j + 1
        x, j = dfa[x][p[j]], j + 1
    return dfa

print(substring("BBBBBBBBBBBAABABAC","ABABAC"))
print(substring("BBBBBBBBBBBAABABAC","ABABACK"))