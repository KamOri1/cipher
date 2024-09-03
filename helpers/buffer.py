import json


class Buffer:
    def __init__(self):
        self.buffer_list = []

    def get_all_info(self, message) -> dict:
        complex_message =message
        return complex_message

    def message_to_json(self, message: dict):
        message_json = self.buffer_list.append(message)

        return message_json

    def get_last_message(self) -> dict:
        return self.buffer_list[-1]
