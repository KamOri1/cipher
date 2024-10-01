from services.rot_13 import Rot13
from files.message import Message
import pytest


class TestRot13:
    @pytest.mark.parametrize(
        "message, expected_output",
        [
            (
                {
                    "content": "something to show",
                    "name": "new file",
                    "rot_type": "rot13",
                    "status": "Encrypting",
                },
                "fbzrguvat gb fubj",
            )
        ],
    )
    def test_encrypt_should_return_encrypted_message_for_message_provided_as_dict(
        self, message, expected_output
    ):
        rot = Rot13()
        result = rot.decrypt(message)

        assert result == expected_output

    @pytest.mark.parametrize(
        "message_text, expected_output",
        [
            (
                "something to show",
                "fbzrguvat gb fubj",
            )
        ],
    )
    def test_encrypt_should_return_encrypted_message_for_message_as_string(
        self, message_text, expected_output
    ):
        message = Message
        message.content = message_text
        rot = Rot13()
        result = rot.encrypt(message)

        assert result == expected_output

    @pytest.mark.parametrize(
        "message_text, expected_output",
        [
            (
                "fbzrguvat gb fubj",
                "something to show",
            )
        ],
    )
    def test_case_1_decrypt_should_return_decrypted_message(
        self, message_text, expected_output
    ):
        message = Message
        message.content = message_text
        rot = Rot13()
        result = rot.decrypt(message)

        assert result == expected_output

    @pytest.mark.parametrize(
        "message, expected_output",
        [
            (
                {
                    "content": "fbzrguvat gb fubj",
                    "name": "new file",
                    "rot_type": "rot13",
                    "status": "Encrypting",
                },
                "something to show",
            )
        ],
    )
    def test_case_2_decrypt_should_return_decrypted_message(
        self, message, expected_output
    ):
        rot = Rot13()
        result = rot.decrypt(message)

        assert result == expected_output
