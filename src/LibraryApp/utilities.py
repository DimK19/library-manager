from functools import reduce

replacement_pairs = [
    ('Ά', 'Α'),
    ('Έ', 'Ε'),
    ('Ή', 'Η'),
    ('Ί', 'Ι'),
    ('Ό', 'Ο'),
    ('Ύ', 'Υ'),
    ('Ώ', 'Ω')
]

def foo(s):
    return reduce(lambda x, pair: x.replace(*pair), replacement_pairs, s.upper())
