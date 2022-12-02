import tkinter as tk
import matplotlib.pyplot as plt

from enum import Enum
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from .model import Model


WINDOW_W = 1280
WINDOW_H = 720
MENU_H = 60
BODY_H = WINDOW_H - MENU_H
RESULTS_LOGGER_W = 500
MODEL_CONTAINER_W = WINDOW_W - RESULTS_LOGGER_W


class C(Enum):
    GRAY = '#2A2D34'
    LIGHTGRAY = '#525866'
    DARKGREEN = '#218380'
    LIGHTGREEN = '#8FD694'
    YELLOW = '#EEB902'
    ORANGE = '#F45D01'


class Gui:
    """
    GUI class.
    """
    def __init__(self) -> None:
        # create blank model
        self.model = Model()
        
        # window
        self.window = tk.Tk()
        self.window.title('MBDpy - ' + self.model.name + '*')

        # top menu frame
        self.frm_menu = tk.Frame(master=self.window,
                                 width=WINDOW_W,
                                 height=MENU_H,
                                 bg=C.DARKGREEN.value)

        # save model button
        self.btn_save_model = tk.Button(master=self.frm_menu,
                                        width=10,
                                        height=2,
                                        command=self.save_model,
                                        text='Save Model',
                                        bd=0)
        self.btn_save_model.pack(side=tk.LEFT)

        # load model button
        self.btn_load_model = tk.Button(master=self.frm_menu,
                                        width=10,
                                        height=2,
                                        command=self.load_model,
                                        text='Load Model',
                                        bd=0)
        self.btn_load_model.pack(side=tk.LEFT, padx=1)

        # loading model name
        self.str_model_name = tk.StringVar(master=self.window,
                                           value='models/trial_model.json')
        self.ent_model_name = tk.Entry(master=self.frm_menu,
                                       width=50,
                                       textvariable=self.str_model_name,
                                       bd=0)
        self.ent_model_name.pack(side=tk.LEFT, padx=5)

        # run button
        self.btn_run_model = tk.Button(master=self.frm_menu,
                                       width=5,
                                       height=2,
                                       command=self.run_model,
                                       text='run',
                                       bd=0)
        self.btn_run_model.pack(side=tk.RIGHT)

        # pack top menu frame
        self.frm_menu.pack(fill=tk.X)

        # model container frame
        self.frm_model_container = tk.Frame(master=self.window,
                                            width=MODEL_CONTAINER_W,
                                            height=BODY_H,
                                            bg=C.GRAY.value)

        # results logger frame
        self.frm_results_logger = tk.Frame(master=self.window,
                                           width=RESULTS_LOGGER_W,
                                           height=BODY_H,
                                           bg=C.LIGHTGRAY.value)
        self.frm_results_logger.pack(side=tk.RIGHT, fill=tk.Y)

        # pack model container frame                               
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
            btn_block = tk.Button(master=self.frm_model_container,
                                  text=block.label,
                                  bd=0)
            btn_block.place(x=block.coord[0],
                            y=block.coord[1],
                            width=block.dimension[0],
                            height=block.dimension[1],
                            anchor=tk.CENTER)

    def save_model(self) -> None:
        """
        Save the model from the GUI save model button.
        """
        self.model.save_json()
        self.window.title('MBDpy - ' + self.model.name)

    def run_model(self) -> None:
        """
        Run the simulation with the actual model and call the plot function.
        """
        self.model.run(10, 0.1)  # TODO parameters controllable from the GUI
        self.plot_channel()

    def plot_channel(self) -> None:
        """
        PLot the desired channel.
        """
        t = self.model.time
        x = self.model.outputs[0]  # TODO choose which channel has to be plotted
        
        fig = plt.Figure(figsize=(5, 5), dpi=100)
        fig.patch.set_facecolor(C.LIGHTGRAY.value)
        ax1 = fig.add_subplot(111)
        ax1.plot(t, x)
        ax1.set_title('Simulation Results')
        ax1.set_xlabel('time [s]')
        ax1.grid(True)

        self.fig_results = FigureCanvasTkAgg(fig, self.frm_results_logger)
        
        toolbar = NavigationToolbar2Tk(self.fig_results, self.frm_results_logger)
        toolbar.update()

        self.fig_results.get_tk_widget().pack(side=tk.BOTTOM)