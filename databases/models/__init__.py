# Import semua model master
from databases.models.masters import (
    Locations,
    FuelTypes,
    AssetTypes,
    Tanks,
    Assets,
    Suppliers
)

# Import semua model transaksi
from databases.models.transactions import (
    FuelReceivings,
    FuelDispensings,
    FuelTransfers
)

__all__ = [
    "Locations",
    "FuelTypes",
    "AssetTypes",
    "Tanks",
    "Assets",
    "Suppliers",
    "FuelReceivings",
    "FuelDispensings",
    "FuelTransfers"
]