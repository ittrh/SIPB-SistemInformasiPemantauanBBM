from PySide6.QtWidgets import QWidget
from src.ui.menus.assets_menu import Ui_AssetsMenu
from src.functions.menus.assets_menu_crud import AssetsMenuCrud

class AssetsMenuController(QWidget):
    def __init__(self):
        super(AssetsMenuController, self).__init__()
        self.ui = Ui_AssetsMenu()
        self.ui.setupUi(self)
        
        self.crud = AssetsMenuCrud()
        self.crud.load_data_assets()
        
    def simpan_handler(self):
        code_asset = self.ui.editKodeAsset.text()
        plat_no = self.ui.editPlatNomor.text()