import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QGridLayout, QTabWidget, QLabel, QLineEdit, QDateTimeEdit, QPushButton, QComboBox, QDateEdit, QCompleter
from PyQt6.QtCore import Qt, QDateTime, QDate
from subprocess import call
from datetime import date, datetime

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Health Check Screening Form')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)

        # personal page
        personal_page = QWidget(self)
        layout = QGridLayout()
        personal_page.setLayout(layout)

        name = QLineEdit(self)
        layout.addWidget(QLabel('Full Name:'), 0, 0)
        layout.addWidget(name, 0, 1)

        consent_cb = QComboBox(self)
        consent_cb.addItems(['No', 'Yes'])
        layout.addWidget(QLabel('Do you give consent for a non-identifiable record\nof your health check to be included in a report?'), 0, 2)
        layout.addWidget(consent_cb, 0, 3)

        postcode = QLineEdit(self)
        layout.addWidget(QLabel('First half of postcode:'), 1, 0)
        layout.addWidget(postcode, 1, 1)

        gp_register = QComboBox(self)
        gp_register.addItems(['Yes', 'No','Yes - but a GP outside of Croydon'])
        layout.addWidget(QLabel('Are you registered with a Croydon GP?'), 2, 2)
        layout.addWidget(gp_register, 2, 3)

        gp = QLineEdit()
        GpSurgies = [
    "Portland Medical Centre",
    "The Farley Road Surgery",
    "The Forestdale Branch",
    "Upper Norwood Group Practice",
    "New Addington Group Practice",
    "Fieldway Medical Centre",
    "Violet Lane Medical Practice",
    "The Addiscombe Road Surgery",
    "Northway Road Surgery",
    "Norbury Health Centre",
    "South Norwood Hill Medical Centre",
    "North Croydon Medical Centre",
    "St James' Medical Practice",
    "Castle Hill Surgery",
    "Old Coulsdon Medical Practice",
    "Queenhill Medical Practice",
    "Parkside Group Practice",
    "Keston & Moorings Medical Practice",
    "The Moorings Medical Practice",
    "Brigstock and South Norwood Medical Partnership",
    "The Selsdon Park Medical Practice",
    "Mitchley Avenue Surgery",
    "Friends' Road Medical Practice",
    "Eversley Medical Practice",
    "London Road Medical Practice",
    "Thornton Heath Medical Centre",
    "Morland Road Surgery",
    "Woodcote Medical",
    "Coulsdon Branch",
    "Parkway Health Centre",
    "Addington Medical Practice",
    "Gravel Hill Surgery",
    "Hartland Way Surgery",
    "Broom Road Medical Practice",
    "The Haling Park Partnership",
    "Ashburton Park Medical Centre",
    "The Whitehorse Practice",
    "Auckland Surgery",
    "Stovell House Surgery",
    "Mitchley Avenue Surgery",
    "Leander Road Primary Care Centre",
    "Shirley Medical Centre",
    "East Croydon Medical Practice",
    "Medics Headley Drive Surgery",
    "Medics Thornton Road Surgery & Valley Park Surgery",
    "Bramley Avenue Surgery",
    "Parchmore Medical Centre",
    "Brigstock Family Practice",
    "Broughton Corner Family Practice",
    "Mersham Medical Centre",
    "Selhurst Medical Centre",
    "Fairview Medical Centre",
    "Broughton Corner Family Practice",
    "The Birdhurst Medical Practice",
    "Greenside Group Practice",
    "Edridge Road Community Health Centre",
    "Country Park Practice",
    "Denmark Road Surgery"]
        completer = QCompleter(GpSurgies)
        gp.setCompleter(completer)
        layout.addWidget(QLabel('Name of your GP surgery:'), 2, 0)
        layout.addWidget(gp, 2, 1)

        sex = QComboBox(self)
        sex.addItems(['Male', 'Female'])
        layout.addWidget(QLabel('What is your sex?'), 3, 2)
        layout.addWidget(sex, 3, 3)

        dob = QDateEdit(self)
        layout.addWidget(QLabel('What is your date of birth?'), 3, 0)
        layout.addWidget(dob, 3, 1)

        ethnicity = QComboBox(self)
        ethnicity.addItems(['White', 'Black', 'South Asian', 'Chinese', 'Mixed Ethnicity', 'Other'])
        ethnicity.setCurrentIndex(-1)
        layout.addWidget(QLabel('Ethnic Background'), 1, 2)
        layout.addWidget(ethnicity, 1, 3)

        # health check page
        hc_page = QWidget(self)
        layout = QGridLayout()
        hc_page.setLayout(layout)

        dia_hist = QComboBox(self)
        dia_hist.addItems(['Yes','No'])
        layout.addWidget(QLabel('Do you have a parent, brother, sister and/or own child with diabetes?'), 0, 0)
        layout.addWidget(dia_hist, 0, 1)
        dia_hist.setCurrentIndex(-1)

        bp_hist = QComboBox(self)
        bp_hist.addItems(['Yes','No'])
        layout.addWidget(QLabel('Has a doctor ever told you that you have high blood pressure, or given you medication for it?'), 0, 2)
        layout.addWidget(bp_hist, 0, 3)
        bp_hist.setCurrentIndex(-1)

        waist = QLineEdit(self)
        layout.addWidget(QLabel('Waist Measurement, cm'), 1, 0)
        layout.addWidget(waist, 1, 1)

        height = QLineEdit(self)
        layout.addWidget(QLabel('Height, cm'), 1, 2)
        layout.addWidget(height, 1, 3)

        weight = QLineEdit(self)
        layout.addWidget(QLabel('Weight, kg'), 2, 0)
        layout.addWidget(weight, 2, 1)

        self.show()


        # add pane to the tab widget
        tab.addTab(personal_page, 'Personal Info')
        tab.addTab(hc_page, 'Health Check')

        main_layout.addWidget(tab, 0, 0, 2, 1)
        SaveB = QPushButton('Save')
        SaveB.clicked.connect(lambda: self.DataTransfer(name.text(), consent_cb.currentText(), postcode.text(), gp_register.currentText(), gp.text(), sex.currentText(), dob,
                                                        ethnicity.currentText(),dia_hist.currentText(),bp_hist.currentText(),waist.text(),
                                                        height.text(),weight.text()))
        main_layout.addWidget(SaveB, 2, 0,
                              alignment=Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(QPushButton('Cancel'), 2, 0,
                              alignment=Qt.AlignmentFlag.AlignRight)

    def PersonalInfo_EH(self,name, consent_cb, name_hc, postcode, gp_register, gp, sex, dob, ethnicity): #Personal info exception handling
        return True

    def DataTransfer(self,name, consent_cb, postcode, gp_register, gp, sex, dob, ethnicity, dia_hist, bp_hist, waist, height, weight): # Sends data to python file, webscrape.py
        dob = dob.date()
        dob = dob.toString('dd/MM/yyyy')
        now = now.date()
        now = now.toString('dd/MM/yyyy')
        birthdate = datetime.strptime(dob, "%d/%m/%Y")
        age = calculateAge(birthdate)
        if self.PersonalInfo_EH(name, consent_cb, postcode, gp_register, gp, sex, dob, ethnicity) == True:
            call(["python", "webscrape.py",name, consent_cb, postcode, gp_register, gp, sex, str(age), ethnicity, dia_hist, bp_hist, waist, height,weight])
        else:
            self.PersonalInfo_EH(name, consent_cb, postcode, gp_register, gp, sex, dob, ethnicity)

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())