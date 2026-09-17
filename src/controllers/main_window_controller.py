from PySide6.QtWidgets import QMainWindow
from src.ui.main_window import Ui_MainWindow
from src.controllers.tabs.dashboard_tab_controller import DashboardTabController
from src.controllers.tabs.tangki_tab_controller import TangkiTabController
from src.controllers.tabs.dispensing_tab_controller import DispensingTabController
from src.functions.window_handler import WindowHandler

class MainWindowController(QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.opened_window = []
        
        self.ui.tabWidget.clear()
        
        self.DashboardTab = DashboardTabController()
        self.TangkiTab = TangkiTabController()
        self.DispensingTab = DispensingTabController()
        
        self.ui.tabWidget.addTab(self.DashboardTab, "Dashboard")
        self.ui.tabWidget.addTab(self.TangkiTab, "Tangki")
        self.ui.tabWidget.addTab(self.DispensingTab, "Pengisian")
        
        self.window_handler = WindowHandler()
        
        self.ui.actionAsset.triggered.connect(self.assets_menu_opener)
        self.ui.actionSupplier.triggered.connect(self.supplier_menu_opener)
        self.ui.actionTangki.triggered.connect(self.tangki_menu_opener)
     
    def assets_menu_opener(self):
        from src.controllers.menus.assets_menu_controller import AssetsMenuController
        self.window_handler.open_single_window(AssetsMenuController)
        
    def supplier_menu_opener(self):
        from src.controllers.menus.supplier_menu_controller import SupplierMenuController
        self.window_handler.open_single_window(SupplierMenuController)
        
    def tangki_menu_opener(self):
        from src.controllers.menus.tangki_menu_controller import TangkiMenuController
        self.window_handler.open_single_window(TangkiMenuController)