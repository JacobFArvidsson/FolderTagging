import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("APA")
    window.setGeometry(400,50,400,400)
    window.show()
    sys.exc_info(app.exec_())

    print("hejsan")

window()