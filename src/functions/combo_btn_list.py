from databases.sqlite_db import get_db_session
from databases.models.masters import FuelTypes, AssetTypes, Locations, Tanks, Assets, Suppliers
from PySide6.QtWidgets import QComboBox

class ComboBtnList:
    def fuel_type_list(self) -> list[dict]:
        with get_db_session() as session:
            data = session.query(FuelTypes).all()
            return [{"id": f.id, "type": f.type} for f in data]
        
    def asset_type_list(self) -> list[dict]:
        with get_db_session() as session:
            data = session.query(AssetTypes).all()
            return [{"id": a.id, "type": a.type} for a in data]
        
    def location_list(self) -> list[dict]:
        with get_db_session() as session:
            data = session.query(Locations).all()
            return [{"id": l.id, "name": l.name} for l in data]
        
    def tank_list(self) -> list[dict]:
        with get_db_session() as session:
            data = session.query(Tanks).all()
            return [{"id": t.id, "name": t.name} for t in data]
        
    def assets_list(self) -> list[dict]:
        with get_db_session() as session:
            data = session.query(Assets).all()
            return [{"id": a.id, "code_asset": a.code_asset} for a in data]
    
    def suppliers_list(self) -> list[dict]:
        with get_db_session() as session:
            data = session.query(Suppliers).all()
            return [{"id": s.id, "name": s.code_asset} for s in data]    
        
    def populate_combobox(self, combo: QComboBox, data_list: list[dict], display_key: str, placeholder: str):
        """Helper untuk mengumpankan list of dict ke QComboBox + menyimpan ID tersembunyi."""
        combo.clear()
            
        # Opsi default/placeholder (ID = None)
        combo.addItem(f"-- {placeholder} --", None)
    
        # Iterasi data dan masukkan ke ComboBox
        for item in data_list:
            display_text = str(item.get(display_key, ""))
            item_id = str(item.get("id", ""))
    
            # Parameter 1: Teks Tampilan, Parameter 2: ID Tersembunyi (UserData)
            combo.addItem(display_text, item_id)
    
        combo.setCurrentIndex(0)  # Setel ke placeholder awal