import CipherInterface

BYTE_MAX = 256

class ExtendedVigenereCipher(CipherInterface.BinaryCipher):
    """Extended Vignere cipher works by shifting chunks of characters in plaintext
    by the key's characters decimal representation"""

    def __init__(self, key_binary: bytearray):
        self.key = key_binary

    def encrypt(self, plain_binary: bytearray) -> bytearray:
        """
        Encrypt a given bytearray, returning an encrypted bytearray.
        Overrides BinaryCipher.encrypt()
        """
        cipher_binary = bytearray(len(plain_binary))

        for idx, symbol in enumerate(plain_binary):
            cipher_binary[idx] = (symbol + self.key[idx % len(self.key)]) % BYTE_MAX

        return cipher_binary

    def decrypt(self, cipher_binary: bytearray) -> bytearray:
        """
        Decrypt a given bytearray, returning an plaintext bytearray.
        Overrides StringCipher.decrypt()
        """
        pass
        plain_binary = bytearray(len(cipher_binary))

        for idx, symbol in enumerate(cipher_binary):
            plain_binary[idx] = (symbol - self.key[idx % len(self.key)]) % BYTE_MAX

        return plain_binary
