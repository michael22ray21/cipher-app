import inquirer
import HandleFiles as hf
from ExtendedVigenereCipher import ExtendedVigenereCipher

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
        raise NotImplementedError
    elif cipher_answer['cipher_type'] == "Full Vigenere Cipher":
        raise NotImplementedError
    elif cipher_answer['cipher_type'] == "Auto-key Vigenere Cipher":
        raise NotImplementedError
    elif cipher_answer['cipher_type'] == "Extended Vigenere Cipher":
        extended_vignere_cipher_run(cipher_answer['cipher_mode'])
    elif cipher_answer['cipher_type'] == "Playfair Cipher":
        raise NotImplementedError
    elif cipher_answer['cipher_type'] == "Super Cipher":
        raise NotImplementedError
    elif cipher_answer['cipher_type'] == "Affine Cipher":
        raise NotImplementedError
    elif cipher_answer['cipher_type'] == "Hill Cipher":
        raise NotImplementedError
    elif cipher_answer['cipher_type'] == "Enigma Cipher":
        raise NotImplementedError
    else:
        raise NotImplementedError
