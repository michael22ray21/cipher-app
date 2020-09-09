import CipherInterface
import string

ROW_COUNT = 5
COLUMN_COUNT = 5

def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)

class PlayfairCipher(CipherInterface.StringCipher):
    """Playfair cipher description here"""

    def __init__(self, key_string: str):
        no_space_key = key_string.replace(" ", "")

        if not no_space_key.isalpha():
            raise Exception("Playfair cipher only accept alphabets with or without spaces as key")

        lowercase_key = no_space_key.lower()

        self.key_table = []

        for char in lowercase_key:
            if char == 'j':
                continue

            if char in self.key_table:
                continue

            self.key_table.append(char)

        for char in string.ascii_lowercase:
            if char == 'j':
                char = 'i'

            if char in self.key_table:
                continue

            self.key_table.append(char)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt a given string, returning an encrypted string.
        Overrides StringCipher.encrypt()
        """
        no_space_plaintext = plaintext.replace(" ", "")

        if not no_space_plaintext.isalpha():
            raise Exception("Playfair cipher only accept alphabets with or without spaces as plaintext")

        lowercase_plaintext = no_space_plaintext.lower()

        processed_plaintext = []

        last_char = ""
        for char in lowercase_plaintext:
            if char == 'j':
                char = 'i'

            if char == last_char:
                processed_plaintext.append('x')

            processed_plaintext.append(char)

            last_char = char

        if len(processed_plaintext) % 2 == 1:
            processed_plaintext.append('x')

        ciphertext_list = []

        for char_1, char_2 in grouped(processed_plaintext, 2):
            char_1_index = self.key_table.index(char_1)
            char_2_index = self.key_table.index(char_2)

            char_1_encrypted = ""
            char_2_encrypted = ""

            # Same row
            if (char_1_index // COLUMN_COUNT) == (char_2_index // COLUMN_COUNT):
                char_1_encrypted = self.key_table[(char_1_index // COLUMN_COUNT) + ((char_1_index + 1) % COLUMN_COUNT)]
                char_2_encrypted = self.key_table[(char_2_index // COLUMN_COUNT) + ((char_2_index + 1) % COLUMN_COUNT)]

            # Same column
            elif (char_1_index % COLUMN_COUNT) == (char_2_index % COLUMN_COUNT):
                char_1_encrypted = self.key_table[(char_1_index + COLUMN_COUNT) % len(self.key_table)]
                char_2_encrypted = self.key_table[(char_2_index + COLUMN_COUNT) % len(self.key_table)]

            elif (char_1_index % COLUMN_COUNT) > (char_2_index % COLUMN_COUNT):
                column_difference = (char_1_index % COLUMN_COUNT) - (char_2_index % COLUMN_COUNT)

                char_1_encrypted = self.key_table[char_1_index - column_difference]
                char_2_encrypted = self.key_table[char_2_index + column_difference]

            elif (char_1_index % COLUMN_COUNT) < (char_2_index % COLUMN_COUNT):
                column_difference = (char_2_index % COLUMN_COUNT) - (char_1_index % COLUMN_COUNT)

                char_1_encrypted = self.key_table[char_1_index + column_difference]
                char_2_encrypted = self.key_table[char_2_index - column_difference]

            ciphertext_list.append(char_1_encrypted)
            ciphertext_list.append(char_2_encrypted)

        return ''.join(ciphertext_list).upper()

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt a given string, returning an plaintext string.
        Overrides StringCipher.decrypt()
        """
        if not ciphertext.isalpha():
            raise Exception("Playfair cipher only accept alphabets as ciphertext")

        lowercase_ciphertext = ciphertext.lower()

        processed_plaintext_list = []

        for char_1, char_2 in grouped(lowercase_ciphertext, 2):
            char_1_index = self.key_table.index(char_1)
            char_2_index = self.key_table.index(char_2)

            char_1_decrypted = ""
            char_2_decrypted = ""

            # Same row
            if (char_1_index // COLUMN_COUNT) == (char_2_index // COLUMN_COUNT):
                char_1_decrypted = self.key_table[(char_1_index // COLUMN_COUNT) + ((char_1_index - 1) % COLUMN_COUNT)]
                char_2_decrypted = self.key_table[(char_2_index // COLUMN_COUNT) + ((char_2_index - 1) % COLUMN_COUNT)]

            # Same column
            elif (char_1_index % COLUMN_COUNT) == (char_2_index % COLUMN_COUNT):
                char_1_decrypted = self.key_table[(char_1_index - COLUMN_COUNT) % len(self.key_table)]
                char_2_decrypted = self.key_table[(char_2_index - COLUMN_COUNT) % len(self.key_table)]

            elif (char_1_index % COLUMN_COUNT) > (char_2_index % COLUMN_COUNT):
                column_difference = (char_1_index % COLUMN_COUNT) - (char_2_index % COLUMN_COUNT)

                char_1_decrypted = self.key_table[char_1_index - column_difference]
                char_2_decrypted = self.key_table[char_2_index + column_difference]

            elif (char_1_index % COLUMN_COUNT) < (char_2_index % COLUMN_COUNT):
                column_difference = (char_2_index % COLUMN_COUNT) - (char_1_index % COLUMN_COUNT)

                char_1_decrypted = self.key_table[char_1_index + column_difference]
                char_2_decrypted = self.key_table[char_2_index - column_difference]

            processed_plaintext_list.append(char_1_decrypted)
            processed_plaintext_list.append(char_2_decrypted)

        return ''.join(processed_plaintext_list)
