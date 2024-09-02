from cipher.menus.content_menu import Menu
from cipher.files.message import Message
from cipher.services.encryption_file import Encryption
from cipher.helpers.buffer import Buffer
from cipher.files.saver import SaveFile


class Manager(Menu):
    def __init__(self, open_message):
        super().__init__()
        self.new_message = Message()
        self.encryption = Encryption()
        self.buffer = Buffer()
        self.save_file = SaveFile()
        self.open_message = open_message
        self.start_menu()

    def start_menu(self) -> None:
            while True:
                first_choose = self.show_menu()
                match first_choose:
                    case '1': self.show_new_message_options()
                    case '2': pass
                    case '3': break

                match self.new_message.rot_type:
                    case 'rot13': self.rot13_encription(self.new_message.message_content)
                    case 'rot47': self.rot47_encription(self.new_message.message_content)

    def show_menu(self):
        super().show_menu()
        return self.execute()

    def execute(self):
        return super().get_choose()

    def show_new_message_options(self) -> None:
        self.new_message.message_name = input('Enter message name: ')
        self.new_message.message_content = input('Enter message content: ')
        self.new_message.rot_type = input('Choose rot13 or rot47: ')

    def rot13_encription(self, message):
        self.new_message.message_content = self.encryption.encrypt_message_rot13(message)
        print(self.new_message.message_content)
        self.collect_message_to_save()
        return self.save_message_to_file(self.buffer.buffer_list[-1])

    def rot47_encription(self, message):
        self.new_message.message_content = self.encryption.encrypt_message_rot47(message)

        return self.new_message.message_content

    def collect_message_to_save(self):
        collected_message = self.buffer.get_all_info(
                                                     name=self.new_message.message_name,
                                                     text=self.new_message.message_content,
                                                     rot_type=self.new_message.rot_type,
                                                     )
        return self.buffer.message_to_json(collected_message)

    def save_message_to_file(self, message):
        self.save_file.save_message(message)