from cipher.menus.content_menu import Menu
from cipher.files.message import Message
from cipher.services import rot_factory, ROT_TYPE_13, ROT_TYPE_47
from cipher.files.saver import SaveFile
from cipher.files.reader import ReadFile
from typing import Type

# class A:
#     def str(self):
#         return 'class A'
#
# class B(A):
#     def str(self):
#         # albo nadpisujesz calkowicie
#         # albo chcesz uzyć str'a z klasy nadrzednej wtedy super()
#         # albo nie nadpisujesz w ogóle i używasz po prostu str z klasy A
#         old_str = super().str()
#         old_str += 'class B'
#         return old_str
#
# class ASuper(A):
#     def method(self):
#         ...
#
# a = ASuper()
# a.str()

# 1. User zapisuje cos do buffera jedna lub wiele wiadomosci mzoe zapisac do pliku / moze dodac pliku
# 2. user moze wczytac z pliku wiadomosci, dodac kolejna wiadomosc i zapisac do pliku z nowa wiadomscia
# 3. czyszczenie buffera*.

class Manager(Menu):
    def __init__(self, buffer):
        self.buffer = buffer
        self.save_file = SaveFile() # Metody statyczne zamiast obiektów i uzywanie bezpośrednio na klasie
        self.open_message = ReadFile() # Metody statyczne zamiast obiektów i uzywanie bezpośrednio na klasie
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



    def choose_rot(self):
        return input('Enter ROT type: ')

    def get_message_data(self, rot_type, operation) -> Message: # get_message_data
        # Zwracania info od user'a zaimast od razu przypisywac.
        name = input('Enter message name: ')
        content = input('Enter message content: ')

        return Message(name=name, content=content, rot_type=rot_type, status=operation)



    def encrypt_message(self, rot_type):
        message = self.get_message_data(rot_type, operation='Encrypting')
        encryptor = rot_factory(rot_type)

        message.content = encryptor.encrypt(message)
        print(f'=============================={message.content}')
        print(f'=============================={message.__dict__}')
        self.collect_message_to_save(message.__dict__)

        return self.save_message_to_file(self.buffer.get_last_messag())


    def collect_message_to_save(self, message):
        return self.buffer.message_to_json(message)

    def save_message_to_file(self, message: dict) -> None:
        self.save_file.save_message(message)

    def choose_file_to_open(self) -> None:
        file_name = input('Enter the file name: ')
        file_message = self.open_message.read_file(file_name)
        match file_message['rot_type']:
            case 'rot13':
                message = self.encryption.encrypt_message_rot13(file_message['text'])
                print(f'Message: {message}')
                self.rot13_decription(file_message['text'], file_message)

            case 'rot47':
                message = self.encryption.encrypt_message_rot47(file_message['text'])
                print(f'Message: {message}')
                self.rot47_decription(file_message['text'], file_message)



    def collect_decription_message_to_save(self, decription_message: str, encryption_message: dict) -> dict:
        collected_message = self.buffer.get_all_info(
                                                     name=encryption_message['name'],
                                                     text=decription_message,
                                                     rot_type=encryption_message['rot_type'],
                                                     status='decryption'
                                                     )
        return self.buffer.message_to_json(collected_message)

    def rot13_decription(self, message: str, file_message: dict):
        decryption_message = self.encryption.encrypt_message_rot13(message)
        self.collect_decription_message_to_save(decryption_message, file_message)

        return self.save_message_to_file(self.buffer.buffer_list[-1])

    def rot47_decription(self, message: str, file_message: dict):
        decryption_message = self.encryption.encrypt_message_rot47(message)
        self.collect_decription_message_to_save(decryption_message, file_message)

        return self.save_message_to_file(self.buffer.buffer_list[-1])
