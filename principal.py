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
    pass

class Cozinha(Screen):
    pass

class Gerente(Screen):
    pass

class Tarefas(Screen):
    def __init__(self,tarefas=[],**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ''

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test3(App):
    def build(self):
        return Gerenciador()

Test3().run()