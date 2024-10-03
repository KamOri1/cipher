from abc import ABC, abstractmethod


class Rot(ABC):
    @abstractmethod
    def encrypt(self, plain_text) -> None:
        pass

    @abstractmethod
    def decrypt(self, encrypted_text) -> None:
        pass
