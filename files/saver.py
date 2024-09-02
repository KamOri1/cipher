import json
from cipher.consts import FILES_DIR

class SaveFile:
    @staticmethod
    def save_message(all_message_information: dict) -> None:
        with open(f'{FILES_DIR}{all_message_information["name"]}.json', 'w') as file:
            json.dump(all_message_information, file)
