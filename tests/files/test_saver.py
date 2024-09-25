from cipher.files.saver import SaveFile


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
