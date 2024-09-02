class SaveFile:
    def save_message(self, all_message_information):
        with open('files/save_message.json', 'a') as file:
            file.write(f'{all_message_information}\n')
