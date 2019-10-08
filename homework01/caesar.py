def encrypt_caesar(plaintext: str) -> str:
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
    # PUT YOUR CODE HERE
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
    return ''.join([chr(((ord(l) - ord_islower_ind[l.islower()]) - shift) % 26 + ord_islower_ind[l.islower()]) if l.isalpha() else l for l in ciphertext])
