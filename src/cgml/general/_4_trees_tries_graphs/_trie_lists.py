from typing import Tuple

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.complete = False
        self.counter = 1 # number of words which have this prefix

class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def add(self, word: str):
        node = self.root
        for char in word.lower():
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    child.counter += 1
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.complete = True


    def find_prefix(self, prefix: str) -> Tuple[bool, int]:
        node = self.root
        if not node.children: return False, 0
        for char in prefix:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, 0
        return True, node.counter


trie = Trie()
trie.add('abc')
trie.add("abcdef")
trie.add('bcdef')

print(trie.find_prefix('abc'))
print(trie.find_prefix('abcd'))
print(trie.find_prefix('abcdt'))
