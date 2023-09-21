import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from speedtestWidget_ui import Ui_speedTest
import speedtest


knopfStyle = """border-radius: 5px;
    background-color: rgb(47, 47, 53);
    font: 10pt "Arial";
"""

class SpeedTestThread(QThread):
    speed_test_completed = pyqtSignal(float, float)
    speed_test_failed = pyqtSignal()

    def run(self):
        try:
            download_speed, upload_speed = speed_test()
            self.speed_test_completed.emit(download_speed, upload_speed)
        except Exception:
            self.speed_test_failed.emit()

class MyForm(QWidget):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_speedTest()
        self.ui.setupUi(self)
        self.ui.knopf.clicked.connect(self.knopf_gedrueckt)
        self.speed_thread = SpeedTestThread()
        self.speed_thread.speed_test_completed.connect(self.speed_test_completed)
        self.speed_thread.speed_test_failed.connect(self.speed_test_failed)
        self.ui.knopf.setEnabled(True)  # Knopf standardmäßig aktiviert

    def knopf_gedrueckt(self):
        self.ui.knopf.setStyleSheet(knopfStyle + "border: 2px solid #761A33; color: rgb(100, 100, 100);")
        self.ui.knopf.setEnabled(False)  # Deaktiviere den Knopf während des Tests
        self.ui.download.setText("Speedtest wird durchgeführt")
        self.ui.upload.setText("")
        self.speed_thread.start()

    def speed_test_completed(self, download_speed, upload_speed):
        self.ui.download.setText(f"Download: {download_speed:.2f} Mbps")
        self.ui.upload.setText(f"Upload: {upload_speed:.2f} Mbps")
        self.ui.knopf.setStyleSheet(knopfStyle + "border: 2px solid #F62A53; color: rgb(255, 255, 255);")
        self.ui.knopf.setEnabled(True)  # Aktiviere den Knopf nach Abschluss des Tests

    def speed_test_failed(self):
        self.ui.download.setText("Speedtest Fehlgeschlagen.")
        self.ui.upload.setText("")
        self.ui.knopf.setStyleSheet(knopfStyle + "border: 2px solid #F62A53; color: rgb(255, 255, 255);")
        self.ui.knopf.setEnabled(True)  # Aktiviere den Knopf nach einem fehlgeschlagenen Test

def speed_test():
    st = speedtest.Speedtest(secure=True)
    st.get_best_server()
    download_speed = st.download() / 10**6  # in Megabit pro Sekunde
    upload_speed = st.upload() / 10**6  # in Megabit pro Sekunde
    return download_speed, upload_speed

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())
