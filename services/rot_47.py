import string
from .rot import Rot


class Rot47(Rot):
    ALPHABET_47 =string.ascii_lowercase + string.punctuation + string.digits + string.ascii_uppercase

    def encrypt(self, plain_text):
        message: str = plain_text.lower()
        shifted_alphabet: str = self.ALPHABET_47[47:] + self.ALPHABET_47[:47]
        encrypted: dict = str.maketrans(self.ALPHABET_47, shifted_alphabet)
        encrypted_message: str = message.translate(encrypted)

        return encrypted_message

    def decrypt(self, encrypted_text):
        return self.encrypt(encrypted_text)

