from cipher.files.saver import SaveFile


def test_function_should_return_eEcrypting_str():
    value = "Decrypting"
    exp = "Encrypting"

    assert SaveFile.message_status(value) == exp  # nosec B101
