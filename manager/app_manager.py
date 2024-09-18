from cipher.menus.content_menu import Menu
from cipher.menus.menu_consts import MenuConsts
from cipher.menus.sub_menu import SubMenu
from cipher.files.message import Message
from cipher.services import rot_factory, ROT_TYPE_13, ROT_TYPE_47
from cipher.files.saver import SaveFile
from cipher.files.reader import ReadFile


class Manager(Menu):
    def __init__(self, buffer) -> None:
        self.buffer = buffer
        self.start_menu()

    def start_menu(self) -> None:
        while True:
            self.show_menu(MenuConsts.OPTIONS)
            first_choose: str = self.get_choose()
            match first_choose:
                case '1':
                    rot_type = self.choose_rot()
                    match rot_type:
                        case 'rot13': self.encrypt_message(rot_type=ROT_TYPE_13, fast_save='save')
                        case 'rot47': self.encrypt_message(rot_type=ROT_TYPE_47, fast_save='save')
                case '2': self.choose_file_to_open()
                case '3': self.buffer_options()
                case '4': break

    @staticmethod
    def choose_rot() -> input:
        return input('Enter ROT type: ')

    @staticmethod
    def file_name() -> input:
        return input('Enter file name: ')

    @staticmethod
    def get_message_data(rot_type, operation) -> Message:
        name = input('Enter message name: ')
        content = input('Enter message content: ')

        return Message(name=name, content=content, rot_type=rot_type, status=operation)

    def encrypt_message(self, rot_type, fast_save=None) -> dict:
        message = self.get_message_data(rot_type, operation='Encrypting')
        encryptor = rot_factory(rot_type)
        message.content = encryptor.encrypt(message)
        self.collect_message_to_save(message)
        match fast_save:
            case 'save':
                file_name = self.file_name()
                Manager.save_message_to_file(self.buffer.get_last_message(), file_name)
        return self.buffer.get_last_message()

    def buffer_options(self) -> None:
        self.show_menu(MenuConsts.BUFFER_OPTIONS)
        choose = self.get_choose()
        match choose:
            case '1':
                self.buffer.save_buffer()
            case '2':
                self.buffer.clear_buffer()

    @staticmethod
    def decrypt_message(rot_type: str, message: str) -> str:
        decrypt = rot_factory(rot_type)
        decrypt_message = decrypt.decrypt(message)
        print(f'\nMessage: {decrypt_message}\n')

        return decrypt_message

    def collect_message_to_save(self, message: object) -> dict:
        return self.buffer.message_to_json(message)

    @staticmethod
    def save_message_to_file(message: dict, file_name: str) -> None:
        SaveFile.save_message(message, file_name)

    def choose_file_to_open(self) -> None:
        file_name = self.file_name()
        file_message = ReadFile.read_file(file_name)
        ReadFile.print_file_content(file_name=file_name, file_content=file_message)
        user_choose = SubMenu.show_sub_menu(MenuConsts.DECRYPT_OR_ADD)
        match user_choose:
            case '1':
                choose_file = int(input(f'Choose message: 1-{len(file_message)}: ')) - 1
                message = Manager.decrypt_message(rot_type=file_message[choose_file]['rot_type'],
                                                  message=file_message[choose_file])

                SaveFile.save_decrypted_content(file_name=file_name,
                                                file_content=file_message,
                                                user_choose=choose_file,
                                                decrypted_message=message)
            case '2':
                rot_type = self.choose_rot()
                rot = {'rot13': ROT_TYPE_13, 'rot47': ROT_TYPE_47}
                SaveFile.add_message_to_file(file_name, self.encrypt_message(rot_type=rot[rot_type]))
