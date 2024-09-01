class Menu:
    def show_menu(self)-> None:
        menu_list : list = ['New message', 'Open message', 'Exite']
        for index, item in enumerate(menu_list, start=1):
            print(f'{index}. {item}')

    def get_choose(self)-> str:
        choose : str = input('What you want to do now? Choose 1-3: ')
        return choose
