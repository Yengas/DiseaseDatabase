from PyQt5.QtWidgets import QWidget
from .generated.Symptom import Ui_Symptom

class SymptomWidget(QWidget):
    def __init__(self, parent = None):
        super(SymptomWidget, self).__init__(parent)
        self.ui = Ui_Symptom()

        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    # Set ui data from symptom.
    def set(self, symptom):
        self.ui.symptom_name.setText(symptom.name)
