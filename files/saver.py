import json
from cipher.consts import FILES_DIR
import string
class SaveFile:
    @staticmethod
    def save_message(all_message_information: dict) -> None:
        with open(f'{FILES_DIR}{all_message_information["name"]}.json', 'w') as file:
            json.dump([all_message_information], file)

    @staticmethod
    def add_message_to_file(file_name: str, new_message: dict) -> None:
        with open(f'{FILES_DIR}{file_name}.json', 'r+') as file:
             file_content = json.load(file)

        file_content.append(new_message)

        with open(f'{FILES_DIR}{file_name}.json', 'w') as file:
             json.dump(file_content, file, indent=4)




