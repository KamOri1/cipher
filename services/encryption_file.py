import string

class Encryption:
    ALPHABET = string.ascii_lowercase

    def __init__(self, message: str) -> None:
        self.message : str = message.lower()

    def encrypt_message_rot13(self)-> str:
        shifted_alphabet : str = self.ALPHABET[13:] + self.ALPHABET[:13]
        encrypted : dict = str.maketrans(self.ALPHABET, shifted_alphabet)
        encrypted_message : str = self.message.translate(encrypted)

        return encrypted_message

    def encrypt_message_rot47(self)-> str:
        pass

