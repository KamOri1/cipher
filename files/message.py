from dataclasses import dataclass


@dataclass
class Message:
    name: str
    content: str
    rot_type: str
    status: str

a = Message(name='kamil', content='cos tam wiem', rot_type='rot13', status='encription').__dict__
print(a)
