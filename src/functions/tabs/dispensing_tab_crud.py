from databases.sqlite_db import get_db_session
from databases.models.transactions import FuelDispensings
from databases.models.masters import Assets, Tanks
from datetime import datetime, date

class DispensingTabCrud:
    def __init__(self):
        self.dispensing_data_view: list[dict] = []
        
    def load_data_dispensing(self) -> list[dict]:
        with get_db_session() as session:
            query = (
                session.query(FuelDispensings, Assets, Tanks)
                .join(Assets, FuelDispensings.asset_id == Assets.id)
                .join(Tanks, FuelDispensings.tank_id == Tanks.id)
                .all()
            )
            
            self.dispensing_data_view = []
            for dispensing, asset, tank in query:
                item = {
                    "id": getattr(dispensing, 'id', None),
                    "volume_keluar": dispensing.volume_keluar,
                    "tangki_pengisi": tank.name,
                    "odometer_hourmeter": dispensing.odometer_hourmeter,
                    "dispensing_at": getattr(dispensing, 'dispensing_at', dispensing.dispensing_at),
                    "petugas_pengisi": dispensing.petugas_pengisi,
                    "code_asset": asset.code_asset,
                    "no_plat": asset.no_plat,
                }
                self.dispensing_data_view.append(item)
        return self.dispensing_data_view
    
    def create_dispensing_transaction(self, param_dict: dict) -> None:
        time_now = datetime.now()
        with get_db_session() as session:
            fuel_dispensing = FuelDispensings(
                tank_id=param_dict['tank_id'],
                asset_id=param_dict['asset_id'],
                volume_keluar=param_dict['volume_keluar'],
                odometer_hourmeter=param_dict['odometer_hourmeter'],
                dispensing_at=time_now,
                petugas_pengisi=param_dict['petugas_pengisi']
            )
            session.add(fuel_dispensing)
            session.commit()
        self.load_data_dispensing()
        
    def search_data_dispensing(self, keyword: str) -> list[dict]:
        if not keyword:
            return self.dispensing_data_view
        
        keyword_lower = keyword.lower()
        return [
            item for item in self.dispensing_data_view
            if keyword_lower in str(item["petugas_pengisi"]).lower() or
            keyword_lower in str(item['code_asset']).lower() or
            keyword_lower in str(item['no_plat']).lower() or
            keyword_lower in str(item['tangki_pengisi']).lower()
        ]
        
    def filter_by_date_dispensing(self, start_date, end_date, search: str) -> list[dict]:
        if hasattr(start_date, "toPython"):
            start_date = start_date.toPython()
        if hasattr(end_date, "toPython"):
            end_date = end_date.toPython()
            
        # Konversi datetime ke date jika bertipe datetime
        if isinstance(start_date, datetime):
            start_date = start_date.date()
        if isinstance(end_date, datetime):
            end_date = end_date.date()

        # Parse jika berupa string 'YYYY-MM-DD'
        if isinstance(start_date, str) and start_date.strip():
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if isinstance(end_date, str) and end_date.strip():
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            
        filtered_result = []
        search_lower = search.strip().lower() if search else ""
        
        for item in self.dispensing_data_view:
            dispensing_at = item.get("dispensing_at")
            item_date = None
            if isinstance(dispensing_at, datetime):
                item_date = dispensing_at.date()
            elif isinstance(dispensing_at, date):
                item_date = dispensing_at
            elif isinstance(dispensing_at, str):
                try:
                    # Mencoba parse string iso/datetime ke date
                    item_date = datetime.fromisoformat(dispensing_at).date()
                except ValueError:
                    item_date = None
                    
            date_matches = True
            if item_date:
                if start_date and item_date < start_date:
                    date_matches = False
                if end_date and item_date > end_date:
                    date_matches = False
            elif start_date or end_date:
                date_matches = False
                
            if not date_matches:
                continue
            text_matches = True
            if search_lower:
                petugas = str(item.get("petugas_pengisi", "")).lower()
                code_asset = str(item.get("code_asset", "")).lower()
                no_plat = str(item.get("no_plat", "")).lower()
                tangki_pengisi = str(item.get("tangki_pengisi")).lower()
                
                if (search_lower not in petugas and 
                    search_lower not in code_asset and 
                    search_lower not in no_plat and
                    search_lower not in tangki_pengisi):
                    text_matches = False
            
            if date_matches and text_matches:
                filtered_result.append(item)
        
        return filtered_result