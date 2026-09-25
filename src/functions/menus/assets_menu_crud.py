from databases.sqlite_db import get_db_session
from databases.models.masters import Assets, Locations, AssetTypes, FuelTypes

class AssetsMenuCrud:
    def __init__(self):
        self.assets_data_view: list[dict] = []
        
    def load_data_assets(self) -> list[dict]:
        with get_db_session() as session:
            query = (
                session.query(Assets, Locations, AssetTypes, FuelTypes)
                .join(Locations, Assets.home_location_id == Locations.id)
                .join(AssetTypes, Assets.asset_type_id == AssetTypes.id)
                .join(FuelTypes, Assets.fuel_type_id == FuelTypes.id)
                .all()
            )
        self.assets_data_view = []
        for assets, locations, asset_type, fuel_type in query:
            item = {
                "id": getattr(assets, 'id', None),
                "location_asset": locations.name,
                "code_asset": assets.code_asset,
                "no_plat": assets.no_plat,
                "type_asset": asset_type.type,
                "fuel_type": fuel_type.type,
            }
            self.assets_data_view.append(item)
        return self.assets_data_view
    
    def create_asset(self, param_dict: dict) -> None:
        with get_db_session() as session:
            asset = Assets(
                home_location_id=param_dict['home_location_id'],
                code_asset=param_dict['code_asset'],
                no_plat=param_dict['no_plat'],
                asset_type_id=param_dict['asset_type_id'],
                fuel_type_id=param_dict['fuel_type_id']
            )
            session.add(asset)
            session.commit()
        self.load_data_assets()
        
    def search_data_asset(self, keyword: str) -> list[dict]:
        if not keyword:
            return self.assets_data_view
        
        keyword_lower = keyword.lower()
        return [
            item for item in self.assets_data_view
            if keyword_lower in str(item["code_asset"]).lower() or
            keyword_lower in str(item["no_plat"]).lower() or
            keyword_lower in str(item["location_asset"]).lower()
        ]