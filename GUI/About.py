from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QCoreApplication
from .generated.AboutPage import Ui_AboutPage

class About(QMainWindow):
    def __init__(self, diagnose):
        super().__init__()
        self.diagnose = diagnose

        ui = Ui_AboutPage()

        # Setup and retranslate the ui according to
        # pyuic5 generated uis.
        ui.setupUi(self)
        ui.retranslateUi(self)

        # Link the buttons to methods of the About class instance.
        ui.agree_button.clicked.connect(self.agree_button_clicked)
        ui.disagree_button.clicked.connect(QCoreApplication.instance().quit)

        self.show()

    def agree_button_clicked(self):
        self.diagnose.show()
        self.hide()
