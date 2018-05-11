def isCryptSolutionA(crypt,solution):
    cr = ["".join([dict(solution)[c] for c in x]) for x in crypt]
    #return int(cr[0]) + int(cr[1]) == int(cr[2]) and sum([1 for c in cr if len(str((int(c)))) == len(c)]) == 3
    return int(cr[0]) + int(cr[1]) == int(cr[2]) and sum([1 for c in cr if not c.startswith("0")]) == 3


def isCryptSolutionB(crypt, S):
    s = {}
    for v in S:
        s[v[0]]=int(v[1])
    def extract_num(word, solution):
        if solution[word[0]] == 0 and len(word)>1:
            return None
        return sum([v * 10 ** (len(word)-p-1) for p, v in enumerate([solution[c] for c in word])])
    result = [extract_num(c, s) for c in crypt]
    return False if None in result else result[0] + result[1] == result[2]


crypt1 = ["SEND", "MORE", "MONEY"]
solution1 = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

crypt2 = ["TEN", "TWO", "ONE"]
solution2 = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]

assert isCryptSolutionA(crypt1, solution1)
assert not isCryptSolutionA(crypt2, solution2)

assert isCryptSolutionB(crypt1, solution1)
assert not isCryptSolutionB(crypt2, solution2)
