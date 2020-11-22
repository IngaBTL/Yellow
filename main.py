import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtGui import QPainter, QColor, QPen, qRgb, QPainterPath, QBrush
from PyQt5.QtCore import Qt, QPoint
from random import randint, choice
from ui_file import Ui_Form

def get_random_color():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return QColor(qRgb(r, g, b))


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        # color = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(get_random_color())
        center = QPoint(randint(0, 400), randint(0, 400))
        # qp.setBrush(Qt.yellow)
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
 