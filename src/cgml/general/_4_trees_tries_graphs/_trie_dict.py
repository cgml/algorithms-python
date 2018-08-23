

class TrieDict:
    _END = '*'

    def __init__(self,words,trie=None):
        if trie: root = trie.trie.copy()
        else: root = {}
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
                current_dict[self._END] = self._END
        self.trie = root

    def exists(self, prefix):
        def exists_helper(trie, prefix):
            if not prefix: return True
            return self.trie.get(prefix[0]) is not None and exists_helper(trie[prefix[0]], prefix[1:])
        return exists_helper(self.trie, prefix)

    def find_max_prefix(self, prefix):
        def find_max_prefix_helper(trie, prefix):
            if not prefix or trie.get(prefix[0]) is None: return ""
            if len(prefix) == 1: return prefix[0]
            return "{}{}".format(prefix[0], find_max_prefix_helper(trie[prefix[0]], prefix[1:]))
        return find_max_prefix_helper(self.trie, prefix)



trie = TrieDict(['foo', 'bar', 'baz', 'barz'])
print (trie.trie)
print(trie.exists("foo"))
print(trie.exists("fogar"))
print(trie.find_max_prefix('foo'))
print(trie.find_max_prefix('fogar'))
trie = TrieDict(['fogar'],trie)
print(trie.find_max_prefix('fogar'))