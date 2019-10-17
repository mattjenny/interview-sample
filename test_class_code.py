import class_code
from forbidden_words_trie import forbidden_words

num_lookup = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
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

def mock_random_sequence(seq):
    num_seq = []
    for char in seq:
        num_seq.append(num_lookup.index(char))
    num_seq.reverse()

    def get_random(m, n):
        return num_seq.pop()

    class_code.random.randrange = get_random


def test_forbidden_word():
    mock_random_sequence('RATSXYZ')
    code = class_code.generate_code()
    assert(code == 'RATXYZ')

def test_forbidden_word_non_consecutive():
    mock_random_sequence('R4A2TSQ')
    code = class_code.generate_code()
    assert(code == 'R4A2TQ')

def test_code_does_not_contain_forbidden_letters():
    mock_random_sequence('A1B0CLDIEOF')
    code = class_code.generate_code()
    assert(code == 'ABCDEF')

def test_all_forbidden_words():
    for word in forbidden_words:
        word = word.upper()
        # We'll have to get more clever if we add forbidden words ending in J
        mock_random_sequence(word + 'JJJJJJ')
        code = class_code.generate_code()
        remaining_length = 6 - (len(word) - 1)
        expected = word[:-1] + 'JJJJJJ'[:remaining_length]
        assert(code == expected)