import sys
from GUI.About import About
from GUI.Diagnose import Diagnose
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    diagnose = Diagnose()
    about = About(diagnose)
    about.show()
    sys.exit(app.exec_())