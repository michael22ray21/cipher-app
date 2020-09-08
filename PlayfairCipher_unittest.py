import unittest
from PlayfairCipher import PlayfairCipher

class PlayfairCipherTestCase(unittest.TestCase):
    def test_encrypt(self):
        key_string = "Jalan Ganesha Sepuluh"

        cipher = PlayfairCipher(key_string)

        plaintext = "Temui Ibu Nanti Malam"

        ciphertext = cipher.encrypt(plaintext)

        self.assertEqual(ciphertext, "ZBRSFYKUPGLGRKVSNLQV")

    def test_decrypt(self):
        key_string = "Jalan Ganesha Sepuluh"

        cipher = PlayfairCipher(key_string)

        ciphertext = "ZBRSFYKUPGLGRKVSNLQV"

        plaintext = cipher.decrypt(ciphertext)

        self.assertEqual(plaintext, "temuixibunantimalamx")

if __name__ == '__main__':
    unittest.main()
