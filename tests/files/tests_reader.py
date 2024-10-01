from files.reader import ReadFile
from files.saver import SaveFile
import pytest
import files.reader
import files.saver
import os


@pytest.fixture
def mock_files_dir(mocker):
    new_value = ""
    mocker.patch.object(files.reader, "FILES_DIR", new_value)
    mocker.patch.object(files.saver, "FILES_DIR", new_value)


class TestReader:
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
        self, mock_files_dir, all_message_information, expected_json, file_name
    ):
        SaveFile.save_message(all_message_information, file_name)
        function_return = ReadFile.read_file(file_name)
        json_file_path = f"{file_name}.json"

        assert function_return == expected_json
        os.remove(json_file_path)

    @pytest.mark.parametrize(
        "file_name, file_content, expected_output",
        [
            ("file", [], "List of message in file: 'file.json'\n"),
            (
                "test_file",
                [
                    {
                        "name": "new file",
                        "content": "something",
                        "rot_type": "rot13",
                        "status": "Decrypting",
                    }
                ],
                "List of message in file: 'test_file.json'\n1: {'name': 'new file', 'content': 'something', 'rot_type': 'rot13', 'status': 'Decrypting'}\n",
            ),
        ],
    )
    def test_print_file_content(self, file_name, file_content, expected_output, capsys):
        ReadFile.print_file_content(file_name, file_content)
        captured_output = capsys.readouterr().out

        assert captured_output == expected_output
