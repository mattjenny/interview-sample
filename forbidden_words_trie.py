from trie_node import TrieNode

forbidden_words = [
    'darn',
    'rats',
    'egg',
    'fuzzy',
    'kthx',
    'haha',
    'ugh',
    '777',
    'cheese',
    'i',
    'l',
    'o',
    '0',
    '1'
]

forbidden_words_trie = TrieNode('', False, True)
for word in forbidden_words:
    forbidden_words_trie.insert(word.upper())
