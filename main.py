import inquirer
import HandleFiles as hf

if __name__ == "__main__":
    cipher_answer = inquirer.list_input(
        "Choose cipher type",
        choices=[
            "Vigenere Cipher",
            "Full Vigenere Cipher",
            "Auto-key Vigenere Cipher",
            "Extended Vigenere Cipher",
            "Playfair Cipher",
            "Super Encryption",
            "Affine Cipher",
            "Hill Cipher",
            "Enigma Cipher"
        ],
    )

    if cipher_answer == "Vigenere Cipher":
        raise NotImplementedError
    elif cipher_answer == "Full Vigenere Cipher":
        raise NotImplementedError
    elif cipher_answer == "Auto-key Vigenere Cipher":
        raise NotImplementedError
    elif cipher_answer == "Extended Vigenere Cipher":
        raise NotImplementedError
    elif cipher_answer == "Playfair Cipher":
        raise NotImplementedError
    elif cipher_answer == "Super Cipher":
        raise NotImplementedError
    elif cipher_answer == "Affine Cipher":
        raise NotImplementedError
    elif cipher_answer == "Hill Cipher":
        raise NotImplementedError
    elif cipher_answer == "Enigma Cipher":
        raise NotImplementedError
    else:
        raise NotImplementedError
