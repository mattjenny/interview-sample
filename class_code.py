import random
from forbidden_words_trie import forbidden_words_trie

CODE_LENGTH = 6
ALPHABET = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]

def random_character():
    # Start at 2 to always exclude 0 and 1
    n = random.randrange(2, 36)
    if n > 9:
        return ALPHABET[n - 10]
    else:
        return '%i' % n

def get_valid_letter(forbidden_roots):
    while True:
        valid_letter = True
        letter = random_character()
        for node in forbidden_roots:
            if letter in node.children and node.children[letter].is_leaf:
                valid_letter = False
        if valid_letter:
            return letter

def generate_code():
    # Keep track of prefixes of forbidden words that we've seen
    forbidden_roots = set([forbidden_words_trie])
    code = ''
    for i in range(CODE_LENGTH):
        letter = get_valid_letter(forbidden_roots)

        # Add any new forbidden word prefixes that this letter matches
        # E.g., if we add a "C" and then an "H", we have seen prefixes
        # "CH" (for 'cheese') and "H" (for 'haha').
        to_add = []
        for node in forbidden_roots:
            if letter in node.children:
                to_add.append(node.children[letter])

        for node in to_add:
            forbidden_roots.add(node)
        
        code = code + letter
    
    return code

def generate_codes(num_codes):
    codes = []
    for i in range(num_codes):
        codes.append(generate_code())

    return codes
