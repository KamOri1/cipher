from dataclasses import dataclass

@dataclass
class MenuConsts:
    OPTIONS = ['New message', 'Open message', 'Save buffer', 'Exite']
    NEW_MESSAGE_OPTIONS = ['Add next message', 'Save message']
    SAVE_OPTIONS = ['One message one file', 'All in one file ']
    DECRYPT_OR_ADD = ['Decrypt message', 'Add message to the file']

