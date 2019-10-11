import string

ord_islower_ind = {True: 97, False: 65}
alphabet_length = 26


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    keyword = keyword.lower()
    ciphertext = ''
    for let_ind, letter in enumerate(plaintext):
        if letter.isalpha():
            _shift = ord(keyword[let_ind % len(keyword)]) - ord_islower_ind[True]
            ciphertext += chr(
                (ord(letter) - ord_islower_ind[letter.islower()] + _shift) % alphabet_length + ord_islower_ind[
                    letter.islower()])
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    keyword = keyword.lower()
    plaintext = ''
    for let_ind, letter in enumerate(ciphertext):
        if letter.isalpha():
            _shift = ord(keyword[let_ind % len(keyword)]) - ord_islower_ind[True]
            plaintext += chr(
                (ord(letter) - ord_islower_ind[letter.islower()] - _shift) % alphabet_length + ord_islower_ind[
                    letter.islower()])
        else:
            plaintext += letter
    return plaintext


if __name__ == '__main__':
    original = string.ascii_letters
    key = 'ACEHKSPZKYREMBZQQSL'
    encrypted = encrypt_vigenere(original, key)
    decrypted = decrypt_vigenere(encrypted, key)

    print(original)
    print(encrypted)
    print(decrypted)
    print(f'Decrypted is equal to orig: {original == decrypted}')
