import sys
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFrame
from main_ui import Ui_MainWindow  # Hier den richtigen Importpfad anpassen 
from speedtestWidget import MyForm 

UHRZEIT_MIT_SEKUNDEN = True

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

        # topbar
        self.uhrzeit_aktualisieren()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.uhrzeit_aktualisieren)
        self.timer.start(1000)
        # --- 

        #self.showFullScreen()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def knopf1_gedrueckt(self):
        print("Knopf1 wurde gedrückt")

    def uhrzeit_aktualisieren(self):
        aktuelle = QDateTime.currentDateTime()
        if UHRZEIT_MIT_SEKUNDEN:
            uhrzeit = aktuelle.toString("hh:mm:ss")
        else:
            uhrzeit = aktuelle.toString("hh:mm")
        self.ui.uhrzeitLabel.setText(uhrzeit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

