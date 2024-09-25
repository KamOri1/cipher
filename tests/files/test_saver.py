from cipher.files.saver import SaveFile


def test_should_return_decrypting_str():
    value = "Encrypting"
    exp = "Decrypting"

    assert SaveFile.message_status(value) == exp


def test_should_return_encrypting_str():
    value = "Decrypting"
    exp = "Encrypting"

    assert SaveFile.message_status(value) == exp  # no
