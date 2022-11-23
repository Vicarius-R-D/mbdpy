from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

from enum import Enum
from model import Model

import json


class C(Enum):
    GRAY = (42/255, 45/255, 52/255, 1)
    DARKGREEN = (33/255, 131/255, 128/255, 1)
    LIGHTGREEN = (143/255, 214/255, 148/255, 1)
    YELLOW = (238/255, 185/255, 2/255, 1)
    ORANGE = (244/255, 93/255, 1/255, 1)


def assign_color(color: C) -> Color:
    return Color(color.value[0], color.value[1], color.value[2], color.value[3]) 


class MainWindow(BoxLayout):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.add_widget(TopMenu())
        self.add_widget(ModelContainer())


class TopMenu(StackLayout):

    def __init__(self, **kwargs):
        super(TopMenu, self).__init__(**kwargs)

        load_button = Button(text='load model',
                             width=100,
                             height=50,
                             size_hint=(None, None),
                             background_color=C.DARKGREEN.value,
                             background_normal='')

        load_button.bind(on_press=ModelContainer.load_model)

        self.add_widget(load_button)


class ModelContainer(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(ModelContainer, self).__init__(**kwargs)

    def load_model(instance) -> None:
        model = Model().load_json('models/trial_model.json')  # TODO add the file name in the gui 
        print(model.blocks)

    def add_blocks(self, model: Model):
        for block in model.blocks:
            self.add_widget(Button(text = block.label,
                                   size_hint = (block.dimension[0], block.dimension[1]),
                                   pos_hint = {'center_x': block.coord[0], 'center_y': block.coord[1]}))


class GUI(App):

    def build(self):
        self.root = root = MainWindow()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            assign_color(C.GRAY)
            self.rect = Rectangle(size = root.size, pos = root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    GUI().run()