from cipher.menus.content_menu import Menu
from cipher.files.message import Message
from cipher.services import rot_factory, ROT_TYPE_13, ROT_TYPE_47
from cipher.files.saver import SaveFile
from cipher.files.reader import ReadFile

# 1. User zapisuje cos do buffera jedna lub wiele wiadomosci mzoe zapisac do pliku / moze dodac pliku
# 2. user moze wczytac z pliku wiadomosci, dodac kolejna wiadomosc i zapisac do pliku z nowa wiadomscia
# 3. czyszczenie buffera*.

class Manager(Menu):
    def __init__(self, buffer):
        self.buffer = buffer
        self.start_menu()

    def start_menu(self) -> None:
        while True:
            self.show_menu()
            first_choose = self.get_choose()
            match first_choose:
                case '1':
                    rot_type = self.choose_rot()
                    match rot_type:
                        case 'rot13': self.encrypt_message(rot_type=ROT_TYPE_13)
                        case 'rot47': self.encrypt_message(rot_type=ROT_TYPE_47)
                case '2': self.choose_file_to_open()
                case '3': ... # save_buffer_to_file()
                case '4': break

    @staticmethod
    def choose_rot():
        return input('Enter ROT type: ')

    @staticmethod
    def get_message_data(rot_type, operation) -> Message:
        name = input('Enter message name: ')
        content = input('Enter message content: ')

        return Message(name=name, content=content, rot_type=rot_type, status=operation)

    def encrypt_message(self, rot_type):
        message = self.get_message_data(rot_type, operation='Encrypting')
        encryptor = rot_factory(rot_type)
        message.content = encryptor.encrypt(message)
        self.collect_message_to_save(message)
        file_name = input('Enter file name: ')
        return self.save_message_to_file(self.buffer.get_last_message(), file_name)

    def decrypt_message(self, rot_type, message):
        decrypt = rot_factory(rot_type)
        decrypt_message = decrypt.decrypt(message)
        print(f'\nMessage: {decrypt_message}\n')
        return decrypt_message

    def collect_message_to_save(self, message):
        return self.buffer.message_to_json(message)

    def save_message_to_file(self, message: dict, file_name) -> None:
       SaveFile.save_message(message, file_name)

    def choose_file_to_open(self) -> None:
        file_name = input('Enter the file name: ')
        file_message = ReadFile.read_file(file_name)
        ReadFile.print_file_content(file_name=file_name, file_content=file_message)
        choose_file = int(input(f'Enter choose file to open: 1-{len(file_message)}: '))  - 1

        match file_message[choose_file]['rot_type']:
            case 'rot_13':
                message = self.decrypt_message(rot_type=ROT_TYPE_13, message=file_message[choose_file])
                SaveFile.save_decrypted_content(file_name=file_name,
                                                file_content=file_message,
                                                user_choose=choose_file,
                                                decrypted_message=message)

            case 'rot_47':
                    message = self.decrypt_message(rot_type=ROT_TYPE_47, message=file_message[choose_file])
                    SaveFile.save_decrypted_content(file_name=file_name,
                                                    file_content=file_message,
                                                    user_choose=choose_file,
                                                    decrypted_message=message)

