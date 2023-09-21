import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFrame
from main_ui import Ui_MainWindow  # Hier den richtigen Importpfad anpassen 
from speedtestWidget import MyForm 

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Erstelle eine Instanz der MyForm-Klasse aus speedtestWidget
        self.speedtest_widget = MyForm()

        # Finde das widgetFrame in deinem Hauptfenster
        self.widgetFrame = self.findChild(QFrame, 'widgetFrame')

        if self.widgetFrame:
            layout = QVBoxLayout()
            layout.addWidget(self.speedtest_widget)
            
            # Setzen Sie den Stretch-Faktor für das widgetFrame-Widget selbst
            layout.setStretchFactor(self.widgetFrame, 1)
            self.widgetFrame.setLayout(layout)

        self.ui.knopf1.clicked.connect(self.knopf1_gedrueckt)
        #self.showFullScreen()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def knopf1_gedrueckt(self):
        print("Knopf1 wurde gedrückt")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

