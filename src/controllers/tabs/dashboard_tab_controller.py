from PySide6.QtWidgets import QWidget
from src.ui.tabs.dashboard_tab import Ui_DashboardTab

class DashboardTabController(QWidget):
    def __init__(self):
        super(DashboardTabController, self).__init__()
        self.ui = Ui_DashboardTab()
        self.ui.setupUi(self)