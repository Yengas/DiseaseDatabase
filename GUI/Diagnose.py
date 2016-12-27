from PyQt5.QtWidgets import QMainWindow, QListWidgetItem
from .generated.DiagnosePage import Ui_DiagnosePage
from .BodyPartWidget import BodyPartWidget
from .ConditionWidget import ConditionWidget
from WebMD.diagnose import SimpleDiagnoser
from WebMD.models import BodyPart

class Diagnose(QMainWindow):
    def __init__(self, parts):
        super().__init__()

        # All parts, symptoms and conditions not to be modified.
        self._parts = parts

        self.picked = []
        self.ui = Ui_DiagnosePage()

        # Setup and retranslate the ui according to
        # pyuic5 generated uis.
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.initializePartCombo(parts)
        self.initializeSymptomCombo(parts[0])
        self.ui.add_symptom_button.clicked.connect(self.add_symptom)
        self.ui.body_part_combo.currentIndexChanged.connect(self.part_changed)

    # Pick the given part and symptom
    def pick_symptom(self, part, symptom):
        try:
            idx = self.picked.index(part)
            self.picked[idx].add_symptom(symptom)
        except(ValueError):
            newPart = BodyPart(id=part.id, name=part.name)
            newPart.add_symptom(symptom)
            self.picked.append(newPart)
        self.set_symptoms(self.picked)
        self.set_conditions(self.picked)


    # Returns part by filtering global parts.
    def getPartByName(self, name):
        name = name.strip()
        next(filter(lambda p: p.name.strip() == name, self._parts))

    # Add symptom to the picked list.
    def add_symptom(self):
        part = self._parts[self.ui.body_part_combo.currentIndex()]
        symptom = part.symptoms()[self.ui.symptom_combo.currentIndex()]
        self.pick_symptom(part, symptom)

    # Triggered on combobox parts change.
    def part_changed(self, idx):
        self.initializeSymptomCombo(self._parts[idx])

    # Initialize the combobox for part.
    def initializePartCombo(self, parts):
        self.ui.body_part_combo.clear()

        for part in parts:
            self.ui.body_part_combo.addItem(part.name)

    # Initialize the symptom combobox
    def initializeSymptomCombo(self, part):
        self.ui.symptom_combo.clear()

        for symptom in part.symptoms():
            self.ui.symptom_combo.addItem(symptom.name)

    # Set all symptoms by given parts and their symptoms.
    def set_symptoms(self, parts):
        self.ui.symptom_list_view.clear()

        for part in parts:
            widget = BodyPartWidget()
            widget.set(part)
            widgetItem = QListWidgetItem(self.ui.symptom_list_view)
            widgetItem.setSizeHint(widget.sizeHint())
            self.ui.symptom_list_view.addItem(widgetItem)
            self.ui.symptom_list_view.setItemWidget(widgetItem, widget)

    # Calculate conditions according to the given parts and their symptoms.
    def set_conditions(self, parts):
        diagnoser = SimpleDiagnoser()
        for part in parts:
            for symptom in part.symptoms():
                diagnoser.update(symptom)

        conditions = diagnoser.diagnose()
        self.ui.condition_list_view.clear()
        for condition in conditions:
            widget = ConditionWidget()
            widget.set(condition)
            widgetItem = QListWidgetItem(self.ui.condition_list_view)
            widgetItem.setSizeHint(widget.sizeHint())
            self.ui.condition_list_view.addItem(widgetItem)
            self.ui.condition_list_view.setItemWidget(widgetItem, widget)
