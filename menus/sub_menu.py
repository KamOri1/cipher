class SubMenu:
    @staticmethod
    def show_sub_menu(options: list) -> input:
        for index, item in enumerate(options, start=1):
            print(f'{index}. {item}')
        return input(f'Enter yours choose: 1-{len(options)} ')



