import json


class ReadFile:
    def read_file(self, file_name: str) -> dict:
        with open(f'encrypted_files/{file_name}.json', 'r+') as file:
                message_data = json.load(file)

        return message_data

