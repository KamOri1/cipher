import string

class Encryption:
    ALPHABET = string.ascii_lowercase
    def __init__(self, message: str) -> None:
        self.message = message.lower()

    def encrypt_message_rot13(self)-> str:
        shifted_alphabet = self.ALPHABET[13:] + self.ALPHABET[:13]
        encrypted = str.maketrans(self.ALPHABET, shifted_alphabet)
        encrypted_message = self.message.translate(encrypted)
        return encrypted_message

    def encrypt_message_rot47(self):
        pass

