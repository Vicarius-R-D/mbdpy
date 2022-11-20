from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication, QGraphicsTextItem
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from .model import Model


class App:
    def __init__(self, model: Model) -> None:
        self.app = QApplication([])
        # Defining a scene rect of 1280x720, with it's origin at 0, 0.
        # If we don't set this on creation, we can set it later with .setSceneRect
        scene = QGraphicsScene(0, 0, 1280, 720)

        for block in model.blocks:
            # Draw a rectangle item, setting the dimensions.
            rect = QGraphicsRectItem(0, 0, block.dimension[0], block.dimension[1])

            # Set the origin (position) of the rectangle in the scene.
            rect.setPos(block.coord[0], block.coord[1])

            # Define the brush (fill).
            brush = QBrush(Qt.white)
            rect.setBrush(brush)

            # Define the pen (line)
            pen = QPen(Qt.black)
            pen.setWidth(2)
            rect.setPen(pen)

            label = QGraphicsTextItem(parent=rect)
            label.setTextWidth(block.dimension[0])
            label.setHtml('<center>' + block.label + '</center>')

            scene.addItem(rect)
        self.view = QGraphicsView(scene)
        self.view.show()

    def execute(self):
        self.app.exec()
