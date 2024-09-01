from cipher.menus.content_menu import Menu
from cipher.files.message import Message
from cipher.services.encryption_file import Encryption

class Manager(Menu):
    def __init__(self, open_message, exite):
        super().__init__()
        self.new_message = Message()
        self.encryption = Encryption()
        self.open_message = open_message
        self.exite = exite

        self.start_menu()

    def start_menu(self)-> None:
            while True:
                first_choose = self.show_menu()
                match first_choose:
                    case '1': self.show_new_message_options()
                    case '2': pass
                    case '3': pass

                match self.new_message.rot_type:
                    case 'rot13': self.encryption.encrypt_message_rot13(self.new_message.message_content)
                    case 'rot47': self.encryption.encrypt_message_rot47(self.new_message.message_content)

    def show_menu(self):
        super().show_menu()
        return self.execute()

    def execute(self):
        return super().get_choose()

    def show_new_message_options(self)-> None:
        self.new_message.message_name = input('Enter message name: ')
        self.new_message.message_content = input('Enter message content: ')
        self.new_message.rot_type = input('Choose rot13 or rot47: ')


