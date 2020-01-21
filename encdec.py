"""
encrypt:

    >>> encrypt("hello", 0b101111100011)
    [2955, 2950, 2959, 2959, 2956]

    >>> encrypt("hello", 4) # `key` with non binary format
    [108, 97, 104, 104, 107]

    >>> encrypt("hello", 'key') # `key` with non int value
    Traceback (most recent call last):
        ...
    TypeError: key is expected to be `int`

    >>> encrypt(1, 0b101111100011) # `plain_text` is not string
    Traceback (most recent call last):
        ...
    TypeError: plain_text is expected to be `str`

decrypt:

    >>> decrypt([2955, 2950, 2959, 2959, 2956], 0b101111100011)
    ['h', 'e', 'l', 'l', 'o']

    >>> decrypt([], 0b101111100011) # empty list
    []

    >>> decrypt('not list', 0b101111100011) # not list
    Traceback (most recent call last):
        ...
    TypeError: encrypted_codepoints is expected to be `list`

    >>> decrypt([2955, 2950, 2959, 2959, 2956], 'a') # invalid key
    Traceback (most recent call last):
        ...
    TypeError: key is expected to be `int`

"""

# 内部処理的にはすべて int だから二進数表記を気にするのは入出力のときだけにする
def encrypt(plain_text, key):
    if not type(plain_text) is str:
        raise TypeError('plain_text is expected to be `str`')
    if not type(key) is int:
        raise TypeError('key is expected to be `int`')

    return [ord(c) ^ key for c in plain_text]

def show_encrypted_codepoints(codepoints, format_string='#b'):
    print([format(c, format_string) for c in codepoints])

def decrypt(encrypted_codepoints, key):
    if not type(encrypted_codepoints) is list:
        raise TypeError('encrypted_codepoints is expected to be `list`')
    if not type(key) is int:
        raise TypeError('key is expected to be `int`')

    return [chr(e ^ key) for e in encrypted_codepoints]

def show_decrypted_letters(letters):
    print(''.join(letters))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
