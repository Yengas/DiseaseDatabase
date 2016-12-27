from PyQt5.QtWidgets import QWidget
from .generated.BodyPart import Ui_BodyPart

class BodyPartWidget(QWidget):
    def __init__(self, parent = None):
        super(BodyPartWidget, self).__init__(parent)
        self.ui = Ui_BodyPart()

        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    # Sets the body part to a specific body part
    def set(self, part):
        self.ui.body_part_label.setText(part['name'])

