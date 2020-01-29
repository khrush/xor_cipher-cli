"""
encrypt:

    >>> encrypt("hello", "world")
    [31, 10, 30, 0, 11]

    >>> encrypt("aaaaaa", "wo") # `key` repeats when the key is shorter than plain_text
    [22, 14, 22, 14, 22, 14]

    >>> encrypt("aa", "wonderful world") # use first 2 letters of `key` and forget the rest when the key is longer than 2 letters of plain_text
    [22, 14]

    >>> encrypt(1, "wo") # `plain_text` is not str
    Traceback (most recent call last):
        ...
    TypeError: plain_text is expected to be `str`

    >>> encrypt("hello", 1) # `key` is not str
    Traceback (most recent call last):
        ...
    TypeError: key is expected to be `str`

decrypt:

    >>> decrypt([31, 10, 30, 0, 11], "world")
    ['h', 'e', 'l', 'l', 'o']

    >>> decrypt([22, 14, 22, 14, 22, 14], "wo") # key is shorter than list size
    ['a', 'a', 'a', 'a', 'a', 'a']

    >>> decrypt([22, 14], "wonderful world") # key is longer than list size
    ['a', 'a']

    >>> decrypt([], "wo") # empty list
    []

    >>> decrypt('not list', "wo") # encrypted_codepoints is not list
    Traceback (most recent call last):
        ...
    TypeError: encrypted_codepoints is expected to be `list`

    >>> decrypt([22, 14], 1) # key is not str
    Traceback (most recent call last):
        ...
    TypeError: key is expected to be `str`

"""
from itertools import cycle

# 内部処理的にはすべて int だから二進数表記を気にするのは入出力のときだけにする
def encrypt(plain_text, key):
    if not type(plain_text) is str:
        raise TypeError('plain_text is expected to be `str`')
    if not type(key) is str:
        raise TypeError('key is expected to be `str`')

    return [ord(c) ^ ord(k)  for c, k in zip(plain_text, cycle(key))]

def show_encrypted_codepoints(codepoints, format_string='#b'):
    print([format(c, format_string) for c in codepoints])

def decrypt(encrypted_codepoints, key):
    if not type(encrypted_codepoints) is list:
        raise TypeError('encrypted_codepoints is expected to be `list`')
    if not type(key) is str:
        raise TypeError('key is expected to be `str`')

    return [chr(e ^ ord(k)) for e, k in zip(encrypted_codepoints, cycle(key))]        

def show_decrypted_letters(letters):
    print(''.join(letters))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
