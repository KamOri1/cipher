from cipher.files.saver import SaveFile
import pytest
import cipher.files.saver
import cipher.consts


@pytest.fixture
def mock_files_dir(mocker):
    new_value = ""
    mocker.patch.object(cipher.files.saver, "FILES_DIR", new_value)


@pytest.mark.parametrize(
    "all_message_information, expected_json, file_name",
    [
        (
            {
                "name": "new file",
                "content": "something",
                "rot_type": "rot13",
                "status": "Decrypting",
            },
            '[{"name": "new file", "content": "something", "rot_type": "rot13", "status": "Decrypting"}]',
            "testcase1",
        ),
    ],
)
def test_save_message_should_create_json_file_with_one_dict_list(
    mock_files_dir, all_message_information, expected_json, file_name
):
    SaveFile.save_message(all_message_information, file_name)
    json_file_path = file_name + ".json"
    with open(json_file_path, "r") as f:
        actual_json = f.read()
    assert actual_json == expected_json


@pytest.mark.parametrize(
    "all_message_information, expected_json, file_name",
    [
        (
            [
                {
                    "name": "new file",
                    "content": "something",
                    "rot_type": "rot13",
                    "status": "Decrypting",
                },
                {
                    "name": "next file",
                    "content": "something else",
                    "rot_type": "rot47",
                    "status": "Decrypting",
                },
            ],
            '[{"name": "new file", "content": "something", "rot_type": "rot13", "status": "Decrypting"},'
            ' {"name": "next file", "content": "something else", "rot_type": "rot47", "status": "Decrypting"}]',
            "testcase2",
        ),
    ],
)
def test_save_message_should_create_json_file_with_list_of_dict(
    mock_files_dir, all_message_information, expected_json, file_name
):
    SaveFile.save_message(all_message_information, file_name)
    json_file_path = file_name + ".json"
    with open(json_file_path, "r") as f:
        actual_json = f.read()
    assert actual_json == expected_json


def test_function_message_status_should_return_encrypting_str():
    value = "Decrypting"
    exp = "Encrypting"

    assert SaveFile.message_status(value) == exp


def test_function_message_status_should_return_decrypting_str():
    value = "Encrypting"
    exp = "Decrypting"

    assert SaveFile.message_status(value) == exp


def test_function_message_status_should_return_none():
    value = "nothing"
    exp = None

    assert SaveFile.message_status(value) == exp
