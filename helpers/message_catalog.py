import os


class Catalog:
    @staticmethod
    def create_catalog() -> None:
        os.makedirs("./encrypted_file", exist_ok=True)
