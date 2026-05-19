# PROMPT DESIGN — Sistem Monitoring & Pelaporan PT KAI Divre I Sumut
# Copy prompt di bawah ini ke Claude Design / v0 / Figma AI

---

## GLOBAL STYLE REFERENCE (Masukkan di semua prompt)

```
Design a professional web dashboard UI for PT KAI (Kereta Api Indonesia) Divre I Sumatera Utara internal reporting system.

Global design style:
- Dark navy blue sidebar (#0D3472) with white icons and text
- White/light gray (#F5F7FA) main content background
- White cards with subtle box shadow (0 2px 8px rgba(0,0,0,0.08))
- Primary blue button: #1A5FCC, rounded corners 8px
- Typography: clean sans-serif (Inter or similar), dark text #1A1A2E
- Status badges: pill-shaped — green for ACC/verified, yellow/amber for WAITING, red for REVISI
- PT KAI logo placeholder on top-left sidebar
- User avatar initials badge on top-right header
- Footer: "© 2024 PT Kereta Api Indonesia (Persero) Divisi Regional I Sumatera Utara"
- Responsive: desktop first (1440px wide)
- Language: Bahasa Indonesia
```

---

## HALAMAN 1 — LOGIN PAGE

```
Design a login page for PT KAI Divre I Sumut internal web system.

Style: clean, professional, corporate
- Left side (40%): dark navy blue panel (#0D3472) with PT KAI logo centered, tagline "Sistem Monitoring & Pelaporan Kinerja Unit", and decorative geometric pattern
- Right side (60%): white background with login form centered

Login form elements:
- Title: "Masuk ke Sistem"
- Subtitle: "PT KAI Divre I Sumatera Utara"
- Email input field with envelope icon
- Password input field with eye toggle icon
- "Lupa password? Hubungi IT Support" link in small gray text below password field
- Primary blue login button full width: "Masuk"
- Error state: show red alert box "Email atau password salah. Sisa percobaan: 2" with warning icon
- Locked state: show red alert box "Akun Anda terkunci setelah 3x percobaan gagal. Silakan ajukan helpdesk ke IT Support." with lock icon and "Ajukan Helpdesk" button

Footer bottom: "© 2024 PT KAI Divre I Sumatera Utara"
```

---

## HALAMAN 2 — RESET PASSWORD (via Token)

```
Design a reset password page for PT KAI Divre I Sumut system.

Style: same as login page, centered card on white/light gray background

Card elements (max-width 480px, centered):
- Back arrow link "← Kembali ke Login"
- Icon: lock with checkmark (blue)
- Title: "Reset Password"
- Subtitle: "Masukkan token yang telah dikirim ke WhatsApp Anda oleh IT Support"
- Token input field: large, monospace font, placeholder "Masukkan token..."
- New password input with eye toggle: "Password Baru"
- Confirm password input with eye toggle: "Konfirmasi Password Baru"
- Password strength indicator bar below new password field
- Primary blue button full width: "Reset Password"
- Error state: red text "Token tidak valid atau sudah kedaluwarsa"
- Success state: green checkmark animation, text "Password berhasil diubah! Mengarahkan ke halaman login..."

Note: Token is one-time use, password update is atomic (no race condition)
```

---

## HALAMAN 3 — DASHBOARD ADMIN GLOBAL

