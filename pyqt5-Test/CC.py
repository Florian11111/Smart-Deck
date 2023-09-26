import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from CC_ui import Ui_ComputerControll


class MyForm(QWidget):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_ComputerControll()
        self.ui.setupUi(self)
        self.ui.widgetStack.setCurrentIndex(0)
        self.ui.knopf1.clicked.connect(self.zuLautstaerke)
        # self.ui.knopf.clicked.connect(self.knopf_gedrueckt)

    def zuLautstaerke(self):
        self.ui.widgetStack.setCurrentIndex(1)
        self.istVerbunden()

    def istVerbunden(self):
        pass
        # schickt anfrage an restserver
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())
