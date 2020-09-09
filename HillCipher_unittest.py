import unittest
from HillCipher import HillCipher

class HillCipherTestCase(unittest.TestCase):
    def test_encrypt(self):
        key = [
            [17, 17, 5],
            [21, 18, 21],
            [2, 2, 19]
        ]

        cipher = HillCipher(key)

        plaintext = "paymoremoney"

        ciphertext = cipher.encrypt(plaintext)

        self.assertEqual(ciphertext, "LNSHDLEWMTRW")

        key = [
            [1, 5],
            [3, 4],
        ]

        cipher = HillCipher(key)

        plaintext = "kucingunyu"

        ciphertext = cipher.encrypt(plaintext)

        self.assertEqual(ciphertext, "GGQMRLHIUW")

    def test_decrypt(self):
        key = [
            [17, 17, 5],
            [21, 18, 21],
            [2, 2, 19]
        ]

        cipher = HillCipher(key)

        ciphertext = "LNSHDLEWMTRW"

        plaintext = cipher.decrypt(ciphertext)

        self.assertEqual(plaintext, "paymoremoney")

        key = [
            [1, 5],
            [3, 4],
        ]

        cipher = HillCipher(key)

        ciphertext = "GGQMRLHIUW"

        plaintext = cipher.decrypt(ciphertext)

        self.assertEqual(plaintext, "kucingunyu")

if __name__ == '__main__':
    unittest.main()