```
Design a dashboard page for Admin Global role in PT KAI Divre I Sumut monitoring system.

Layout: dark navy sidebar (left 220px) + main content (right)

Sidebar navigation items with icons:
- Dashboard (active state: blue highlight)
- Laporan
- History Laporan
- Manajemen Unit
- Manajemen User
- Helpdesk
- Manajemen Notifikasi
- Settings
- Keluar

Top header: page title "Dashboard", user badge top-right showing "AG" initials, name "Admin Global", subtitle "Divre I Sumatera Utara"

Main content:
1. Summary cards row (4 cards):
   - Angkutan Penumpang: "1.250.400" subtitle "Total kumulatif hari ini", green +5.2% badge, bus icon
   - Angkutan Barang: "850.000 Ton" subtitle "Total tonase terangkut", red -2.1% badge, truck icon
   - KNA: "92%" subtitle "Pencapaian target tahunan", green +0.5% badge, checkmark icon
   - Keuangan: "Rp 45,2 Miliar" subtitle "Total pendapatan operasional", green +12% badge, wallet icon

2. Filter bar (white card):
   - Dropdown "Pilih Unit": "Semua Unit Divre I"
   - Dropdown "Bulan": "Mei"
   - Dropdown "Tahun": "2024"
   - Blue button "Terapkan Filter" with filter icon
   - Right side: "Export PDF" button (outline), "Lihat Laporan" button (outline)

3. Charts row (2 charts side by side):
   - Left chart (60%): "Trend Volume Mingguan (Mei 2024)" - bar chart, x-axis: Minggu 1-4, blue bars, stats below: AVERAGE 312.600, PEAK 380.000, GROWTH +4.2% green
   - Right chart (40%): "Trend Tahunan Pencapaian RKAD 2024" - line chart, x-axis: JAN-NOV, blue line with dots, legend: "Realisasi" (blue dot) "Target RKAD" (gray dot), note "Data diperbarui otomatis setiap 24 jam"

4. Table "Status Pelaporan Unit Terakhir" with "Lihat Semua" link:
   Columns: ID UNIT | NAMA UNIT PELAPOR | WAKTU LAPOR | JENIS LAPORAN | STATUS | AKSI
   Row 1: DIVRE1-001 | Unit Angkutan Penumpang | Hari ini, 09:45 | Harian Operasional | green badge "TERVERIFIKASI" | external link icon
   Row 2: DIVRE1-004 | Unit Sarana | Hari ini, 08:20 | Maintenance Lokomotif | amber badge "MENUNGGU REVIEW" | external link icon
   Row 3: DIVRE1-002 | Unit Angkutan Barang | Kemarin, 17:10 | Volume Logistik | red badge "PERBAIKAN DATA" | external link icon
```

---

## HALAMAN 4 — DASHBOARD USER UNIT

```
Design a dashboard page for User Unit role in PT KAI Divre I Sumut system.

Same sidebar style as Admin but navigation items:
- Dashboard (active)
- Input Laporan
- History Laporan
- Target Saya
- Helpdesk
- Keluar

Top header: user badge "UU", name "Unit Angkutan Barang", subtitle "Divre I Sumatera Utara"

Main content:
1. Status cards row (3 cards):
   - "Laporan Hari Ini" with status badge: large amber badge "MENUNGGU REVIEW", date "Kamis, 24 April 2025"
   - "Laporan Bulan Ini" stats: ACC: 18, REVISI: 3, Belum Submit: 1
   - "Pencapaian Target" progress ring chart 78%, label "dari target tahunan"

2. Alert banner (if laporan hari ini belum submit): amber background, warning icon, text "Laporan hari ini belum disubmit. Batas waktu: 17.00 WIB", blue button "Input Sekarang"

3. Chart: "Trend Volume Mingguan" - bar chart blue, Minggu 1-4

4. Table "History Laporan Terbaru":
   Columns: TANGGAL | JENIS | STATUS | CATATAN REVISI | AKSI
   Show last 5 entries with colored status badges
   Status: ACC (green), REVISI (red), WAITING (amber), DRAFT (gray)
```

---

## HALAMAN 5 — INPUT LAPORAN (Unit Angkutan Barang)

