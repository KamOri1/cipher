from helpers.buffer import Buffer
from files.message import Message
import files.saver
import pytest
import os


@pytest.fixture
def mock_files_dir(mocker):
    new_value = ""
    mocker.patch.object(files.saver, "FILES_DIR", new_value)


@pytest.fixture
def create_message(mocker):
    message_information = mocker.Mock(spec=Message)
    message_information.name = "Secret"
    message_information.content = "something"
    message_information.rot_type = "rot13"
    message_information.status = "Encrypting"

    return message_information


class TestBuffer:
    def test_message_to_json_should_add_message_to_buffer_list(self, create_message):
        buffer = Buffer()
        message = create_message
        buffer.message_to_json(message)

        assert buffer.buffer_list == [message.__dict__]

    def test_get_last_message_should_return_last_message(self, create_message):
        buffer = Buffer()
        buffer.message_to_json(create_message)
        message = create_message
        buffer.message_to_json(message)

        assert buffer.get_last_message() == message.__dict__

    def test_clear_buffer_should_return_empty_list(self, create_message):
        buffer = Buffer()
        message = create_message
        buffer.message_to_json(message)
        buffer.clear_buffer()

        assert buffer.buffer_list == []

    def test_save_buffer_should_save_buffer_to_json_file(self, mock_files_dir, mocker):
        buffer = Buffer()
        buffer.buffer_list = {
            "name": "new file",
            "content": "something",
            "rot_type": "rot13",
            "status": "Decrypting",
        }
        json_file_path = "test_file.json"
        mocker.patch("builtins.input", return_value="test_file")
        buffer.save_buffer()
        os.remove(json_file_path)

    def test_save_buffer_should_create_json_file_with_one_dict_list(
        self, mock_files_dir, mocker
    ):
        buffer = Buffer()
        buffer.buffer_list = {
            "name": "new file",
            "content": "something",
            "rot_type": "rot13",
            "status": "Decrypting",
        }
        mocker.patch("builtins.input", return_value="test2_file")
        buffer.save_buffer()
        json_file_path = "test2_file.json"
        with open(json_file_path, "r") as file:
            actual_json = file.read()
        assert (
            actual_json
            == '[{"name": "new file", "content": "something", "rot_type": "rot13", "status": "Decrypting"}]'
        )
        os.remove(json_file_path)
