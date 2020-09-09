import inquirer
import HandleFiles as hf
from VignereCipher import VignereCipher
from ExtendedVigenereCipher import ExtendedVigenereCipher
from PlayfairCipher import PlayfairCipher
from HillCipher import HillCipher
from SuperCipher import SuperCipher
from AffineCipher import AffineCipher
from AutoKeyVignereCipher import AutoKeyVignereCipher
from FullVignereCipher import FullVignereCipher

def vigenere_cipher_run(mode: str):
    key = simple_key_read_prompt()

    cipher = VignereCipher(key)

    if mode == "Encrypt":
        plaintext = plaintext_read_prompt()

        ciphertext = cipher.encrypt(plaintext)

        ciphertext_write_prompt(ciphertext)

    elif mode == "Decrypt":
        ciphertext = ciphertext_read_prompt()

        plaintext = cipher.decrypt(ciphertext)

        plaintext_write_prompt(plaintext)

def full_vigenere_cipher_run(mode: str):
    key = simple_key_read_prompt()

    cipher = FullVignereCipher(key)

    if mode == "Encrypt":
        plaintext = plaintext_read_prompt()

        ciphertext = cipher.encrypt(plaintext)

        ciphertext_write_prompt(ciphertext)

    elif mode == "Decrypt":
        ciphertext = ciphertext_read_prompt()

        plaintext = cipher.decrypt(ciphertext)

        plaintext_write_prompt(plaintext)

def extended_vignere_cipher_run(mode: str):
    key = extended_vignere_cipher_get_key()

    cipher = ExtendedVigenereCipher(key)

    if mode == "Encrypt":
        extended_vignere_cipher_encrypt(cipher)

    elif mode == "Decrypt":
        extended_vignere_cipher_decrypt(cipher)

def extended_vignere_cipher_get_key() -> bytearray:
    # Set up cipher key
    key_source = inquirer.list_input(
        "Choose key source",
        choices=[
            "Manual Input",
            "File"
        ]
    )

    if key_source == "Manual Input":
        key_string = inquirer.text(message="key")

        return key_string.encode('UTF-8')

    elif key_source == "File":
        question = [
            inquirer.Path("file_path",
                            message="path to key file",
                            path_type=inquirer.Path.FILE,
                            ),
        ]

        key_file_path = inquirer.prompt(question)

        return hf.read_file_as_bytearray(key_file_path['file_path'])

    else:
        raise NotImplementedError

def extended_vignere_cipher_encrypt(cipher: ExtendedVigenereCipher):
        # Ask for plain binary and where to store the result
        question = [
            inquirer.Path("source",
                            message="path to plain file",
                            path_type=inquirer.Path.FILE,
                            ),
            inquirer.Path("destination",
                            message="path for encrypted result",
                            path_type=inquirer.Path.FILE,
                            ),
        ]

        answer = inquirer.prompt(question)

        plain_data = hf.read_file_as_bytearray(answer['source'])

        encrypted_data = cipher.encrypt(plain_data)

        hf.write_file_from_bytearray(encrypted_data, answer['destination'])

def extended_vignere_cipher_decrypt(cipher: ExtendedVigenereCipher):
        # Ask for encrypted binary and where to store the result
        question = [
            inquirer.Path("source",
                            message="path to encrypted file",
                            path_type=inquirer.Path.FILE,
                            ),
            inquirer.Path("destination",
                            message="path for decrypted result",
                            path_type=inquirer.Path.FILE,
                            ),
        ]

        answer = inquirer.prompt(question)

        encrypted_data = hf.read_file_as_bytearray(answer['source'])

        plain_data = cipher.decrypt(encrypted_data)

        hf.write_file_from_bytearray(plain_data, answer['destination'])

def playfair_cipher_run(mode: str):
    key = playfair_cipher_get_key()

    cipher = PlayfairCipher(key)

    if mode == "Encrypt":
        plaintext = plaintext_read_prompt()

        ciphertext = cipher.encrypt(plaintext)

        ciphertext_write_prompt(ciphertext)

    elif mode == "Decrypt":
        ciphertext = ciphertext_read_prompt()

        plaintext = cipher.decrypt(ciphertext)

        plaintext_write_prompt(plaintext)

