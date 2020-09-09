import CipherInterface
from VignereCipher import VignereCipher

def CharToInt(char) :
    if (char == 'A') : return 0
    elif (char == 'B') : return 1
    elif (char == 'C') : return 2
    elif (char == 'D') : return 3
    elif (char == 'E') : return 4
    elif (char == 'F') : return 5
    elif (char == 'G') : return 6
    elif (char == 'H') : return 7
    elif (char == 'I') : return 8
    elif (char == 'J') : return 9
    elif (char == 'K') : return 10
    elif (char == 'L') : return 11
    elif (char == 'M') : return 12
    elif (char == 'N') : return 13
    elif (char == 'O') : return 14
    elif (char == 'P') : return 15
    elif (char == 'Q') : return 16
    elif (char == 'R') : return 17
    elif (char == 'S') : return 18
    elif (char == 'T') : return 19
    elif (char == 'U') : return 20
    elif (char == 'V') : return 21
    elif (char == 'W') : return 22
    elif (char == 'X') : return 23
    elif (char == 'Y') : return 24
    elif (char == 'Z') : return 25
    else : return -1

def IntToChar(num) :
    while (num < 0 or 25 < num) : num = num % 26
    if (num == 0) : return 'A'
    elif (num == 1) : return 'B'
    elif (num == 2) : return 'C'
    elif (num == 3) : return 'D'
    elif (num == 4) : return 'E'
    elif (num == 5) : return 'F'
    elif (num == 6) : return 'G'
    elif (num == 7) : return 'H'
    elif (num == 8) : return 'I'
    elif (num == 9) : return 'J'
    elif (num == 10) : return 'K'
    elif (num == 11) : return 'L'
    elif (num == 12) : return 'M'
    elif (num == 13) : return 'N'
    elif (num == 14) : return 'O'
    elif (num == 15) : return 'P'
    elif (num == 16) : return 'Q'
    elif (num == 17) : return 'R'
    elif (num == 18) : return 'S'
    elif (num == 19) : return 'T'
    elif (num == 20) : return 'U'
    elif (num == 21) : return 'V'
    elif (num == 22) : return 'W'
    elif (num == 23) : return 'X'
    elif (num == 24) : return 'Y'
    elif (num == 25) : return 'Z'
    else : return ''

class AutoKeyVignereCipher(CipherInterface.StringCipher):
    """Auto-key Vignere cipher description here"""

    def __init__(self, key: str):
        self.key = key.upper()

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt a given bytearray, returning an encrypted string.
        Overrides StringCipher.encrypt()
        """
        self.key += plaintext.upper()
        return VignereCipher.encrypt(plaintext, self.key)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt a given bytearray, returning an plaintext string.
        Overrides StringCipher.decrypt()
        """
        plain_text = ''
        i = 0
        for a in ciphertext :
            plain_text += IntToChar(CharToInt(a) - CharToInt(self.key[i]))
            self.key += IntToChar(CharToInt(a) - CharToInt(self.key[i]))
            i += 1
        return plain_text
