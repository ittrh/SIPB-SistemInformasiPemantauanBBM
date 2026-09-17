**Bisa banget.** Model data `FuelDispensings` kamu sudah punya semua field yang dibutuhkan untuk query tersebut:

* **Asset**: `asset_id` (atau via `relationship("Assets")` untuk mengambil nama/nomor plat asset)
* **Konsumsi BBM**: `volume_keluar`
* **Filter Tanggal**: `dispensed_at`

---

### Contoh Query SQLAlchemy

Kamu bisa menggunakan agregasi `func.sum()` dan pengelompokan `group_by()` untuk menghitung total konsumsi per asset, lalu diurutkan secara *descending* (`desc()`).

```python
from datetime import datetime
from sqlalchemy import func
from src.models import FuelDispensings, Assets  # Sesuaikan dengan lokasi modelmu

def get_top_fuel_consuming_assets(session, start_date: datetime, end_date: datetime, limit: int = 5):
    results = (
        session.query(
            Assets.nama_asset, # Asumsi di model Assets ada kolom nama_asset
            func.sum(FuelDispensings.volume_keluar).label("total_volume")
        )
        .join(FuelDispensings, Assets.id == FuelDispensings.asset_id)
        # Filter berdasarkan range tanggal
        .filter(FuelDispensings.dispensed_at.between(start_date, end_date))
        # Group berdasarkan asset
        .group_by(Assets.id, Assets.nama_asset)
        # Urutkan dari volume terbanyak ke sedikit
        .order_by(func.sum(FuelDispensings.volume_keluar).desc())
        # Ambil Top N (misal: Top 5 atau Top 10)
        .limit(limit)
        .all()
    )
    
    return results

```

---

### Cara Memanggilnya di PySide6

Misalnya kamu memanggil fungsi di atas dari controller UI untuk menampilkan hasilnya ke dalam tabel atau grafik:

```python
# Contoh range tanggal (misal dari input QDateEdit di UI)
tgl_mulai = datetime(2026, 9, 1, 0, 0, 0)
tgl_selesai = datetime(2026, 9, 30, 23, 59, 59)

top_assets = get_top_fuel_consuming_assets(db_session, tgl_mulai, tgl_selesai, limit=5)

for ranking, (nama_asset, total_bbm) in enumerate(top_assets, start=1):
    print(f"Peringkat {ranking}: {nama_asset} - Total BBM: {total_bbm} Liter")

```