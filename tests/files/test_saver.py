from cipher.files.saver import SaveFile
import pytest
import cipher.files.saver
import cipher.consts
import os


@pytest.fixture
def mock_files_dir(mocker):
    new_value = "json_file/"
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
    json_file_path = f"json_file/{file_name}.json"
    with open(json_file_path, "r") as f:
        actual_json = f.read()
    assert actual_json == expected_json
    os.remove(json_file_path)


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
    json_file_path = f"json_file/{file_name}.json"
    with open(json_file_path, "r") as f:
        actual_json = f.read()
    assert actual_json == expected_json
    os.remove(json_file_path)


@pytest.mark.parametrize(
    "all_message_information, expected_json, file_name, new_message",
    [
        (
            {
                "name": "add new file",
                "content": "something to test",
                "rot_type": "rot13",
                "status": "Decrypting",
            },
            """[
    {
        "name": "add new file",
        "content": "something to test",
        "rot_type": "rot13",
        "status": "Decrypting"
    },
    {
        "name": "next file",
        "content": "something else",
        "rot_type": "rot47",
        "status": "Decrypting"
    }
]""",
            "testa_add_message",
            {
                "name": "next file",
                "content": "something else",
                "rot_type": "rot47",
                "status": "Decrypting",
            },
        ),
    ],
)
def test_should_add_new_message_to_file(
    mock_files_dir, all_message_information, expected_json, file_name, new_message
):
    SaveFile.save_message(all_message_information, file_name)
    SaveFile.add_message_to_file(file_name, new_message)
    json_file_path = f"json_file/{file_name}.json"
    with open(json_file_path, "r") as f:
        actual_json = f.read()
    assert actual_json == expected_json
    os.remove(json_file_path)


@pytest.mark.parametrize(
    "file_content, expected_json, file_name, decrypted_message, user_choose",
    [
        (
            [
                {
                    "name": "secret",
                    "content": "guvf vf n arj zrffntr",
                    "rot_type": "rot_13",
                    "status": "Encrypting",
                }
            ],
            """[
    {
        "name": "secret",
        "content": "this is a new message",
        "rot_type": "rot_13",
        "status": "Decrypting"
    }
]""",
            "testa_decrypted_message",
            "this is a new message",
            0,
        ),
    ],
)
def test_should_save_decrypted_content(
    mock_files_dir,
    file_content,
    expected_json,
    file_name,
    decrypted_message,
    user_choose,
):
    SaveFile.save_decrypted_content(
        file_name, file_content, user_choose, decrypted_message
    )
    json_file_path = f"json_file/{file_name}.json"
    with open(json_file_path, "r") as f:
        actual_json = f.read()
    assert actual_json == expected_json
    os.remove(json_file_path)


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
