from cipher.menus.content_menu import Menu
import pytest


@pytest.mark.parametrize(
    "menu_options, expected_output",
    [
        (
            ["New message", "Open message", "Buffer", "Exit"],
            "1. New message\n2. Open message\n3. Buffer\n4. Exit\n",
        )
    ],
)
def test_content_menu_should_print_list_elements(menu_options, expected_output, capsys):
    Menu.show_menu(menu_options)
    captured_output = capsys.readouterr().out

    assert captured_output == expected_output
