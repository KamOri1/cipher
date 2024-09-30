from cipher.manager.app_manager import Manager
from cipher.helpers.buffer import Buffer
import pytest


@pytest.fixture
def mock_start_menu(mocker):
    mock_start_menu = mocker.patch("cipher.manager.app_manager.Manager.start_menu")
    mock_start_menu.side_effect = lambda *args, **kwargs: None
    buffer = Buffer()
    manager = Manager(buffer)
    mock_start_menu.assert_called_once_with()

    return manager


def test_mock_choose_rot_should_return_correct_value(mock_start_menu, mocker):
    manager = mock_start_menu
    with mocker.patch("builtins.input", return_value="rot13"):
        result = manager.choose_rot()
        assert result == "rot13"


def test_mock_file_name_should_return_correct_value(mock_start_menu, mocker):
    manager = mock_start_menu
    with mocker.patch("builtins.input", return_value="new file"):
        result = manager.file_name()
        assert result == "new file"


def test_mock_get_message_data_should_return_message(mock_start_menu, mocker):
    manager = mock_start_menu
    with mocker.patch("builtins.input", side_effect=["new file", "something"]):
        result = manager.get_message_data("rot13", operation="Encrypting")

        assert result.__dict__ == {
            "name": "new file",
            "content": "something",
            "rot_type": "rot13",
            "status": "Encrypting",
        }
