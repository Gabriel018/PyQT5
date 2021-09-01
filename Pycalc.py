
import  sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit

__Author__ = "Duke"

class pycalc(QMainWindow):

 def __init__(self):

    super().__init__()
    self.setWindowTitle("Calculadora")
    self.setFixedSize(400,400)
    self._centralwidget = QWidget(self)
    self.setCentralWidget(self._centralwidget)
    self.PrincLayout = QVBoxLayout()
    self._centralwidget.setLayout(self.PrincLayout)
    self.createDisplay()
    self.createButtons()

 def createDisplay(self):
     self.display = QLineEdit()
     self.display.setFixedHeight(20)
     self.display.setAlignment(Qt.AlingRight)
     self.display.setReadOnly(True)
     self.PrincLayout.addWidget(self.display)
def main():

     calc = QApplication(sys.argv)
     view = pycalc()
     view.show()
     sys.exit(calc.exec_())

if __name__ == '__main__':
     main()