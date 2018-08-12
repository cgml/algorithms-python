def firstNonRepeatCharacter(s):
    chars = {}
    nonrepeating = []
    for c in s:
        counts = chars.get(c,0)
        if counts == 0: nonrepeating.append(c)
        else:
            if c in nonrepeating: nonrepeating.remove(c)
        chars[c]=counts+1
    if len(nonrepeating) > 0: return nonrepeating[0]
    else: return "_"


assert firstNonRepeatCharacter("abacabad") == "c"
assert firstNonRepeatCharacter("abacabcadd") == "_"
