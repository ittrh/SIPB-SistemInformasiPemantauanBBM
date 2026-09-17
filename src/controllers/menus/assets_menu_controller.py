from PySide6.QtWidgets import QWidget
from src.ui.menus.assets_menu import Ui_AssetsMenu

class AssetsMenuController(QWidget):
    def __init__(self):
        super(AssetsMenuController, self).__init__()
        self.ui = Ui_AssetsMenu()
        self.ui.setupUi(self)