```
Design an input form page for daily report submission — Unit Angkutan Barang (Cargo).

Layout: same sidebar + header

Page title: "Input Laporan Harian" with breadcrumb "Dashboard > Input Laporan > Angkutan Barang"

Status progress bar at top: 3 steps — "DRAFT" (active blue) → "READY TO SUBMIT" → "WAITING"

Form sections as white cards:

CARD 1 — Header Laporan:
- Nama Unit (read-only): "Unit Angkutan Barang"
- Jenis Laporan (read-only): "Harian"
- Tanggal (auto-filled, read-only): "24 April 2025"

CARD 2 — Data Harian (required):
- Table with columns: Komoditi | Jumlah KA | Volume (Ton) | Pendapatan (Rp)
- Rows for each commodity: BBM, CPO, Pupuk, dll
- Last row: "+ Tambah Komoditi" button (blue outline)
- Row total at bottom: bold "TOTAL HARIAN"

CARD 3 — Data Kumulatif (required):
- Total Volume Kumulatif (Ton): number input
- Total Pendapatan Kumulatif (Rp): number input
- Info text: "Akumulasi 1 Januari s/d hari ini"

CARD 4 — Target vs Realisasi (required):
- Target Program (Ton): number input
- Realisasi (Ton): number input (auto-sum from daily)
- Persentase: auto-calculated, shown as "78.5%" with progress bar

CARD 5 — Box Detail (optional):
- Textarea placeholder: "Catatan tambahan, keterangan khusus, atau informasi relevan lainnya... (opsional)"
- Gray label: "Kolom ini bersifat opsional, boleh dikosongkan"

Action buttons:
- Gray outline button: "Simpan Draft"
- Blue button: "Validasi Internal" (active when all required fields filled)
- After validation: green button "Submit Laporan" appears
```

---

## HALAMAN 6 — INPUT LAPORAN (Unit KNA)

```
Design an input form page for daily report — Unit KNA (Non Angkutan).

Same layout as cargo form. 

CARD 2 — Data Harian KNA (required):
Sub-section A: ROW (Right of Way)
- Jumlah Kontrak ROW: number input
- Luas (m²): number input
- Nilai Kontrak (Rp): number input

Sub-section B: Non-ROW
- Jumlah Kontrak Non-ROW: number input
- Luas (m²): number input
- Nilai Kontrak (Rp): number input

CARD 3 — Data Kumulatif:
- Total Kontrak (ROW + Non-ROW): auto-calculated
- Luas Total (m²): number input
- Nilai Total (Rp): number input

CARD 4 — Target vs Realisasi (RKAD — hanya ada di KNA):
- RKAD Target (Rp): number input
- Realisasi (Rp): number input
- Pencapaian (%): auto-calculated with progress bar
- Note label in blue: "RKAD: Rencana Kerja Anggaran Divisi"

CARD 5 — Box Detail (opsional): same as cargo
```

---

## HALAMAN 7 — INPUT LAPORAN (Angkutan Penumpang)

```
Design an input form page for daily report — Unit Angkutan Penumpang.

Same layout structure.

CARD 2 — Data Harian (required):
Table with columns: Nama KA | Jumlah Penumpang | Pendapatan (Rp)
Rows: list of train names (KA Sribilah, KA Putri Deli, dll)
"+ Tambah KA" button (blue outline)
Bottom totals row: Total Penumpang | Total Pendapatan

CARD 3 — Kumulatif:
- Total Penumpang Tahun Berjalan: number input
- Total Pendapatan Tahun Berjalan: number input

CARD 4 — Target vs Realisasi:
- Target Penumpang: number input
- Realisasi Penumpang: auto-sum
- Persentase: auto-calculated progress bar

CARD 5 — Box Detail (opsional)
```

---

## HALAMAN 8 — INPUT LAPORAN (Keuangan)

```
Design an input form page for daily report — Unit Keuangan.

CARD 2 — Data Harian:
- Pendapatan Harian (Rp): number input with Rp prefix
- Pengeluaran Harian (Rp): number input with Rp prefix
- Laba/Rugi Harian: auto-calculated, show green if positive, red if negative

CARD 3 — Kumulatif:
- Total Pendapatan Kumulatif (Rp): number input
- Total Laba/Rugi Kumulatif (Rp): auto-calculated, colored

CARD 4 — Target vs Realisasi:
- Target Pendapatan: number input
- Realisasi Pendapatan: number input
- Persentase: auto-calculated

CARD 5 — Box Detail (opsional)
```

