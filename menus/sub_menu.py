class SubMenu:
    @staticmethod
    def show_sub_menu(options) -> None:
        for index, item in enumerate(options, start=1):
            print(f'{index}. {item}')



