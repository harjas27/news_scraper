import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        qbtn = QPushButton('Nation', self)
        qbtn.resize(150,60)
        qbtn.move(0, 0)      

        qbtn = QPushButton('World', self)
        qbtn.resize(150,60)
        qbtn.move(160, 0) 

        qbtn = QPushButton('City', self)
        qbtn.resize(150,60)
        qbtn.move(320, 0) 

        qbtn = QPushButton('Sport', self)
        qbtn.resize(150,60)
        qbtn.move(480, 0) 
        
        self.setGeometry(10, 30, 630, 640)
        self.setWindowTitle('Quit button')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())