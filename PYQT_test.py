import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class CounterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Zähler-App')
        self.setGeometry(100, 100, 300, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.counter_label = QLabel('0', self)
        self.counter_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.counter_label)

        self.increment_button = QPushButton('Erhöhen', self)
        self.increment_button.clicked.connect(self.increment_counter)
        self.layout.addWidget(self.increment_button)

        self.central_widget.setLayout(self.layout)

        self.counter = 0

    def increment_counter(self):
        self.counter += 1
        self.counter_label.setText(str(self.counter))

def main():
    app = QApplication(sys.argv)
    window = CounterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
