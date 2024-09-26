import os


class Catalog:
    @staticmethod
    def create_catalog() -> None:
        if os.path.exists("../encrypted_file") is False:
            os.makedirs("../encrypted_file")
