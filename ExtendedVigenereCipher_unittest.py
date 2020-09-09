import unittest
from ExtendedVigenereCipher import ExtendedVigenereCipher

class ExtendedVigenereCipherTestCase(unittest.TestCase):
    def test_encrypt(self):
        key_binary = bytearray([1, 2, 3, 4, 5])

        cipher = ExtendedVigenereCipher(key_binary)

        plain_binary = bytearray([1, 2, 3, 4, 5])

        cipher_binary = cipher.encrypt(plain_binary)

        self.assertEqual(cipher_binary, bytearray([2, 4, 6, 8, 10]))

        plain_binary = bytearray([1, 2, 3, 4, 5, 6, 7])

        cipher_binary = cipher.encrypt(plain_binary)

        self.assertEqual(cipher_binary, bytearray([2, 4, 6, 8, 10, 7, 9]))

    def test_decrypt(self):
        key_binary = bytearray([1, 2, 3, 4, 5])

        cipher = ExtendedVigenereCipher(key_binary)

        cipher_binary = bytearray([2, 4, 6, 8, 10])

        plain_binary = cipher.decrypt(cipher_binary)

        self.assertEqual(plain_binary, bytearray([1, 2, 3, 4, 5]))

        cipher_binary = bytearray([2, 4, 6, 8, 10, 7, 9])

        plain_binary = cipher.decrypt(cipher_binary)

        self.assertEqual(plain_binary, bytearray([1, 2, 3, 4, 5, 6, 7]))

if __name__ == '__main__':
    unittest.main()
