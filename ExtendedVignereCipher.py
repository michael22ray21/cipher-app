import CipherInterface

class ExtendedVignereCipher(CipherInterface.BinaryCipher):
    """Extended Vignere cipher description here"""

    def __init__(self):
        pass

    def encrypt(self, plain_binary: bytearray) -> bytearray:
        """
        Encrypt a given bytearray, returning an encrypted bytearray.
        Overrides BinaryCipher.encrypt()
        """
        pass

    def decrypt(self, cipher_binary: bytearray) -> bytearray:
        """
        Decrypt a given bytearray, returning an plaintext bytearray.
        Overrides StringCipher.decrypt()
        """
        pass
