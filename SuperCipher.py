import CipherInterface
from VignereCipher import VignereCipher

class SuperCipher(CipherInterface.StringCipher):
    """Super cipher description here"""

    def __init__(self, key: str):
        self.key = key
        self.vigenere_cipher = VignereCipher(key)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt a given bytearray, returning an encrypted string.
        Overrides StringCipher.encrypt()
        """
        vigenere_ciphertext = self.vigenere_cipher.encrypt(plaintext)

        plain_text = ''.join([i for i in vigenere_ciphertext.upper() if i.isalpha()])
        ncol = len(self.key)
        nrow = len(plain_text) // len(self.key) + 1

        if len(plain_text) < nrow * ncol :
            plain_text = plain_text + ''.join(['X' for i in range(nrow * ncol - len(plain_text))])

        mat = [['a' for i in range(ncol)] for i in range(nrow)]
        k = 0
        for i in range(nrow) :
            for j in range(ncol) :
                mat[i][j] = plain_text[k]
                k += 1

        cipher_text = ''
        for i in range(ncol) :
            for j in range(nrow) :
                cipher_text += mat[j][i]

        return cipher_text

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt a given bytearray, returning an plaintext string.
        Overrides StringCipher.decrypt()
        """
        cipher_text = ''.join([i for i in ciphertext.upper() if i.isalpha()])
        ncol = len(self.key)
        nrow = len(cipher_text) // len(self.key)
        mat = [['a' for i in range(ncol)] for i in range(nrow)]

        k = 0
        for i in range(ncol) :
            for j in range(nrow) :
                mat[j][i] = cipher_text[k]
                k += 1

        plain_text = ''
        for i in range(nrow) :
            for j in range(ncol) :
                plain_text += mat[i][j]

        plain_text = plain_text.rstrip('X')

        return self.vigenere_cipher.decrypt(plain_text)
