import uuid
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from databases.sqlite_db import Base


class Locations(Base):
    __tablename__ = "locations"

    id = Column(String(10), primary_key=True, index=False)
    name = Column(String(25), nullable=False)
    type = Column(String(10))  # 'MASTER','SITE','VENDOR'
    address = Column(String)

    tank = relationship("Tanks", back_populates="location")
    asset = relationship("Assets", back_populates="location")


class FuelTypes(Base):
    __tablename__ = "fuel_types"

    id = Column(String(10), primary_key=True, index=False)
    type = Column(String(25))

    tank = relationship("Tanks", back_populates="fuel_type")
    asset = relationship("Assets", back_populates="fuel_type")


class AssetTypes(Base):
    __tablename__ = "asset_types"

    id = Column(String(10), primary_key=True, index=False)
    type = Column(String(25))

    asset = relationship("Assets", back_populates="asset_type")


class Tanks(Base):
    __tablename__ = "tanks"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    location_id = Column(String(10), ForeignKey("locations.id"))
    name = Column(String)
    capacity_liters = Column(Float)
    current_stock = Column(Float)
    fuel_type_id = Column(String(10), ForeignKey("fuel_types.id"))

    location = relationship("Locations", back_populates="tank")
    fuel_type = relationship("FuelTypes", back_populates="tank")
    fuel_receiving = relationship("FuelReceivings", back_populates="tank")
    fuel_dispensing = relationship("FuelDispensings", back_populates="tank")

    # Perbaikan nama atribut disesuaikan dengan transactions.py
    fuel_source = relationship(
        "FuelTransfers",
        foreign_keys="FuelTransfers.tank_source_id",
        back_populates="tank_source",
    )
    fuel_destination = relationship(
        "FuelTransfers",
        foreign_keys="FuelTransfers.tank_destination_id",
        back_populates="tank_destination",
    )


class Assets(Base):
    __tablename__ = "assets"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    home_location_id = Column(String(10), ForeignKey("locations.id"))
    code_asset = Column(String(50))
    no_plat = Column(String(11))
    asset_type_id = Column(String(10), ForeignKey("asset_types.id"))
    fuel_type_id = Column(String(10), ForeignKey("fuel_types.id"))

    location = relationship("Locations", back_populates="asset")
    asset_type = relationship(
        "AssetTypes", back_populates="asset"
    )  # FIX: Typo nama class
    fuel_type = relationship("FuelTypes", back_populates="asset")
    fuel_dispensing = relationship("FuelDispensings", back_populates="asset")
    fuel_transfer = relationship("FuelTransfers", back_populates="asset")


class Suppliers(Base):
    __tablename__ = "suppliers"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name = Column(String)
    address = Column(String)

    fuel_receiving = relationship("FuelReceivings", back_populates="supplier")