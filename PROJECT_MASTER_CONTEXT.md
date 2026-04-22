# PROJECT MASTER CONTEXT
# Sistem Monitoring dan Pelaporan Kinerja Unit PT KAI Divre I Sumatera Utara
# Terintegrasi WhatsApp — Metode Waterfall

---

## 1. JUDUL TUGAS AKHIR

**Perancangan Sistem Monitoring dan Pelaporan Kinerja Unit PT KAI Divre I Sumatera Utara Terintegrasi WhatsApp Menggunakan Metode Waterfall**

> Status: Mulai dari **nol** — belum ada implementasi apapun.

---

## 2. LATAR BELAKANG

Dalam operasional PT Kereta Api Indonesia (Persero) Divre I Sumatera Utara, setiap unit kerja memiliki kewajiban menyampaikan laporan kinerja secara berkala. Namun proses yang berjalan masih memiliki kendala:

- Sistem pelaporan belum terintegrasi secara terpusat
- Proses validasi laporan masih dilakukan secara manual
- Monitoring kinerja unit sulit dilakukan secara real-time
- Tidak tersedia sistem notifikasi otomatis untuk keterlambatan atau revisi laporan
- Tidak adanya visualisasi data yang membantu analisis performa unit
- Komunikasi terkait revisi laporan masih bergantung pada chat/pesan pribadi

**Solusi:** Sistem monitoring dan pelaporan kinerja unit berbasis web yang terintegrasi dengan WhatsApp Gateway.

---

## 3. GAMBARAN UMUM SISTEM

- **Jenis:** Web-based Monitoring & Reporting System
- **Data:** Berbasis data operasional real (bukan KPI)
- **Validasi:** Two-level validation system (internal + eksternal)
- **Integrasi:** WhatsApp Gateway (Baileys)
- **Realtime:** Socket.io
- **Helpdesk:** Tersedia sistem helpdesk & IT Support

### Fungsi Utama
1. Input laporan harian per unit
2. Validasi internal oleh user unit
3. Review laporan oleh Admin Global (ACC / REVISI)
4. Monitoring melalui dashboard dengan grafik batang
5. Notifikasi otomatis (WA + realtime)
6. Helpdesk untuk kendala sistem

---

## 4. METODE PENGEMBANGAN

**SDLC Modified Waterfall**

| Tahapan | Status |
|---------|--------|
| Requirement | Selesai |
| Analysis | Selesai |
| Design | Selesai |
| Implementation | Belum dimulai |
| Testing | Belum dimulai |
| Maintenance | Belum dimulai |

---

## 5. STACK TEKNOLOGI

| Layer | Teknologi |
|-------|-----------|
| Frontend | React |
| Backend | Node.js + Express |
| ORM | Prisma |
| Database | MySQL |
| Realtime | Socket.io |
| WhatsApp | Baileys |
| Auth | JWT |

---

## 6. ROLE & HAK AKSES

### USER UNIT
- Input laporan harian
- Validasi internal laporan sendiri
- Submit laporan (hanya jika status `READY_TO_SUBMIT`)
- Lihat status laporan unit sendiri
- Input target (RKAP/Program) unit sendiri
- Tambah komoditi barang (untuk unit Angkutan Barang)
- Ajukan helpdesk (TOKEN / ISSUE / REVISION)
- Export laporan (PDF & Excel)

### ADMIN GLOBAL
- Monitor semua unit
- Review laporan: ACC atau REVISI
- Set status laporan menjadi REVISI (termasuk dari request helpdesk)
- Kelola akun user (buat, edit, nonaktifkan)
- Kelola unit
- Kelola notifikasi
- Handle helpdesk jenis **REVISION**

### IT SUPPORT
- Generate token reset password
- Handle technical issue
- Monitoring sistem
- Handle helpdesk jenis **TOKEN** dan **ISSUE**

> **Catatan:** Jika IT Support ter-lock, penanganannya dilakukan langsung via akses database (di luar scope sistem).

---

## 7. SISTEM KEAMANAN LOGIN

