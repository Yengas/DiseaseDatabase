from PyQt5.QtWidgets import QWidget
from .generated.Symptom import Ui_Symptom

class SymptomWidget(QWidget):
    def __init__(self, parent = None):
        super(SymptomWidget, self).__init__(parent)
        self.ui = Ui_Symptom()

        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    # Set ui data from symptom.
    def set(self, symptom, method):
        self.symptom = symptom
        self.method = method
        self.ui.symptom_name.setText(symptom.name)
        self.ui.remove_button.clicked.connect(self.clicked)

    def clicked(self):
        self.method(self.symptom)
