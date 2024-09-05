class SubMenu:
    NEW_MESSAGE_OPTIONS = ['Add next message', 'Save message']
    SAVE_OPTIONS = ['One message one file', 'All in one file ']


    @staticmethod
    def show_sub_menu(options) -> None:
        for index, item in enumerate(options, start=1):
            print(f'{index}. {item}')

    @staticmethod
    def get_choose() -> str:
        choose: str = input('What you want to do now? Choose 1-2: ')
        return choose
