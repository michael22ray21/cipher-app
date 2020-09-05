import CipherInterface

class FullKeyVignereCipher(CipherInterface.StringCipher):
    """Full-key Vignere cipher description here"""

    def __init__(self):
        pass

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt a given bytearray, returning an encrypted string.
        Overrides StringCipher.encrypt()
        """
        pass

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt a given bytearray, returning an plaintext string.
        Overrides StringCipher.decrypt()
        """
        pass
