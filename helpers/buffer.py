from typing import Any
from cipher.files.saver import SaveFile
from cipher.files.message import Message


class Buffer:
    def __init__(self):
        self.buffer_list = []

    def message_to_json(self, message: "Message"):
        self.buffer_list.append(message.__dict__)

    def get_last_message(self) -> dict[str, Any]:
        return self.buffer_list[-1]

    def clear_buffer(self) -> None:
        self.buffer_list.clear()

    def save_buffer(self) -> None:
        file_name = input("Enter file name: ")
        SaveFile.save_message(self.buffer_list, file_name)
