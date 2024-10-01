from menus.content_menu import Menu
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
def test_show_menu_should_print_list_elements(menu_options, expected_output, capsys):
    Menu.show_menu(menu_options)
    captured_output = capsys.readouterr().out

    assert captured_output == expected_output


@pytest.mark.parametrize(
    "user_choose, expected_output",
    [(1, 1)],
)
def test_get_choose_should_return_expected_value(user_choose, expected_output, mocker):
    mocker.patch("cipher.menus.content_menu.Menu.get_choose", return_value=user_choose)
    Menu.choose = user_choose

    result = Menu.get_choose()

    assert result == expected_output


def test_get_choose_valid_input(mocker):
    with mocker.patch("builtins.input", return_value="2"):
        result = Menu.get_choose()
        assert result == "2"
