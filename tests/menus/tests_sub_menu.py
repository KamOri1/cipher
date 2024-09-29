from cipher.menus.sub_menu import SubMenu
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
def test_show_sub_menu_should_print_list_elements(
    menu_options, expected_output, capsys, mocker
):
    with mocker.patch("builtins.input", return_value="2"):
        SubMenu.show_sub_menu(menu_options)
        captured_output = capsys.readouterr().out

    assert captured_output == expected_output


@pytest.mark.parametrize(
    "menu_options",
    [
        (
            ["New message", "Open message", "Buffer", "Exit"],
            "1. New message\n2. Open message\n3. Buffer\n4. Exit\n",
        )
    ],
)
def test_show_sub_menu_should_return_value_2(menu_options, capsys, mocker):
    with mocker.patch("builtins.input", return_value="2"):
        result = SubMenu.show_sub_menu(menu_options)
        assert result == "2"
