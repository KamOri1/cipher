import string
from typing import Type


class Encryption:
    ALPHABET = string.ascii_lowercase
    ALPHABET_47 = ALPHABET + string.punctuation + string.digits + string.ascii_uppercase

    def encrypt_message_rot13(self, new_message: str )-> str:
        message: str = new_message.lower()
        shifted_alphabet : str = self.ALPHABET[13:] + self.ALPHABET[:13]
        encrypted : dict = str.maketrans(self.ALPHABET, shifted_alphabet)
        encrypted_message : str = message.translate(encrypted)

        return encrypted_message

    def encrypt_message_rot47(self, new_message: str )-> str:
        message: str = new_message.lower()
        shifted_alphabet: str = self.ALPHABET_47[47:] + self.ALPHABET_47[:47]
        encrypted: dict = str.maketrans(self.ALPHABET_47, shifted_alphabet)
        encrypted_message: str = message.translate(encrypted)

        return encrypted_message


