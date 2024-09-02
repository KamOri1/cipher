import json
class SaveFile:
    def save_message(self, all_message_information: dict) -> None:
        with open(f'encrypted_files/{all_message_information["name"]}.json', 'w') as file:
            json.dump(all_message_information, file)
