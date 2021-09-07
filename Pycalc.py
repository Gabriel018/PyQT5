
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

from functools import  partial

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

 def Setdisplay(self,text):
     self.display.setText(text)
     self.display.setFocus()

 def  DisplayTExt(self):
    return self.display.text()

 def Cleardisplay(self):
     self.Setdisplay("")
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
       "+": (2,0),
       "-": (2,1),
       "*": (2,2),
       "/": (2,3),
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
     Cal_controller(view=view)
     sys.exit(calc.exec_())


class Cal_controller():
    #Connecta os comandos aos Botoes
    def __init__(self,view):
        self._view = view
        self.connsignal()
    def buldingexpres(self,exp):
        expression = self._view.DisplayTExt() + exp
        self._view.Setdisplay(expression)
    def connsignal(self):

        for BtnTxt , btn in self._view.buttons.items():
            if BtnTxt not in {'=', 'C'}:
                btn.clicked.connect(partial(self.buldingexpres,BtnTxt))





if __name__ == '__main__':
     main()