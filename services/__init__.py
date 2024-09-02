from .encryption_file import Rot13

ROT_TYPE_13 = 'rot_13'
ROT_TYPE_47 = 'rot_47'


def rot_factory(rot_type):
    if rot_type == ROT_TYPE_13:
        return Rot13()
    elif rot_type == ROT_TYPE_47:
        ...
        # return Rot47()
