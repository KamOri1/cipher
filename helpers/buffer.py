import json


class Buffer:
    def get_all_info(self, **kwargs) -> dict:
        complex_message = kwargs
        return complex_message

    def message_to_json(self, message: dict) -> json:
        message_json = json.dumps(message)
        return message_json