---

## HALAMAN 9 — REVIEW LAPORAN (Admin Global)

```
Design a report review page for Admin Global.

Page title: "Review Laporan" breadcrumb "Dashboard > Laporan > Review"

Left section (60%): Report detail card
- Header: Unit name, tanggal, jenis laporan
- Status badge current: amber "MENUNGGU REVIEW"
- All report data displayed in read-only format (same sections as input form)
- Box detail section if filled

Right section (40%): Review action card (sticky)
- Title: "Tindakan Review"
- Reviewer info: Admin name, timestamp
- Large green button: "ACC - Terima Laporan" with checkmark icon
- Separator "atau"
- Textarea: "Catatan Revisi (wajib jika REVISI)"
- Large red outline button: "REVISI - Kembalikan Laporan" with X icon
- Warning text below REVISI button: "Notifikasi WhatsApp akan dikirim otomatis ke unit terkait"

Confirmation modal when clicking ACC:
- "Apakah Anda yakin ingin meng-ACC laporan ini?"
- Cancel | Konfirmasi ACC button

Confirmation modal when clicking REVISI:
- "Laporan akan dikembalikan untuk diperbaiki"
- "Catatan revisi: [text]"
- "Notifikasi WA akan dikirim ke unit"
- Cancel | Kirim Revisi button
```

---

## HALAMAN 10 — HELPDESK (User — Ajukan Tiket)

```
Design a helpdesk submission page for users in PT KAI system.

Page title: "Helpdesk & Bantuan"

Top info card: light blue background
"Butuh bantuan? Ajukan tiket dan tim kami akan segera membantu."

Form card — "Buat Tiket Baru":
- Jenis Permintaan (required): radio buttons or segmented control
  - TOKEN (lock icon): "Reset Password / Akun Terkunci → akan ditangani IT Support"
  - ISSUE (warning icon): "Masalah Teknis Sistem → akan ditangani IT Support"
  - REVISION (document icon): "Revisi Laporan yang Sudah Disubmit → akan ditangani Admin Global"

- Conditional field if REVISION selected:
  "Pilih Laporan" dropdown: list of submitted reports with date

- Deskripsi (required): textarea placeholder "Jelaskan masalah atau permintaan Anda secara detail..."

- Primary blue button: "Kirim Tiket"

After submit: success state card with green checkmark:
"Tiket berhasil dikirim! Tim terkait akan segera menindaklanjuti."
If TOKEN: "IT Support akan mengirim token reset password ke WhatsApp Anda."
If REVISION: "Notifikasi WhatsApp telah dikirim ke Admin Global."
```

---

## HALAMAN 11 — HELPDESK (IT Support — Handle Tiket TOKEN)

```
Design a helpdesk management page for IT Support role.

Sidebar navigation:
- Dashboard
- Helpdesk (active) - with red badge showing pending count
- Monitoring Sistem
- Settings
- Keluar

Main content:
Tabs: "TOKEN (3)" | "ISSUE (2)" | "Semua"

Table — daftar tiket TOKEN:
Columns: ID TIKET | NAMA USER | UNIT | WAKTU AJUKAN | STATUS | AKSI
Row example: 
- TKT-001 | Ahmad Fauzi | Unit Angkutan Barang | 24 Apr 2025, 09:15 | amber "OPEN" | "Handle" blue button

When clicking "Handle" → side panel opens:
- User info: nama, unit, nomor WA
- Deskripsi masalah dari user
- Divider "Generate Token Reset Password"
- Token preview field (auto-generated, monospace): "TK-7X9A2M" with "Regenerate" link
- Token expiry: "Berlaku selama 1 jam"
- Large blue button: "Generate & Kirim via WhatsApp"
- After send: green success "Token berhasil dikirim ke +62812-xxxx-xxxx"
- Close button & mark as resolved
```

---

