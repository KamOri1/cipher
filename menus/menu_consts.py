from dataclasses import dataclass


@dataclass
class MenuConsts:
    OPTIONS = ['New message', 'Open message', 'Buffer', 'Exit']
    NEW_MESSAGE_OPTIONS = ['Add next message', 'Save message']
    SAVE_OPTIONS = ['One message one file', 'All in one file ']
    DECRYPT_OR_ADD = ['Decrypt / Encrypt message', 'Add message to the file']
    BUFFER_OPTIONS = ['Save buffer', 'Clear buffer']