def playfair_cipher_get_key() -> str:
    # Set up cipher key
    key_source = inquirer.list_input(
        "Choose key source",
        choices=[
            "Manual Input",
            "File"
        ]
    )

    if key_source == "Manual Input":
        key_string = inquirer.text(message="key")

        return key_string

    elif key_source == "File":
        question = [
            inquirer.Path("file_path",
                            message="path to key file",
                            path_type=inquirer.Path.FILE,
                            ),
        ]

        key_file_path = inquirer.prompt(question)

        return hf.read_file_as_string_single_stripped(key_file_path['file_path'])

    else:
        raise NotImplementedError

def hillCipher_cipher_run(mode: str):
    key = hillCipher_cipher_get_key()

    cipher = HillCipher(key)

    if mode == "Encrypt":
        plaintext = plaintext_read_prompt()

        ciphertext = cipher.encrypt(plaintext)

        ciphertext_write_prompt(ciphertext)

    elif mode == "Decrypt":
        ciphertext = ciphertext_read_prompt()

        plaintext = cipher.decrypt(ciphertext)

        plaintext_write_prompt(plaintext)

def hillCipher_cipher_get_key() -> str:
    # Set up cipher key
    key_source = inquirer.list_input(
        "Choose key source",
        choices=[
            "Manual Input",
            "File"
        ]
    )

    if key_source == "Manual Input":
        key_size = int(inquirer.text(message="key size (N x N)"))

        key_string = inquirer.text(message="key")

        key_list = [int(x) for x in key_string.split()]

        if len(key_list) != key_size ** 2:
            raise Exception("key length not valid")

        key = []

        for i in range(0, key_size):
            key_row = []
            for j in range(0, key_size):
                key_row.append(key_list[key_size * i + j])
            key.append(key_row)

        return key

    elif key_source == "File":
        question = [
            inquirer.Path("file_path",
                            message="path to key file",
                            path_type=inquirer.Path.FILE,
                            ),
        ]

        key_file_path = inquirer.prompt(question)

        key_string_list = hf.read_file_as_string_list_stripped(key_file_path['file_path'])

        key_size = int(key_string_list[0])

        key_list = [int(x) for x in key_string_list[1].split()]

        if len(key_list) != key_size ** 2:
            raise Exception("key length not valid")

        key = []

        for i in range(0, key_size):
            key_row = []
            for j in range(0, key_size):
                key_row.append(key_list[key_size * i + j])
            key.append(key_row)

        return key

    else:
        raise NotImplementedError

def super_cipher_run(mode: str):
    key = simple_key_read_prompt()

    cipher = SuperCipher(key)

    if mode == "Encrypt":
        plaintext = plaintext_read_prompt()

        ciphertext = cipher.encrypt(plaintext)

        ciphertext_write_prompt(ciphertext)

    elif mode == "Decrypt":
        ciphertext = ciphertext_read_prompt()

        plaintext = cipher.decrypt(ciphertext)

        plaintext_write_prompt(plaintext)

def affine_cipher_run(mode: str):
    key = [int(x) for x in simple_key_read_prompt().split()]

    cipher = AffineCipher(key)

    if mode == "Encrypt":
        plaintext = plaintext_read_prompt()

        ciphertext = cipher.encrypt(plaintext)

        ciphertext_write_prompt(ciphertext)

    elif mode == "Decrypt":
        ciphertext = ciphertext_read_prompt()

        plaintext = cipher.decrypt(ciphertext)

        plaintext_write_prompt(plaintext)

def autokey_vigenere_cipher_run(mode: str):
    key = simple_key_read_prompt()

    cipher = AutoKeyVignereCipher(key)

    if mode == "Encrypt":
        plaintext = plaintext_read_prompt()

        ciphertext = cipher.encrypt(plaintext)

        ciphertext_write_prompt(ciphertext)

    elif mode == "Decrypt":
        ciphertext = ciphertext_read_prompt()

        plaintext = cipher.decrypt(ciphertext)

        plaintext_write_prompt(plaintext)

def plaintext_read_prompt() -> str:
        # Ask for plaintext source
        plaintext_source = inquirer.list_input(
            "Choose plaintext source",
            choices=[
                "Manual Input",
                "File"
            ]
        )

        if plaintext_source == "Manual Input":
            plaintext_string = inquirer.text(message="plaintext")

            return plaintext_string

        elif plaintext_source == "File":
            question = [
                inquirer.Path("file_path",
                                message="path to plaintext file",
                                path_type=inquirer.Path.FILE,
                                ),
            ]

            plaintext_file_path = inquirer.prompt(question)

            return hf.read_file_as_string_single_stripped(plaintext_file_path['file_path'])

        else:
            raise NotImplementedError

