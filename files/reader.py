import json
from consts import FILES_DIR


class ReadFile:
    @staticmethod
    def read_file(file_name: str) -> list[dict[str, str]]:
        with open(f"{FILES_DIR}{file_name}.json", "r+") as file:
            file_content: list = json.load(file)

        return file_content

    @staticmethod
    def print_file_content(file_name: str, file_content: list[dict[str, str]]) -> None:
        print(f"List of message in file: '{file_name}.json'")
        for index, value in enumerate(file_content, start=1):
            print(f"{index}: {value}")
