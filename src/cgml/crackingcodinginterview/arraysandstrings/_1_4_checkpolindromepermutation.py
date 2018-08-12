def check_palindrome_permutation(s):
    if s is None: return False
    if len(s)<2: return True
    d = {}
    oddchars = set()
    for idx, c in enumerate(s):
        if c == ' ': continue
        d[c] = d.get(c,0)+1
        if d[c]%2 !=0:oddchars.add(c)
        else: oddchars.remove(c)

    return len(oddchars) <= 1

assert check_palindrome_permutation("aaa bb")
assert check_palindrome_permutation("aac bb")
assert not check_palindrome_permutation("aac bbe")