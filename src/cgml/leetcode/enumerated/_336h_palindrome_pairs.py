class Solution:
    def palindromePairs(self, words):
        trie = {}
        p = {}
        empty_word = -1
        for widx, word in enumerate(words):  # O(W)
            d = trie
            if len(word) == 0: empty_word = widx
            rword = ''.join(list(reversed(list(word))))
            for idx, c in enumerate(rword):  # O(K)
                dc = d.get(c, {})
                tail = rword[idx+1:]
                if p.get(tail) is None: p[tail] = self._palindrome(tail)  # O(K)
                dc['**'] = dc.get('**', [])
                dc['ps'] = dc.get('ps', [])
                if idx == len(word) - 1: dc['**'].append(widx)
                if p[tail]: dc['ps'].append(widx)
                d[c]=dc
                d = dc


        result = set()
        for widx, word in enumerate(words):  # O(W)
            d = trie
            for idx, c in enumerate(word):  # O(K)
                d = d.get(c, None)
                if not d: break
                # case 1 - word exhasted. check remaining tails
                if idx == len(word) - 1:
                    for t in d.get('ps',[]):
                        if widx != t: result.add((widx, t))

                # case 2 - if remaining part of the word is polindrome - check
                else:
                    tail = word[idx+1:]
                    if p.get(tail, None) is None: p[tail] = self._palindrome(tail)
                    if p[tail]:
                        for t in d.get('**',[]):
                            if widx != t: result.add((widx, t))

        if empty_word >= 0:
            for idx, word in enumerate(words):
                if idx != empty_word and self._palindrome(word):
                    result.add((empty_word, idx))
                    result.add((idx, empty_word))

        result = [list(v) for v in sorted(result)]
        return result

    def _palindrome(self, word):
        if not word: return True
        l, r = 0, len(word) - 1
        while l < r and word[l] == word[r]: l, r = l + 1, r - 1
        return word[l] == word[r]

print('Actual  ', Solution().palindromePairs(["a","abc","aba",""]))
print('Expected', [[0,3],[3,0],[2,3],[3,2]])
print('Actual  ', Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))
print('Expected', [[0,1],[1,0],[3,2],[2,4]])
