from typing import Any
import json
from cipher.consts import FILES_DIR


class SaveFile:
    @staticmethod
    def save_message(all_message_information: dict[str, Any] | list, file_name) -> None:
        with open(f"{FILES_DIR}{file_name}.json", "w") as file:
            if isinstance(all_message_information, dict):
                json.dump([all_message_information], file)
            else:
                json.dump(all_message_information, file)

    @staticmethod
    def add_message_to_file(file_name: str, new_message: dict[str, Any]) -> None:
        with open(f"{FILES_DIR}{file_name}.json", "r+") as file:
            file_content: list = json.load(file)

        file_content.append(new_message)

        with open(f"{FILES_DIR}{file_name}.json", "w") as file:
            json.dump(file_content, file, indent=4)

    @staticmethod
    def save_decrypted_content(
        file_name: str, file_content: list, user_choose: int, decrypted_message: str
    ) -> None:
        file_content[user_choose]["content"] = decrypted_message
        file_content[user_choose]["status"] = SaveFile.message_status(
            file_content[user_choose]["status"]
        )
        decrypted = file_content

        with open(f"{FILES_DIR}{file_name}.json", "w") as file:
            json.dump(decrypted, file, indent=4)

    @staticmethod
    def message_status(file_content) -> str:
        status: str = file_content
        match status:
            case "Decrypting":
                return "Encrypting"
            case "Encrypting":
                return "Decrypting"
