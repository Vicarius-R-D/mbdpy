from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QToolBar, QAction, QStatusBar, QCheckBox
from PyQt5.QtGui import QPalette, QColor, QIcon

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("MBDpy")

        layout1 = QHBoxLayout()

        lateral_menu = QWidget()
        lateral_menu.setMinimumWidth(520)
        lateral_menu.setMaximumWidth(520)
        lateral_menu.setMinimumHeight(1080)
        lateral_menu.setAutoFillBackground(True)
        palette = lateral_menu.palette()
        palette.setColor(QPalette.Window, QColor('grey'))
        lateral_menu.setPalette(palette)

        model_space = QWidget()
        model_space.setMinimumWidth(1400)
        model_space.setMinimumHeight(1080)
        model_space.setAutoFillBackground(True)
        palette = model_space.palette()
        palette.setColor(QPalette.Window, QColor('white'))
        model_space.setPalette(palette)

        layout1.addWidget(lateral_menu)
        layout1.addWidget(model_space)

        layout1.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

        button_action = QAction(QIcon("bug.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
    
    def onMyToolBarButtonClick(self, s):
        print("click", s)

class App:
    def __init__(self) -> None:
        self.app = QApplication([])
        self.window = MainWindow()
        self.window.show()

    def execute(self):
        self.app.exec()
