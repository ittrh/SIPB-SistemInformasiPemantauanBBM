import uuid
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from databases.sqlite_db import Base


class FuelReceivings(Base):
    __tablename__ = "fuel_receivings"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    tank_id = Column(
        String(36), ForeignKey("tanks.id")
    )  # FIX: String(10) -> String(36) untuk UUID
    supplier_id = Column(String(36), ForeignKey("suppliers.id"))
    volume_masuk = Column(Float)
    no_pengadaan = Column(String(50))
    received_at = Column(DateTime)
    penerima = Column(String(50))
    keterangan = Column(String)

    tank = relationship("Tanks", back_populates="fuel_receiving")
    supplier = relationship(
        "Suppliers", back_populates="fuel_receiving"
    )  # FIX: Typo Supplilers -> Suppliers


class FuelDispensings(Base):
    __tablename__ = "fuel_dispensings"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    tank_id = Column(
        String(36), ForeignKey("tanks.id")
    )  # FIX: String(10) -> String(36) untuk UUID
    asset_id = Column(String(36), ForeignKey("assets.id"))
    volume_keluar = Column(Float)
    odometer_hourmeter = Column(Integer)
    dispensed_at = Column(DateTime)
    petugas_pengisi = Column(String(50))

    tank = relationship("Tanks", back_populates="fuel_dispensing")
    asset = relationship("Assets", back_populates="fuel_dispensing")


class FuelTransfers(Base):
    __tablename__ = "fuel_transfers"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    tank_source_id = Column(
        String(36), ForeignKey("tanks.id")
    )  # FIX: String(10) -> String(36)
    tank_destination_id = Column(
        String(36), ForeignKey("tanks.id")
    )  # FIX: String(10) -> String(36)
    volume_keluar = Column(Float)
    transfer_at = Column(DateTime)
    unit_transport_id = Column(String(36), ForeignKey("assets.id"))
    keterangan = Column(String)

    # FIX: Disamakan back_populates nya dengan class Tanks di master.py
    tank_source = relationship(
        "Tanks",
        foreign_keys=[tank_source_id],
        back_populates="fuel_source",
    )
    tank_destination = relationship(
        "Tanks",
        foreign_keys=[tank_destination_id],
        back_populates="fuel_destination",
    )
    asset = relationship("Assets", back_populates="fuel_transfer")