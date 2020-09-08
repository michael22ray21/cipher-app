import CipherInterface
from pymatrix import Matrix

class HillCipher(CipherInterface.StringCipher):
    """Hill cipher description here"""

    def __init__(self, key: list = None):
        if not key:
            key = Matrix.identity(3)

        self.key_matrix = Matrix.from_list(key)

        try:
            determinant_modulus_inverse = pow(round(self.key_matrix.det()), -1, 26)
            self.key_matrix_inverse = (determinant_modulus_inverse * self.key_matrix.adjoint()) % 26
        except:
            raise Exception("Key matrix have to be modular inversible")

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt a given string, returning an encrypted string.
        Overrides StringCipher.encrypt()
        """
        no_space_plaintext = plaintext.replace(" ", "")

        if not no_space_plaintext.isalpha():
            raise Exception("Hill cipher only accept alphabets with or without spaces as plaintext")

        lowercase_plaintext = no_space_plaintext.lower()

        plaintext_mod_26_list = [ord(char) - ord('a') for char in lowercase_plaintext]

        ciphertext_mod_26_list = []

        block = self.key_matrix.numcols

        offset = 0
        while offset < len(plaintext_mod_26_list):
            plaintext_slice = None
            if len(plaintext_mod_26_list) - offset < block:
                padding = [0 for x in range(len(plaintext_mod_26_list), offset+block)]
                plaintext_slice = plaintext_mod_26_list[offset:len(plaintext_mod_26_list)] + padding
                
            else:
                plaintext_slice = plaintext_mod_26_list[offset:offset+block]

            plaintext_matrix_block = Matrix.from_list([[x] for x in plaintext_slice])

            ciphertext_matrix_block = self.key_matrix * plaintext_matrix_block

            for x in ciphertext_matrix_block.elements():
                ciphertext_mod_26_list.append(x % 26)

            offset += block

        ciphertext = ''.join([chr(x + ord('a')) for x in ciphertext_mod_26_list]).upper()

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt a given string, returning a plaintext string.
        Overrides StringCipher.decrypt()
        """

        if not ciphertext.isalpha():
            raise Exception("Hill cipher only accept alphabets as ciphertext")

        lowercase_ciphertext = ciphertext.lower()

        ciphertext_mod_26_list = [ord(char) - ord('a') for char in lowercase_ciphertext]

        plaintext_mod_26_list = []

        block = self.key_matrix.numcols

        offset = 0
        while offset < len(ciphertext_mod_26_list):
            ciphertext_slice = None

            if len(ciphertext_mod_26_list) - offset < block:
                padding = [0 for x in range(len(ciphertext_mod_26_list), offset+block)]
                ciphertext_slice = ciphertext_mod_26_list[offset:len(ciphertext_mod_26_list)] + padding
            else:
                ciphertext_slice = ciphertext_mod_26_list[offset:offset+block]

            ciphertext_matrix_block = Matrix.from_list([[x] for x in ciphertext_slice])

            plaintext_matrix_block = self.key_matrix_inverse * ciphertext_matrix_block

            for x in plaintext_matrix_block.elements():
                plaintext_mod_26_list.append(round(x) % 26)

            offset += block

        plaintext = ''.join([chr(x + ord('a')) for x in plaintext_mod_26_list])

        return plaintext
