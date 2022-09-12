from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window





Window.size = (700, 600)


class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Registrar(Screen):
    pass

class Recepcionista(Screen):
    class Mesas(Screen):
        pass

class Cozinha(Screen):
    pass

class Gerente(Screen):
    pass



class Test3(App):
    def build(self):
        return Gerenciador()

Test3().run()