import json

class ReadFile:
    @staticmethod
    def read_file(file_name: str) -> None:
        with open(f'encrypted_files/{file_name}.json', 'r+') as file:
                json.load(file)



