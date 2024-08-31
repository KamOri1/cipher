from content_menu import Menu

class MenuManager(Menu):
    def __init__(self, new_message, open_message, exite):
        super().__init__()
        self.new_message = new_message
        self.open_message = open_message
        self.exite = exite
        self.menu_options = {'1' : self.new_message, '2' : self.open_message, '3' : self.exite}
        self.start_menu()

    def start_menu(self):
            while True:
                first_choose = self.show_menu()
                self.menu_options[first_choose]


    def show_menu(self):
        Menu().show_menu()
        return self.execute()

    def execute(self):
        return super().get_choose()

a = MenuManager(1,1,1,)
