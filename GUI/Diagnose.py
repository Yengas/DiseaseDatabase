from PyQt5.QtWidgets import QMainWindow, QListWidgetItem
from .generated.DiagnosePage import Ui_DiagnosePage
from .BodyPartWidget import BodyPartWidget

class Diagnose(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_DiagnosePage()

        # Setup and retranslate the ui according to
        # pyuic5 generated uis.
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.setSymptoms([{ 'name': 'test' }])

    def setSymptoms(self, parts):
        part = parts[0]
        widget = BodyPartWidget()
        widget.set(part)
        widgetItem = QListWidgetItem(self.ui.symptom_list_view)
        widgetItem.setSizeHint(widget.sizeHint())
        self.ui.symptom_list_view.addItem(widgetItem)
        self.ui.symptom_list_view.setItemWidget(widgetItem, widget)
        #self.ui.symptom_list_view.
