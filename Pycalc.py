
import  sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt

__Author__ = "Duke"

class pycalc(QMainWindow):

 def __init__(self):

    super().__init__()
    self.setWindowTitle("Calculadora")
    #self.setFixedSize(400,400)
    self._centralwidget = QWidget(self)
    self.setCentralWidget(self._centralwidget)
    self.PrincLayout = QVBoxLayout()
    self._centralwidget.setLayout(self.PrincLayout)
    self.createDisplay()
    self.createButtons()

 def Setdiplay(self,text):
     self.display.setText(text)
     self.display.setFocus()

 def  DisplayTExt(self):
    return self.display.text()

 def Cleardisplay(self):
     self.Setdiplay("")
 def createButtons(self):
   self.buttons = {}
   buttonsLayout = QGridLayout()
   buttons = {
       "1":(0,0),
       "2":(0,1),
       "3": (0,2),
       "4": (0,3),
       "5": (1,0),
       "6": (1,1),
       "7": (1,2),
       "8": (1,3),
   }

   for BtnTxt,  pos in buttons.items():
       self.buttons[BtnTxt] = QPushButton(BtnTxt)
       self.buttons[BtnTxt].setFixedSize(40,40)
       buttonsLayout.addWidget(self.buttons[BtnTxt],pos[0],pos[1])
       self.PrincLayout.addLayout(buttonsLayout)



 def createDisplay(self):
     self.display = QLineEdit()
     self.display.setFixedHeight(20)
     self.display.setAlignment(Qt.AlignRight)
     self.display.setReadOnly(True)
     self.PrincLayout.addWidget(self.display)
def main():

     calc = QApplication(sys.argv)
     view = pycalc()
     view.show()
     sys.exit(calc.exec_())

if __name__ == '__main__':
     main()