- **3x gagal login → akun ter-LOCK otomatis**
- User yang ter-lock tidak bisa login sampai password di-reset
- Harus mengajukan helpdesk jenis TOKEN ke IT Support

### Alur Reset Password via Token

```
3x gagal login
    ↓
Akun ter-LOCK
    ↓
User ajukan helpdesk jenis TOKEN ke IT Support
    ↓
IT Support generate token (one-time, ada expiry)
    ↓
Token dikirim via WhatsApp ke user
    ↓
User buka halaman reset password → input token + password baru
    ↓
Password lama di database LANGSUNG diganti (atomic update, tanpa tabrakan)
    ↓
Token di-invalidate (tidak bisa dipakai lagi)
    ↓
Akun ter-UNLOCK otomatis
    ↓
User bisa login dengan password baru
```

**Catatan teknis:** Update password bersifat atomic — password lama langsung terganti ke data baru, tidak ada race condition atau konflik.

---

## 8. ALUR LAPORAN (CORE FLOW)

```
User input laporan
    ↓
[Box Detail Opsional — boleh dikosongkan]
    ↓
Validasi Internal (dilakukan user unit sendiri)
    ↓
Status: DRAFT → NEED_REVISION_INTERNAL → READY_TO_SUBMIT
    ↓
Submit (HANYA bisa jika status READY_TO_SUBMIT)
    ↓
Status: WAITING (menunggu Admin Global)
    ↓
Admin Review
    ↓
ACC ──────────── tidak ada notifikasi WA
    atau
REVISI ────────── notifikasi WA + realtime (Socket.io)
```

**Constraint:** 1 unit = 1 laporan per hari (unique constraint di database)

---

## 9. SISTEM VALIDASI (TWO-LEVEL)

### Level 1 — Validasi Internal (oleh User Unit)

| Status | Keterangan |
|--------|-----------|
| `DRAFT` | Laporan baru dibuat, belum divalidasi |
| `NEED_REVISION_INTERNAL` | Perlu diperbaiki user sendiri sebelum submit |
| `READY_TO_SUBMIT` | Sudah valid, siap dikirim ke Admin |

### Level 2 — Validasi Eksternal (oleh Admin Global)

| Status | Keterangan |
|--------|-----------|
| `WAITING` | Sudah di-submit, menunggu review Admin |
| `ACC` | Diterima Admin |
| `REVISI` | Perlu diperbaiki (dari Admin langsung atau dari request helpdesk) |

**Rule:** Tidak bisa submit jika status bukan `READY_TO_SUBMIT`

---

## 10. ALUR EDIT LAPORAN SETELAH SUBMIT

User **tidak bisa langsung edit** laporan yang sudah di-submit. Harus melalui helpdesk:

```
Laporan status WAITING atau ACC
    ↓
User ajukan helpdesk jenis REVISION
    ↓
Notifikasi WA otomatis dikirim ke Admin Global
    ↓
Admin set status laporan → REVISI
    ↓
User bisa edit laporan
    ↓
User re-submit → status kembali ke WAITING
    ↓
Admin review ulang
```

---

## 11. JENIS UNIT & STRUKTUR LAPORAN

### Struktur Umum (berlaku di semua unit)

1. **Header Laporan**
   - Nama Unit
   - Jenis Laporan (Harian / Mingguan / Bulanan)
   - Tanggal / Periode

2. **Data Harian** (wajib)
   - Aktivitas / operasional harian
   - Volume / output
   - Pendapatan / nilai
   
3. **Data Kumulatif**
   - Akumulasi dari 1 Januari s/d hari berjalan
   - Total volume kumulatif
   - Total pendapatan kumulatif

4. **Target vs Realisasi**
   - Target (diinput oleh unit sendiri)
   - Realisasi
   - Persentase pencapaian

5. **Box Detail** *(opsional — boleh dikosongkan)*
   - Catatan khusus, breakdown tambahan, keterangan

6. **Rekapitulasi**
   - Total performa hari ini
   - Status (naik / turun / stabil)

---

### Unit 1 — KNA (Non Angkutan)
**Fokus:** Kontrak, luas, nilai