## HALAMAN 12 — DASHBOARD IT SUPPORT

```
Design a dashboard for IT Support role.

Sidebar:
- Dashboard (active)
- Helpdesk
- Monitoring Sistem
- Keluar

Summary cards:
- Tiket TOKEN Pending: "3" red badge, needs action
- Tiket ISSUE Pending: "2" amber badge
- Total Tiket Hari Ini: "8"
- Token Generated Hari Ini: "5"

Recent tickets table same as helpdesk page
System monitoring section: simple status indicators (green dot = online) for Backend, Database, WhatsApp Gateway
```

---

## HALAMAN 13 — GRAFIK & VISUALISASI DASHBOARD (Per Unit)

```
Design a data visualization / analytics page for a single unit in PT KAI system.

Page title: "Analitik Unit — Angkutan Barang"
Filter: Bulan dropdown | Tahun dropdown | "Terapkan" button | "Export Excel" button | "Export PDF" button

Section 1 — Grafik Mingguan (bar chart):
Title: "Trend Volume per Minggu — Mei 2024"
X-axis: Minggu 1, Minggu 2, Minggu 3, Minggu 4
Y-axis: Volume (Ton)
Blue bars, hover tooltip
Stats below: AVERAGE | PEAK | GROWTH

Section 2 — Grafik Tahunan (bar chart):
Title: "Trend Volume per Bulan — 2024"
X-axis: Jan - Des
Y-axis: Volume (Ton)
Blue bars, current month highlighted darker

Section 3 — Target vs Realisasi card:
Horizontal comparison bar: Target (gray) vs Realisasi (blue)
Percentage achievement: large bold "78.5%" 
Status: amber "Di Bawah Target"

Note: ALL charts are bar charts only (no pie charts)
```

---

## HALAMAN 14 — MANAJEMEN USER (Admin Global)

```
Design a user management page for Admin Global.

Page title: "Manajemen User"
Top right: blue button "+ Tambah User Baru"

Search bar + filter by role dropdown + filter by unit dropdown

Table:
Columns: NAMA | EMAIL | ROLE | UNIT | STATUS | AKSI
Row example:
- Ahmad Fauzi | ahmad@kai.id | User Unit | Angkutan Barang | green "Aktif" | Edit icon | Lock icon
- Budi Santoso | budi@kai.id | Admin Global | - | green "Aktif" | Edit icon
- Citra Dewi | citra@kai.id | User Unit | KNA | red "Terkunci" | Edit icon | Unlock icon

Add/Edit User modal:
- Nama Lengkap input
- Email input
- No. WhatsApp input (for token & notifications)
- Role dropdown: User Unit / Admin Global / IT Support
- Unit dropdown (only shows if role = User Unit)
- Password (auto-generated, shown once)
- Save button
```

---

## CATATAN STYLE KONSISTEN (Tambahkan di setiap prompt)

```
Consistent UI rules across all pages:
- Sidebar always dark navy #0D3472, 220px wide
- Active sidebar item: blue highlight with left border accent
- All cards: white, border-radius 12px, subtle shadow
- All primary buttons: #1A5FCC blue, border-radius 8px, white text
- All outline buttons: white background, blue border, blue text
- Status badges (pill shape, 6px padding):
  - ACC / TERVERIFIKASI: #DCFCE7 background, #16A34A text
  - WAITING / MENUNGGU: #FEF9C3 background, #CA8A04 text
  - REVISI / PERBAIKAN: #FEE2E2 background, #DC2626 text
  - DRAFT: #F1F5F9 background, #64748B text
- Tables: alternating row white/#F8FAFC, hover #EFF6FF
- All charts: bar charts only, primary blue #1A5FCC bars
- Form inputs: border #D1D5DB, focus border #1A5FCC, border-radius 8px
- PT KAI logo: top-left sidebar, white version
- Footer: "© 2024 PT Kereta Api Indonesia (Persero) Divisi Regional I Sumatera Utara. All rights reserved."
```
