from abc import ABC, abstractmethod


class Rot(ABC):
    @abstractmethod
    def encrypt(self, plain_text):
        pass

    @abstractmethod
    def decrypt(self, encrypted_text):
        pass
