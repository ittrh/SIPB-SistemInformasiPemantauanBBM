from PySide6.QtWidgets import QWidget, QComboBox, QMessageBox, QCompleter, QHeaderView, QAbstractItemView
from PySide6.QtCore import Qt

from src.ui.menus.assets_menu import Ui_AssetsMenu
from src.functions.menus.assets_menu.assets_menu_crud import AssetsMenuCrud
from src.functions.menus.assets_menu.assets_menu_table_model import AssetsMenuTableModel
from src.functions.combo_btn_list import ComboBtnList

class AssetsMenuController(QWidget):
    def __init__(self):
        super(AssetsMenuController, self).__init__()
        self.ui = Ui_AssetsMenu()
        self.ui.setupUi(self)
        
        self.combolist = ComboBtnList()
        self.setup_comboboxes()
        self.load_master_combobox()
        
        self.crud = AssetsMenuCrud()
        self.crud.load_data_assets()
        
        self.load_table_data()
        self.ui.editCariDataAsset.textChanged.connect(self.search_handler)
        
        self.ui.btnSimpan.clicked.connect(self.simpan_handler)
        
    def setup_comboboxes(self):
        combos: list[QComboBox] = [
            self.ui.comboTipeKendaraan,
            self.ui.comboLokasiKendaraan,
            self.ui.comboTipeBBM
        ]
        for combo in combos:
            combo.setEditable(True)
            combo.setInsertPolicy(QComboBox.NoInsert)
            
            # Buat QCompleter baru jika belum ada untuk menghindari AttributeError
            if not combo.completer():
                completer = QCompleter(combo)
                combo.setCompleter(completer)
            
            combo.completer().setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
            combo.completer().setFilterMode(Qt.MatchContains)
        
    def load_master_combobox(self):
        fuel_types = self.combolist.fuel_type_list()
        self.combolist.populate_combobox(self.ui.comboTipeBBM, fuel_types, display_key="type", placeholder="Pilih Tipe BBM")
        
        asset_type = self.combolist.asset_type_list()
        self.combolist.populate_combobox(self.ui.comboTipeKendaraan, asset_type, display_key="type", placeholder="Pilih Tipe Kendaraan")
        
        location = self.combolist.location_list()
        self.combolist.populate_combobox(self.ui.comboLokasiKendaraan, location, display_key="name", placeholder="Pilih Lokasi Operasional")
    
    def simpan_handler(self):
        code_asset = self.ui.editKodeAsset.text().strip()
        plat_no = self.ui.editPlatNomor.text().strip().upper()
        selected_fuel_type_id = self.ui.comboTipeBBM.currentData()
        selected_asset_type_id = self.ui.comboTipeKendaraan.currentData()
        selected_location_id = self.ui.comboLokasiKendaraan.currentData()
        
        if not code_asset and not plat_no:
            QMessageBox.warning(self, "Peringatan", "Identitas Kendaraan Harus Jelas")
            return
        if not selected_fuel_type_id:
            QMessageBox.warning(self, "Peringatan", "Silahkan pilih Tipe BBM!")
            return
        if not selected_asset_type_id:
            QMessageBox.warning(self, "Peringatan", "Silahkan pilih Tipe Kendaraan!")
            return
        if not selected_location_id:
            QMessageBox.warning(self, "Peringatan", "Silahkan pilih Lokasi Operasional Kendaraan!")
            return
        
        param_dict = {
            "home_location_id": selected_location_id,
            "code_asset": code_asset,
            "no_plat": plat_no,
            "asset_type_id": selected_asset_type_id,
            "fuel_type_id": selected_fuel_type_id
        }
        
        try:
            self.crud.create_asset(param_dict)
            QMessageBox.information(self, "Berhasil", "Data Asset berhasil disimpan!")
            
            self.reset_form()
            self.load_table_data()
        except ValueError as e:
            QMessageBox.warning(self, "Peringatan", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error Database", f"Gagal menyimpan data: {e}")
            
    def reset_form(self):
        self.ui.comboTipeBBM.setCurrentIndex(0)
        self.ui.comboTipeKendaraan.setCurrentIndex(0)
        self.ui.comboLokasiKendaraan.setCurrentIndex(0)
        self.ui.editKodeAsset.clear()
        self.ui.editPlatNomor.clear()
        
    def load_table_data(self, data_assets=None):
        self.ui.editCariDataAsset.clear()
        if data_assets is None:
            data_assets = self.crud.assets_data_view
        self.model = AssetsMenuTableModel(data_assets, parent=self)
        self.ui.tableDataAsset.setModel(self.model)
        header = self.ui.tableDataAsset.horizontalHeader()
        self.ui.tableDataAsset.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableDataAsset.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        
        
        # Sesuaikan dengan jumlah kolom pada model tabel
        for col_index in range(5):
            header.setSectionResizeMode(col_index, QHeaderView.Stretch)
            
    def search_handler(self):
        keyword = self.ui.editCariDataAsset.text().strip()
        if keyword:
            table_data = self.crud.search_data_asset(keyword)
            self.load_table_data(table_data)
        else:
            self.load_table_data()