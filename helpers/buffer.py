from cipher.files.saver import SaveFile


class Buffer:
    def __init__(self):
        self.buffer_list = []

    def message_to_json(self, message: dict):
        message_json = self.buffer_list.append(message.__dict__)
        return message_json

    def get_last_message(self) -> dict:
        return self.buffer_list[-1]

    def clear_buffer(self):
        self.buffer_list.clear()

    def save_buffer(self):
        file_name = input('Enter file name: ')
        SaveFile.save_message(self.buffer_list, file_name)
