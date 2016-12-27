from PyQt5.QtWidgets import QWidget
from .generated.Condition import Ui_condition

class ConditionWidget(QWidget):
    def __init__(self, parent = None):
        super(ConditionWidget, self).__init__(parent)
        self.ui = Ui_condition()

        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    # Set fields to the given condition.
    def set(self, condition):
        self.ui.condition_name.setText(condition.name)
        self.ui.condition_about.setText(condition.about)
        self.ui.weight_value.setText(str(condition.weight))