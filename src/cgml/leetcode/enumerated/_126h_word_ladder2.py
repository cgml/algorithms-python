from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def findLadders(self, begin, end, words):
        if end not in words: return []
        front, back = {begin: [[begin]]}, {end: [[end]]}
        fwords, ewords = set(words), set(words)
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                fwords, ewords = ewords, fwords
            hold = defaultdict(list)
            toDel, res = set(), []
            for wd, pths in front.items():
                nxts = fwords & {wd[:i] + c + wd[i + 1:] for i in range(len(wd)) for c in ascii_lowercase}
                toDel |= nxts
                for w in nxts:
                    for pth in pths:
                        if w in back:
                            if pth[0] == begin:
                                res += [pth + bk[::-1] for bk in back[w]]
                            else:
                                res += [bk + pth[::-1] for bk in back[w]]
                        hold[w].append(pth + [w])
            if res: return res
            front = hold
            fwords -= toDel
        return []
