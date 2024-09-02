import string
from .rot import Rot


class Rot13(Rot):
    ALPHABET = string.ascii_lowercase

    def encrypt(self, plain_text):
        message: str = plain_text.lower()
        shifted_alphabet : str = self.ALPHABET[13:] + self.ALPHABET[:13]
        encrypted : dict = str.maketrans(self.ALPHABET, shifted_alphabet)
        encrypted_message : str = message.translate(encrypted)

        return encrypted_message

    def decrypt(self, encrypted_text):
        return self.encrypt(encrypted_text)
