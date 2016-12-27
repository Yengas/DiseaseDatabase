from PyQt5.QtWidgets import QWidget, QListWidgetItem
from .generated.BodyPart import Ui_BodyPart
from .SymptomWidget import SymptomWidget

class BodyPartWidget(QWidget):
    def __init__(self, parent = None):
        super(BodyPartWidget, self).__init__(parent)
        self.ui = Ui_BodyPart()

        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    # Sets the body part to a specific body part
    def set(self, part):
        self.ui.body_part_label.setText(part.name)

        for symptom in part.symptoms():
            widget = SymptomWidget()
            widget.set(symptom)
            widgetItem = QListWidgetItem(self.ui.symptom_list)
            widgetItem.setSizeHint(widget.sizeHint())
            self.ui.symptom_list.addItem(widgetItem)
            self.ui.symptom_list.setItemWidget(widgetItem, widget)
