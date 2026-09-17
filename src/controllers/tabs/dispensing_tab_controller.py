from PySide6.QtWidgets import QWidget
from src.ui.tabs.dispensing_tab import Ui_DispensingTab

class DispensingTabController(QWidget):
    def __init__(self):
        super(DispensingTabController, self).__init__()
        self.ui = Ui_DispensingTab()
        self.ui.setupUi(self)