class TrieNode:
    def __init__(self, letter, is_leaf=False, is_root=False):
        self.letter = letter
        self.is_leaf = is_leaf
        self.is_root = is_root
        self.children = {}

    def insert(self, word):
        if len(word) == 0:
            self.is_leaf = True
        else:
            first_char = word[0]
            if first_char not in self.children:
                self.children[first_char] = TrieNode(first_char)
            self.children[first_char].insert(word[1:])
