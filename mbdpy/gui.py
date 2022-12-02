import tkinter as tk

from enum import Enum
from .model import Model

class C(Enum):
    GRAY = '#2A2D34'
    DARKGREEN = '#218380'
    LIGHTGREEN = '#8FD694'
    YELLOW = '#EEB902'
    ORANGE = '#F45D01'


class Gui:
    """
    GUI class.
    """
    def __init__(self) -> None:
        self.model = Model()
        self.window = tk.Tk()
        self.window.title('MBDpy - ' + self.model.name)

        self.frm_menu = tk.Frame(master=self.window, width=1280, height=60, bg=C.DARKGREEN.value)

        self.btn_load_model = tk.Button(master=self.frm_menu, width=10, command=self.load_model, text='Load Model')
        self.btn_load_model.pack(side=tk.LEFT)

        self.str_model_name = tk.StringVar(master=self.window, value='models/trial_model.json')

        self.ent_model_name = tk.Entry(master=self.frm_menu, width=50, textvariable=self.str_model_name)
        self.ent_model_name.pack(side=tk.LEFT)

        self.frm_menu.pack(fill=tk.X)

        self.frm_model_container = tk.Frame(master=self.window, width=1280, height=660, bg=C.GRAY.value)
        self.frm_model_container.pack(fill=tk.BOTH, expand=True)

    def run(self) -> None:
        """
        Run the application GUI.
        """
        self.window.mainloop()

    def load_model(self) -> None:
        """
        Load the model from the GUI load model button.
        """
        self.model = Model().load_json(self.ent_model_name.get())
        self.window.title('MBDpy - ' + self.model.name)

        for block in self.model.blocks:
            btn_block = tk.Button(master=self.frm_model_container, text=block.label)
            btn_block.place(x=block.coord[0],
                            y=block.coord[1],
                            width=block.dimension[0],
                            height=block.dimension[1],
                            anchor=tk.CENTER)


if __name__ == '__main__':
    gui = Gui()
    gui.run()