def ciphertext_write_prompt(ciphertext: str):
    # Ask for ciphertext destination
    destination = inquirer.list_input(
        "Choose result destination",
        choices=[
            "Terminal Output",
            "File"
        ]
    )

    group_by_five = inquirer.confirm(
        "Group result by 5 characters?",
        default=False
    )

    if group_by_five:
        temporary_ciphertext = ""

        for idx, elem in enumerate(ciphertext):
            temporary_ciphertext += elem
            if idx % 5 == 4:
                temporary_ciphertext += " "

        ciphertext = temporary_ciphertext

    if destination == "Terminal Output":
        print(ciphertext)

    elif destination == "File":
        question = [
            inquirer.Path("file_path",
                            message="path to ciphertext file",
                            path_type=inquirer.Path.FILE,
                            ),
        ]

        ciphertext_file_path = inquirer.prompt(question)

        hf.write_file_from_string(ciphertext, ciphertext_file_path['file_path'])

    else:
        raise NotImplementedError

def ciphertext_read_prompt() -> str:
        # Ask for ciphertext source
        ciphertext_source = inquirer.list_input(
            "Choose ciphertext source",
            choices=[
                "Manual Input",
                "File"
            ]
        )

        if ciphertext_source == "Manual Input":
            ciphertext_string = inquirer.text(message="ciphertext")

            return ciphertext_string

        elif ciphertext_source == "File":
            question = [
                inquirer.Path("file_path",
                                message="path to ciphertext file",
                                path_type=inquirer.Path.FILE,
                                ),
            ]

            ciphertext_file_path = inquirer.prompt(question)

            return hf.read_file_as_string_single_stripped(ciphertext_file_path['file_path'])

        else:
            raise NotImplementedError

def plaintext_write_prompt(plaintext: str):
    # Ask for plaintext destination
    destination = inquirer.list_input(
        "Choose result destination",
        choices=[
            "Terminal Output",
            "File"
        ]
    )

    if destination == "Terminal Output":
        print(plaintext)

    elif destination == "File":
        question = [
            inquirer.Path("file_path",
                            message="path to plaintext file",
                            path_type=inquirer.Path.FILE,
                            ),
        ]

        plaintext_file_path = inquirer.prompt(question)

        hf.write_file_from_string(plaintext, plaintext_file_path['file_path'])

    else:
        raise NotImplementedError

def simple_key_read_prompt() -> str:
    # Set up cipher key
    key_source = inquirer.list_input(
        "Choose key source",
        choices=[
            "Manual Input",
            "File"
        ]
    )

    if key_source == "Manual Input":
        key_string = inquirer.text(message="key")

        return key_string

    elif key_source == "File":
        question = [
            inquirer.Path("file_path",
                            message="path to key file",
                            path_type=inquirer.Path.FILE,
                            ),
        ]

        key_file_path = inquirer.prompt(question)

        return hf.read_file_as_string_single_stripped(key_file_path['file_path'])

    else:
        raise NotImplementedError

if __name__ == "__main__":
    cipher_question = [
        inquirer.List(
            name="cipher_type",
            message="Choose cipher type",
            choices=[
                "Vigenere Cipher",
                "Full Vigenere Cipher",
                "Auto-key Vigenere Cipher",
                "Extended Vigenere Cipher",
                "Playfair Cipher",
                "Super Encryption",
                "Affine Cipher",
                "Hill Cipher",
                "Enigma Cipher",
            ],
        ),
        inquirer.List(
            name="cipher_mode",
            message="Chose cipher mode",
            choices=[
                "Encrypt",
                "Decrypt",
            ]
        ),
    ]

    cipher_answer = inquirer.prompt(cipher_question)

    if cipher_answer['cipher_type'] == "Vigenere Cipher":
        vigenere_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Full Vigenere Cipher":
        full_vigenere_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Auto-key Vigenere Cipher":
        autokey_vigenere_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Extended Vigenere Cipher":
        extended_vignere_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Playfair Cipher":
        playfair_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Super Encryption":
        super_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Affine Cipher":
        affine_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Hill Cipher":
        hillCipher_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Enigma Cipher":
        raise NotImplementedError
    else:
        raise NotImplementedError
