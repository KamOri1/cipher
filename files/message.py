class Message:
    def encrypted_message(self)-> dict:
        message : dict = {
                        'name': self.message_name,
                        'text': self.message_content,
                        'rot_type': self.rot_type,
                        'status': 'encrypted'
                         }
        return message

    def add_new_message(self)-> None:
        self.message_name = input('Enter message name: ')
        self.message_content = input('Enter message content: ')
        self.rot_type = input('Choose rot13 or rot47: ')

