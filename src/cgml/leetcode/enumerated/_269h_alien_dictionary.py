class Solution(object):
    def alienOrder(self, words):
        edges = []
        for pair in zip(words,words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    edges += a + b,
                    break
        chars, order = set(''.join(words)), []
        while edges:
            cur_roots_neg = set(list(zip(*edges))[1])
            current_roots = chars - cur_roots_neg
            if not current_roots: return ''
            order += current_roots
            edges = [edge for edge in edges if current_roots.isdisjoint(edge)]
            chars -= current_roots
        return ''.join(order + list(chars))

print(Solution().alienOrder( [ "wrt", "wrf", "er", "ett", "rftt" ]), "=?", "wertf")