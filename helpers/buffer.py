import json


class Buffer:
    buffer_list: list = []

    def get_all_info(self, **kwargs) -> dict:
        complex_message = kwargs
        return complex_message

    def message_to_json(self, message: dict) -> json:
        message_json = json.dumps(message)
        self.buffer_list.append(message_json)
        return message_json
