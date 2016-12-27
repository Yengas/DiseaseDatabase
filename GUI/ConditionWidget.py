from PyQt5.QtWidgets import QWidget
from .generated.Condition import Ui_condition

class ConditionWidget(QWidget):
    def __init__(self, parent = None):
        super(ConditionWidget, self).__init__(parent)
        self.ui = Ui_condition()

        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    # Implement method to set condition from condition model
