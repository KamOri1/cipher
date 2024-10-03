import string
from .rot import Rot
from files.message import Message


class Rot13(Rot):
    ALPHABET = string.ascii_lowercase

    def encrypt(self, plain_text: dict | Message) -> str:
        if isinstance(plain_text, dict):
            message: str = plain_text["content"]
        else:
            message: str = plain_text.content.lower()
        shifted_alphabet: str = self.ALPHABET[13:] + self.ALPHABET[:13]
        encrypted: dict = str.maketrans(self.ALPHABET, shifted_alphabet)
        encrypted_message: str = message.translate(encrypted)

        return encrypted_message

    def decrypt(self, encrypted_text) -> str:
        return self.encrypt(encrypted_text)