| Bagian | Field |
|--------|-------|
| Harian | Jumlah kontrak ROW, Luas, Nilai, Non-ROW |
| Kumulatif | Total kontrak, Luas total, Nilai total |
| Target vs Realisasi | **RKAD** (hanya di KNA), Realisasi, % |

> **RKAD hanya ada di unit KNA, tidak di unit lain.**

---

### Unit 2 — Angkutan Penumpang
**Fokus:** Jumlah penumpang & pendapatan

| Bagian | Field |
|--------|-------|
| Harian | List KA + jumlah penumpang, Total penumpang, Total pendapatan |
| Kumulatif | Total penumpang tahun berjalan, Total pendapatan |
| Target | Target penumpang, Realisasi, % |

---

### Unit 3 — Angkutan Barang
**Fokus:** Volume & pendapatan + detail komoditi

| Bagian | Field |
|--------|-------|
| Harian | Jumlah KA per komoditi, Volume harian, Pendapatan harian |
| Kumulatif | Volume total, Pendapatan total |
| Target | Program, Realisasi, % |
| Rincian | Per komoditi (BBM, CPO, dll) |

> **Komoditi bersifat dinamis** — user bisa tambah komoditi sendiri (tidak fixed).

---

### Unit 4 — Keuangan
**Fokus:** Cashflow & profit

| Bagian | Field |
|--------|-------|
| Harian | Pendapatan, Pengeluaran |
| Rekap | Laba/Rugi harian |
| Kumulatif | Total pendapatan, Total laba/rugi |

---

## 12. TARGET (RKAP / PROGRAM)

- Diinput oleh **user unit sendiri** (bukan Admin Global)
- Target per tahun / per periode
- Digunakan untuk perbandingan dengan realisasi harian & kumulatif
- **RKAD khusus unit KNA** — unit lain menggunakan label "Target" atau "Program"

---

## 13. VISUALISASI DASHBOARD

**Format grafik:** Diagram Batang saja untuk semua unit (tidak ada pie chart)

### Grafik per Unit

| Unit | Grafik 1 — Mingguan | Grafik 2 — Bulanan |
|------|--------------------|--------------------|
| KNA | Nilai kontrak per minggu | Nilai kontrak per bulan |
| Penumpang | Jumlah penumpang per minggu | Pendapatan per bulan |
| Barang | Volume (Ton) per minggu | Pendapatan per bulan |
| Keuangan | Pendapatan vs Pengeluaran per minggu | Laba/Rugi per bulan |

### Skala Waktu
- **Grafik bulanan:** X-axis = Minggu 1, 2, 3, 4
- **Grafik tahunan:** X-axis = Jan – Des

---

## 14. SISTEM NOTIFIKASI

| Trigger | Channel | Penerima |
|---------|---------|---------|
| Laporan di-REVISI | WA (Baileys) + Realtime (Socket.io) | User unit terkait |
| Reminder deadline | WA jam 16:30 | Semua unit (termasuk yang sudah submit) |
| Helpdesk REVISION masuk | WA | Admin Global |
| Token reset password | WA | User yang ter-lock |

> Tidak ada notifikasi WA saat laporan di-ACC.

---

## 15. HELPDESK SYSTEM

### Jenis Tiket

| Jenis | Dirouting ke | Alur |
|-------|-------------|------|
| `TOKEN` | IT Support | User lock → ajukan TOKEN → IT generate token → kirim WA → user reset password |
| `ISSUE` | IT Support | User laporkan masalah teknis → IT handle |
| `REVISION` | Admin Global | User minta edit laporan → notif WA Admin → Admin set status REVISI |

> Tidak ada fitur history helpdesk yang bisa dilihat oleh user.

---

## 16. EXPORT LAPORAN

- Format: **PDF** dan **Excel**
- Berlaku untuk laporan per unit
- Dapat dilakukan oleh User Unit maupun Admin Global

---

## 17. DESAIN DATABASE

### Tabel Utama

