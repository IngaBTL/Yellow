import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtGui import QPainter, QColor, QPen, qRgb, QPainterPath, QBrush
from PyQt5.QtCore import Qt, QPoint
from random import randint, choice


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.started = False
        
    def run(self):
        self.started = True
        self.update()
        
    def draw(self):
        if not self.started:
            return
        qp = QPainter()
        qp.begin(self)
        center = QPoint(randint(0, 400), randint(0, 400))
        qp.setBrush(Qt.yellow)
        r = randint(1, 200)
        qp.drawEllipse(center, r, r)
        qp.end()

    def paintEvent(self, event):  # обновление экрана
        self.draw()


# Запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
 