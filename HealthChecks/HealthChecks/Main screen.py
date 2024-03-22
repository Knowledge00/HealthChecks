from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import QProcess
import sys
from subprocess import call
HCName = "hello"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Main Window')

        self.hc_name_entry = QLineEdit()
        self.Location = QLineEdit()
        self.diabetes_button = QPushButton('Diabetes Risk Checks')
        self.survey_button = QPushButton('Survey')
        self.everything_button = QPushButton('Everything')
        self.search_button = QPushButton('Search')

        layout = QVBoxLayout()
        layout.addWidget(self.Location)
        layout.addWidget(self.hc_name_entry)
        layout.addWidget(self.diabetes_button)
        layout.addWidget(self.survey_button)
        layout.addWidget(self.everything_button)
        layout.addWidget(self.search_button)

        self.diabetes_button.clicked.connect(lambda: call(["python", "hcsf.py","Diabetes",self.hc_name_entry.text(),self.Location.text()]))
        self.survey_button.clicked.connect(lambda: call(["python", "hcsf.py","Survey",self.hc_name_entry.text(),self.Location.text()]))
        self.everything_button.clicked.connect(lambda: call(["python", "hcsf.py","Everything",self.hc_name_entry.text(),self.Location.text()]))
        self.search_button.clicked.connect(lambda: call(["python", "hcsf.py","Search",self.hc_name_entry.text(),self.Location.text()]))

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())