from PySide6.QtWidgets import QWidget
from src.ui.tabs.tangki_tab import Ui_TangkiTab

class TangkiTabController(QWidget):
    def __init__(self):
        super(TangkiTabController, self).__init__()
        self.ui = Ui_TangkiTab()
        self.ui.setupUi(self)