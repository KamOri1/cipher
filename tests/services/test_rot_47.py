from services.rot_47 import Rot47
from files.message import Message
import pytest


class TestRot47:
    @pytest.mark.parametrize(
        "message, expected_output",
        [
            (
                {
                    "content": "something to show",
                    "name": "new file",
                    "rot_type": "rot47",
                    "status": "Encrypting",
                },
                "731^8{|2` 83 7{3B",
            )
        ],
    )
    def test_case_1_encrypt_should_return_encrypted_message(
        self, message, expected_output
    ):
        rot = Rot47()
        result = rot.decrypt(message)

        assert result == expected_output

    @pytest.mark.parametrize(
        "message_text, expected_output",
        [
            (
                "something to show",
                "731^8{|2` 83 7{3B",
            )
        ],
    )
    def test_case_2_encrypt_should_return_encrypted_message(
        self, message_text, expected_output
    ):
        message = Message
        message.content = message_text
        rot = Rot47()
        result = rot.encrypt(message)

        assert result == expected_output

    @pytest.mark.parametrize(
        "message_text, expected_output",
        [
            (
                "731^8{|2`",
                "something",
            )
        ],
    )
    def test_case_1_decrypt_should_return_decrypted_message(
        self, message_text, expected_output
    ):
        message = Message
        message.content = message_text
        rot = Rot47()
        result = rot.decrypt(message)

        assert result == expected_output

    @pytest.mark.parametrize(
        "message, expected_output",
        [
            (
                {
                    "content": "731^8{|2`",
                    "name": "new file",
                    "rot_type": "rot47",
                    "status": "Encrypting",
                },
                "something",
            )
        ],
    )
    def test_case_2_decrypt_should_return_decrypted_message(
        self, message, expected_output
    ):
        rot = Rot47()
        result = rot.decrypt(message)

        assert result == expected_output
