def encrypt(plain_text, key):
    chars = list(plain_text)
    encrypted_codepoints = [ord(c) ^ key for c in chars]
    return encrypted_codepoints 

def decrypt(encrypted_codepoints, key):
    return [chr(e ^ key) for e in encrypted_codepoints]
