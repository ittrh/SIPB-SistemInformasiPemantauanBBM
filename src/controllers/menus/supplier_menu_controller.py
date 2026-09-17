from PySide6.QtWidgets import QWidget
from src.ui.menus.supplier_menu import Ui_SupplierMenu

class SupplierMenuController(QWidget):
    def __init__(self):
        super(SupplierMenuController, self).__init__()
        self.ui = Ui_SupplierMenu()
        self.ui.setupUi(self)