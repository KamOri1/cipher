class Menu:
    @staticmethod
    def show_menu(menu_options: list[str]) -> None:
        for index, item in enumerate(menu_options, start=1):
            print(f"{index}. {item}")

    @staticmethod
    def get_choose() -> str:
        choose: str = input("What you want to do now? Choose 1-4: ")
        return choose
