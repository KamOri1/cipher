import json
from cipher.consts import FILES_DIR


class ReadFile:
    @staticmethod
    def read_file(file_name: str) -> list:
        with open(f'./{FILES_DIR}{file_name}.json', 'r+') as file:
            file_content: list = json.load(file)

        return file_content

    @staticmethod
    def print_file_content(file_name: str, file_content: list) -> None:
        print(f'List of message in \'{file_name}.json\' file:')
        for index, value in enumerate(file_content, start=1):
            print(f'{index}: {value}')
