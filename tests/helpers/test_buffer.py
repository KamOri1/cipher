from cipher.helpers.buffer import Buffer
from cipher.files.message import Message
import pytest


@pytest.fixture
def create_message(mocker):
    message_information = mocker.Mock(spec=Message)
    message_information.name = "Secret"
    message_information.content = "something"
    message_information.rot_type = "rot13"
    message_information.status = "Encrypting"

    return message_information


def test_message_to_json_should_add_message_to_buffer_list(create_message):
    buffer = Buffer()
    message = create_message
    buffer.message_to_json(message)

    assert buffer.buffer_list == [message.__dict__]
