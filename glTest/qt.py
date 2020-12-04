import sys
from PyQt5.QtWidgets import QWidget, QApplication
class Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()
    def setUi(self):
        self.setGeometry(10,10,200,200)
        self.setWindowTitle('Hi')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = Frame()
    app.exit(app.exec_())