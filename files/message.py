from dataclasses import dataclass


@dataclass
class Message:
    message_name = str
    message_content = str
    rot_type = str
    status = str
