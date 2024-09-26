from cipher.files.reader import ReadFile
from cipher.files.saver import SaveFile
import pytest
import cipher.files.reader
import cipher.files.saver
import cipher.consts
import os


@pytest.fixture
def mock_files_dir(mocker):
    new_value = "json_file/"
    mocker.patch.object(cipher.files.reader, "FILES_DIR", new_value)
    mocker.patch.object(cipher.files.saver, "FILES_DIR", new_value)


@pytest.mark.parametrize(
    "all_message_information, expected_json, file_name",
    [
        (
            {
                "content": "something",
                "name": "new file",
                "rot_type": "rot13",
                "status": "Decrypting",
            },
            [
                {
                    "content": "something",
                    "name": "new file",
                    "rot_type": "rot13",
                    "status": "Decrypting",
                }
            ],
            "test_reader_1",
        ),
    ],
)
def test_read_file_should_return_json_file_with_json(
    mock_files_dir, all_message_information, expected_json, file_name
):
    SaveFile.save_message(all_message_information, file_name)
    function_return = ReadFile.read_file(file_name)
    json_file_path = f"json_file/{file_name}.json"

    assert function_return == expected_json
    os.remove(json_file_path)
