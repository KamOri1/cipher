from dataclasses import dataclass


@dataclass
class Message:
    name: str
    content: str
    rot_type: str
    status: str


