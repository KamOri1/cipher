class Menu:
    OPTIONS = ['New message', 'Open message','Save buffer', 'Exite']

    @staticmethod
    def show_menu() -> None:
        for index, item in enumerate(Menu.OPTIONS, start=1):
            print(f'{index}. {item}')

    @staticmethod
    def get_choose() -> str:
        choose: str = input('What you want to do now? Choose 1-3: ')
        return choose
