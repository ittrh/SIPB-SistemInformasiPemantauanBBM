Berikut adalah rancangan skema basis data relasional untuk sistem pemantauan BBM di perusahaan Anda. Rancangan ini mencakup pengelolaan lokasi/site, tangki penyimpanan, transaksi masuk (penerimaan), transaksi keluar (pengisian unit), serta transfer antar lokasi.

### Skema Basis Data

#### 1. `locations` (Lokasi / Site / Head Office)

Menyimpan data unit kerja, lokasi site, maupun Kantor HO.

* `location_id` (PK, INT, Auto Increment)
* `name` (VARCHAR) — Contoh: "Head Office", "Site A", "Site B"
* `type` (ENUM) — `'HEAD_OFFICE'`, `'SITE'`, `'VENDOR'`
* `address` (TEXT)
* `created_at` (DATETIME)

#### 2. `tanks` (Tangki Penyimpanan / Storage BBM)

Setiap lokasi bisa memiliki satu atau lebih tangki penyimpanan BBM.

* `tank_id` (PK, INT, Auto Increment)
* `location_id` (FK -> `locations.location_id`)
* `name` (VARCHAR) — Contoh: "Tangki Utama HO 10KL", "Tangki Portable Site A"
* `capacity_liters` (DECIMAL(10,2)) — Kapasitas maksimal tangki
* `current_stock` (DECIMAL(10,2)) — Stok saat ini (diperbarui otomatis via trigger/transaksi)
* `fuel_type` (VARCHAR) — Contoh: "Solar B35", "Pertamax"

#### 3. `assets` (Unit Kerja / Alat Berat / Kendaraan)

Menyimpan daftar unit/mesin yang mengisi BBM.

* `asset_id` (PK, INT, Auto Increment)
* `home_location_id` (FK -> `locations.location_id`) — Base location unit
* `asset_code` (VARCHAR) — Contoh: "DT-01", "EXCA-05", "GENSET-HO"
* `type` (VARCHAR) — Contoh: "Dump Truck", "Excavator", "Genset"
* `license_plate` (VARCHAR, Nullable)

#### 4. `fuel_receivings` (Penerimaan BBM / Inflow)

Mencatat stok BBM yang masuk ke tangki (misal: pembelian dari supplier/vendor).

* `receiving_id` (PK, INT, Auto Increment)
* `tank_id` (FK -> `tanks.tank_id`)
* `supplier_name` (VARCHAR)
* `volume_liters` (DECIMAL(10,2)) — Jumlah BBM masuk
* `delivery_note_number` (VARCHAR) — Nomor Surat Jalan/PO
* `received_at` (DATETIME)
* `received_by` (VARCHAR)

#### 5. `fuel_dispensings` (Pengeluaran BBM ke Unit / Outflow)

Mencatat pengisian BBM langsung ke kendaraan atau alat kerja (baik di HO maupun Site).

* `dispensing_id` (PK, INT, Auto Increment)
* `tank_id` (FK -> `tanks.tank_id`) — Tangki sumber BBM
* `asset_id` (FK -> `assets.asset_id`) — Unit yang diisi
* `volume_liters` (DECIMAL(10,2)) — Jumlah BBM yang diisikan
* `odometer_hourmeter` (DECIMAL(10,2)) — Odometer/Hour Meter saat pengisian (untuk analisis efisiensi)
* `dispensed_at` (DATETIME)
* `operator_name` (VARCHAR) — Petugas pengisian

#### 6. `fuel_transfers` (Transfer BBM antar Tangki/Site)

Mencatat pendistribusian BBM dari Head Office ke Site (atau antar-tangki).

* `transfer_id` (PK, INT, Auto Increment)
* `source_tank_id` (FK -> `tanks.tank_id`) — Tangki asal (misal: Tangki HO)
* `destination_tank_id` (FK -> `tanks.tank_id`) — Tangki tujuan (misal: Tangki Site A)
* `volume_liters` (DECIMAL(10,2))
* `status` (ENUM) — `'PENDING'`, `'IN_TRANSIT'`, `'COMPLETED'`, `'CANCELLED'`
* `sent_at` (DATETIME)
* `received_at` (DATETIME, Nullable)
* `transport_vehicle_code` (VARCHAR) — Unit yang membawa BBM (misal: Fuel Truck HO)

---

### Alur Kerja & Pemantauan Stok

```
[Supplier] ---> (Penerimaan) ---> [Tangki HO] 
                                    |
            +-----------------------+-----------------------+
            |                                               |
  (Pengisian Langsung)                             (Transfer BBM)
            v                                               v
[Unit / Kendaraan HO]                             [Tangki Site]
                                                            |
                                                   (Pengisian Langsung)
                                                            v
                                                   [Unit / Alat Site]

```

* **Stok Real-time (`current_stock`):** Setiap ada baris baru di `fuel_receivings` (tambah stok), `fuel_dispensings` (kurang stok), atau `fuel_transfers` (kurang di asal, tambah di tujuan saat *COMPLETED*), lakukan pembaruan pada `current_stock` di tabel `tanks`.
* **Audit Trail & Konsumsi Fuel:** Kolom `odometer_hourmeter` pada `fuel_dispensings` sangat membantu untuk menghitung rasio konsumsi BBM (Liter/KM atau Liter/Jam Kerja).