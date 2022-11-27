import tkinter as tk

from enum import Enum
from model import Model # must be used .model


class C(Enum):
    GRAY = '#2A2D34'
    DARKGREEN = '#218380'
    LIGHTGREEN = '#8FD694'
    YELLOW = '#EEB902'
    ORANGE = '#F45D01'


class Gui:

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.frm_menu = tk.Frame(master=self.window, width=1280, height=60, bg=C.DARKGREEN.value)
        self.btn_load_model = tk.Button(master=self.frm_menu, width=10, command=self.load_model)
        self.btn_load_model.pack(side=tk.LEFT)
        self.frm_menu.pack(fill=tk.X)

        self.frm_model_container = tk.Frame(master=self.window, width=1280, height=660, bg=C.GRAY.value)
        self.frm_model_container.pack(fill=tk.BOTH, expand=True)

    def run(self) -> None:
        self.window.mainloop()

    def load_model(self) -> None:
        model = Model().load_json('models/trial_model.json')  # TODO add the file name in the gui 
        
        for block in model.blocks:
            btn_block = tk.Button(master=self.frm_model_container)
            btn_block.place(x=block.coord[0],
                            y=block.coord[1],
                            width=block.dimension[0],
                            height=block.dimension[1])


if __name__ == '__main__':
    gui = Gui()
    gui.run()