| Tabel | Keterangan |
|-------|-----------|
| `User` | Data user semua role, field: loginAttempts, isLocked |
| `Unit` | Data unit kerja (KNA, Penumpang, Barang, Keuangan) |
| `Report` | Header laporan, unique constraint (unitId + tanggal) |
| `ReportKNA` | Detail laporan unit KNA (ROW, Non-ROW, RKAD) |
| `ReportPassenger` | Detail laporan penumpang (per KA) |
| `ReportCargo` | Detail laporan barang |
| `CargoCommodity` | Komoditi barang (dinamis, user bisa tambah) |
| `ReportFinance` | Detail laporan keuangan |
| `SupportRequest` | Helpdesk (TOKEN / ISSUE / REVISION) |
| `ResetToken` | Token reset password (one-time, ada expiry) |
| `AuditLog` | Log aktivitas sistem |
| `Target` | Target per unit per periode (diinput user unit) |

### Constraint Penting
- `Report`: unique per `(unitId, tanggal)` — 1 unit = 1 laporan per hari
- `ResetToken`: one-time use, di-invalidate setelah dipakai
- `User`: `loginAttempts` di-reset setelah login berhasil atau password di-reset

---

## 18. MODULAR SYSTEM (BACKEND)

| Modul | Fungsi |
|-------|--------|
| `Auth` | Login, JWT, lock akun, unlock |
| `User` | CRUD user oleh Admin |
| `Unit` | Kelola unit |
| `Report` | CRUD laporan per jenis unit |
| `Validation` | Internal & external validation flow |
| `Target` | Input & kelola target per unit |
| `Dashboard` | Agregasi data untuk grafik |
| `Notification` | WA (Baileys) + Socket.io |
| `Helpdesk` | SupportRequest routing |
| `Token` | Generate, validasi, invalidate reset token |
| `Export` | Generate PDF & Excel |
| `AuditLog` | Logging aktivitas |

---

## 19. URUTAN IMPLEMENTASI

| No | Modul | Keterangan |
|----|-------|-----------|
| 1 | Setup project + DB schema | Prisma schema, MySQL, struktur folder |
| 2 | Auth system | Login, JWT, lock 3x gagal, unlock |
| 3 | Token system | Generate, kirim WA, reset password atomic |
| 4 | User & Unit management | Admin buat/kelola akun & unit |
| 5 | Target input | User unit input target per periode |
| 6 | Report CRUD | Input laporan per unit + box detail opsional + komoditi custom |
| 7 | Validation system | Internal (DRAFT → READY_TO_SUBMIT) + External (WAITING → ACC/REVISI) |
| 8 | Admin review | ACC & REVISI langsung dari Admin |
| 9 | Helpdesk system | TOKEN → IT, ISSUE → IT, REVISION → Admin |
| 10 | Notifikasi | Socket.io realtime + WhatsApp Baileys |
| 11 | Dashboard & grafik | Diagram batang mingguan & bulanan per unit |
| 12 | Export | PDF & Excel per laporan |

---

## 20. KEPUTUSAN TEKNIS FINAL

| Keputusan | Detail |
|-----------|--------|
| Tidak menggunakan KPI | Data berbasis operasional real |
| Modular system | Setiap fitur terpisah per modul |
| Two-level validation | Internal (user) + Eksternal (admin) |
| WhatsApp integration | Menggunakan Baileys |
| Role separation | 3 role: User Unit, Admin Global, IT Support |
| Prisma ORM | Untuk akses database MySQL |
| JWT Auth | Token-based authentication |
| Diagram batang saja | Tidak ada pie chart di visualisasi |
| RKAD hanya di KNA | Unit lain menggunakan "Target" / "Program" |
| Komoditi dinamis | User bisa tambah komoditi sendiri |
| Lock akun 3x gagal | Wajib reset via token dari IT Support |
| Password reset atomic | Tidak ada race condition / tabrakan data |
| Edit laporan via helpdesk | Tidak bisa langsung edit setelah submit |
| Reminder 16:30 ke semua | Broadcast ke semua unit tanpa terkecuali |
| Export PDF & Excel | Ada fitur export laporan |

---

*Dokumen ini merupakan master context final hasil diskusi — dapat digunakan sebagai referensi pengembangan di setiap sesi baru.*
