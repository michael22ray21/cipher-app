import inquirer
import HandleFiles as hf

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
        raise NotImplementedError
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
