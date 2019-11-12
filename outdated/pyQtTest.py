from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("This is the title")
        self.initUI()


    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Button1")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()




# def clicked():
#     print("clicked")

# def window():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setGeometry(200, 200, 300, 300)
#     win.setWindowTitle("This is the title")

#     # label = QtWidgets.QLabel(win)
#     # label.setText("my label")
#     # label.move(50, 50)

#     # b1 = QtWidgets.QPushButton(win)
#     # b1.setText("Button1")
#     # b1.clicked.connect(clicked)


#     win.show()
#     sys.exit(app.exec_())

# window()

