from abc import ABC, abstractmethod


class Rot(ABC):
    @abstractmethod
    def encrypt(self, plain_text):
        ...

    @abstractmethod
    def decrypt(self, encrypted_text):
        ...
