from PySide6.QtWidgets import QWidget
from src.ui.menus.tangki_menu import Ui_TangkiMenu

class TangkiMenuController(QWidget):
    def __init__(self):
        super(TangkiMenuController, self).__init__()
        self.ui = Ui_TangkiMenu()
        self.ui.setupUi(self)