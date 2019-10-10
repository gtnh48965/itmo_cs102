import string

ord_islower_ind = {True: 97, False: 65}
alphabet_length = 26


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha():
            ciphertext += chr(
                (ord(letter) - ord_islower_ind[letter.islower()] + shift) % alphabet_length + ord_islower_ind[
                    letter.islower()])
        else:
            ciphertext += letter
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for letter in ciphertext:
        if letter.isalpha():
            plaintext += chr(
                (ord(letter) - ord_islower_ind[letter.islower()] - shift) % alphabet_length + ord_islower_ind[
                    letter.islower()])
        else:
            plaintext += letter
    return plaintext


if __name__ == '__main__':
    original = string.ascii_letters
    encrypted = encrypt_caesar(string.ascii_letters)
    decrypted = decrypt_caesar(encrypt_caesar(string.ascii_letters))

    print(original)
    print(encrypted)
    print(decrypted)
    print(f'Decrypted is equal to orig: {original == decrypted}')
