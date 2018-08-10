
from PyQt.Qtcore import *
from PyQt.QtGui import *

#class testPixMap(QWidget):
#    def __init__(self):
#
#        self.label = QLabel()
#        self.pixmap = Pixmap()
#        self.label.setPixmap(self.pixmap)

def window():
    app = QApplication(sys.argv)
    win = Qwidget()
    l1 = QLabel()
    l1.setPixmap(QPixmap())

    vbox = QVBixLayout()
    vbox.addWdiget(l1)
    win.setLayout(vbox)
    win.setWindowTitle("test")
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
