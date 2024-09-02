import json
class SaveFile:
    def save_message(self, all_message_information):
        with open(f'files/{all_message_information["name"]}.json', 'w') as file:
            #file.write(f'{all_message_information}\n')
            json.dump(all_message_information, file)