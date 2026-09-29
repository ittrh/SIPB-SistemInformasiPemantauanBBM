from PySide6.QtCore import Qt, QAbstractTableModel

class AssetsMenuTableModel(QAbstractTableModel):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._data = data or []
        self._header = ['Lokasi', 'Kode Asset', 'Nomor Plat', 'Tipe Kendaraan', 'Tipe BBM']
        
    def rowCount(self, parent = None):
        return len(self._data)
    
    def columnCount(self, parent = None):
        return len(self._header)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        
        row = self._data[index.row()]
        col = index.column()
        
        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0: return row.get("location_asset", "")
            if col == 1: return row.get("code_asset", "")
            if col == 2: return row.get("no_plat", "")
            if col == 3: return row.get("type_asset", "")
            if col == 4: return row.get("fuel_type", "")
        return None
    
    def headerData(self, section, orientation, role = Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._header[section]
        return None