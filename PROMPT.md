Create a low-fidelity wireframe prototype for a web-based internal reporting system called Sistem Monitoring & Pelaporan PT KAI Divre I Sumatera Utara.

LOW-FI RULES — STRICT:
- Layout boxes and labels only. No real content.
- No actual data, numbers, names, or copy inside elements.
- Every element is a gray rectangle with a short label: [SIDEBAR], [TABLE], [CHART: BAR], [FORM INPUT], [BUTTON], [BADGE], [MODAL], etc.
- No icons, no images, no color, no typography styling.
- Grayscale only: white background, light gray boxes, dark gray labels.
- Desktop layout, 1440px wide.

---

GLOBAL LAYOUT (apply to all screens except Login and Reset Password):
- Left: [SIDEBAR 220px] with stacked [NAV ITEM] rows, different per role
- Top: [HEADER BAR] with [PAGE TITLE] left and [USER AVATAR] right
- Center: [MAIN CONTENT AREA]
- Bottom: [FOOTER BAR]

---

SCREEN 1 — Login
Two-column layout:
- Left 40%: [BRAND PANEL] containing [IMAGE: LOGO] and [TEXT BLOCK: tagline]
- Right 60%: [LOGIN FORM] containing [INPUT: email], [INPUT: password], [LINK: forgot password], [BUTTON: login]
- State A: [ALERT BOX: error message]
- State B: [ALERT BOX: locked] + [BUTTON: helpdesk]

Links to: SCREEN 2, SCREEN 3, SCREEN 4, SCREEN 12

---

SCREEN 2 — Reset Password
Centered single card:
- [LINK: back]
- [ICON PLACEHOLDER]
- [TEXT BLOCK: title]
- [INPUT: token]
- [INPUT: new password]
- [INPUT: confirm password]
- [PROGRESS BAR: password strength]
- [BUTTON: reset]
- State A: [ALERT: error]
- State B: [ALERT: success]

Links to: SCREEN 1

---

SCREEN 3 — Dashboard Admin Global
Sidebar nav: [NAV: Dashboard] [NAV: Laporan] [NAV: History Laporan] [NAV: Manajemen Unit] [NAV: Manajemen User] [NAV: Helpdesk] [NAV: Notifikasi] [NAV: Settings] [NAV: Keluar]

Main content:
- Row: [KPI CARD] [KPI CARD] [KPI CARD] [KPI CARD]
- [FILTER BAR] with [DROPDOWN] [DROPDOWN] [DROPDOWN] [BUTTON] [BUTTON] [BUTTON]
- Row: [CHART: BAR 60%] [CHART: LINE 40%]
- [TABLE: laporan status] with [BADGE] per row

Links to: SCREEN 9, SCREEN 14, SCREEN 10, SCREEN 15

---

SCREEN 4 — Dashboard User Unit
Sidebar nav: [NAV: Dashboard] [NAV: Input Laporan] [NAV: History Laporan] [NAV: Target Saya] [NAV: Helpdesk] [NAV: Keluar]

Main content:
- Row: [STATUS CARD] [STATUS CARD] [STATUS CARD: ring chart]
- [ALERT BANNER] + [BUTTON]
- [CHART: BAR]
- [TABLE: history laporan] with [BADGE] per row

Links to: SCREEN 5, SCREEN 10

---

SCREEN 5 — Input Laporan: Angkutan Barang
Breadcrumb: [BREADCRUMB]
[STEPPER: 3 steps]

- [CARD: header laporan — 3 read-only fields]
- [CARD: data harian — TABLE with input cells] + [BUTTON: tambah row]
- [CARD: data kumulatif — 2 inputs]
- [CARD: target vs realisasi — 2 inputs + PROGRESS BAR]
- [CARD: box detail — TEXTAREA optional]
- Actions: [BUTTON: draft] [BUTTON: validasi] [BUTTON: submit — hidden until validated]

Links to: SCREEN 4

---

SCREEN 6 — Input Laporan: KNA
Same layout as SCREEN 5.

- [CARD: header laporan]
- [CARD: data harian — 2 sub-sections, each 3 inputs]
- [CARD: data kumulatif — 3 inputs, 1 auto-calc]
- [CARD: target vs realisasi RKAD — 2 inputs + PROGRESS BAR + note]
- [CARD: box detail — TEXTAREA optional]
- Actions: [BUTTON: draft] [BUTTON: validasi] [BUTTON: submit]

---

SCREEN 7 — Input Laporan: Angkutan Penumpang
Same layout as SCREEN 5.

- [CARD: header laporan]
- [CARD: data harian — TABLE with input cells] + [BUTTON: tambah row]
- [CARD: data kumulatif — 2 inputs]
- [CARD: target vs realisasi — 2 inputs + PROGRESS BAR]
- [CARD: box detail — TEXTAREA optional]
- Actions: [BUTTON: draft] [BUTTON: validasi] [BUTTON: submit]

---

SCREEN 8 — Input Laporan: Keuangan
Same layout as SCREEN 5.

- [CARD: header laporan]
- [CARD: data harian — 3 inputs, 1 auto-calc]
- [CARD: data kumulatif — 2 inputs, 1 auto-calc]
- [CARD: target vs realisasi — 2 inputs + auto %]
- [CARD: box detail — TEXTAREA optional]
- Actions: [BUTTON: draft] [BUTTON: validasi] [BUTTON: submit]

---

SCREEN 9 — Review Laporan (Admin Global)
Breadcrumb: [BREADCRUMB]

Two-column layout:
- Left 60%: [CARD: report detail — read-only sections, BADGE: current status]
- Right 40% sticky: [CARD: review actions]
  - [BUTTON: ACC full-width]
  - [DIVIDER]
  - [TEXTAREA: catatan revisi]
  - [BUTTON: REVISI outline full-width]
  - [TEXT: whatsapp notification warning]

Overlay: [MODAL: ACC confirmation — BUTTON cancel, BUTTON confirm]
Overlay: [MODAL: REVISI confirmation — BUTTON cancel, BUTTON send]

Links to: SCREEN 3

---

SCREEN 10 — Helpdesk: Ajukan Tiket (User Unit)
- [INFO BOX]
- [CARD: form tiket]
  - [RADIO GROUP: 3 options]
  - [DROPDOWN: conditional — shown only if REVISION selected]
  - [TEXTAREA: deskripsi]
  - [BUTTON: kirim]
- State: [SUCCESS CARD]

Links to: SCREEN 11

---

SCREEN 11 — Helpdesk: Handle Tiket (IT Support)
Sidebar nav: [NAV: Dashboard] [NAV: Helpdesk — active, badge] [NAV: Monitoring] [NAV: Settings] [NAV: Keluar]

- [TAB BAR: TOKEN, ISSUE, Semua]
- [TABLE: daftar tiket] with [BADGE] and [BUTTON: handle] per row

Side panel (on Handle click):
- [TEXT BLOCK: user info]
- [TEXT BLOCK: deskripsi]
- [DIVIDER]
- [TOKEN DISPLAY BOX] + [LINK: regenerate]
- [TEXT: expiry]
- [BUTTON: generate and send]
- State: [SUCCESS TEXT]
- [BUTTON: close]

Links to: SCREEN 2

---

SCREEN 12 — Dashboard IT Support
Sidebar nav: [NAV: Dashboard — active] [NAV: Helpdesk] [NAV: Monitoring] [NAV: Keluar]

Main content:
- Row: [KPI CARD] [KPI CARD] [KPI CARD] [KPI CARD]
- [TABLE: recent tickets] with [BADGE] per row
- [MONITORING SECTION]: Row of [STATUS INDICATOR] boxes

Links to: SCREEN 11

---

SCREEN 13 — Grafik & Visualisasi
- [FILTER BAR]: [DROPDOWN] [DROPDOWN] [BUTTON] [BUTTON: export] [BUTTON: export]
- [CARD: CHART BAR — mingguan] + [STATS ROW: 3 values]
- [CARD: CHART BAR — tahunan]
- [CARD: TARGET VS REALISASI] — [PROGRESS BAR horizontal] + [BADGE: status]

---

SCREEN 14 — Manajemen User (Admin Global)
- [BUTTON: tambah user] top right
- [FILTER BAR]: [SEARCH INPUT] [DROPDOWN] [DROPDOWN]
- [TABLE: daftar user] with [BADGE: status] and [ICON BTN] per row

Overlay: [MODAL: form tambah/edit user]
- [INPUT] x5
- [DROPDOWN: role]
- [DROPDOWN: unit — conditional]
- [TEXT: auto-generated password]
- [BUTTON: simpan]

---

SCREEN 15 — Settings
Sidebar nav: same as role (Admin Global or IT Support)
Page title: Settings

Sections as cards:
- [CARD: Preferensi Tampilan]
  - [LABEL: Bahasa] + [TOGGLE: ID / EN]
  - [LABEL: Tema] + [TOGGLE: Light / Dark]
- [CARD: Notifikasi]
  - [TOGGLE ITEM] x3
- [CARD: Keamanan]
  - [BUTTON: Ganti Password]
- [BUTTON: Simpan Perubahan]

---

PROTOTYPE FLOWS:

Flow A — User Unit:
SCREEN 1 → SCREEN 4
SCREEN 4 → SCREEN 5
SCREEN 4 → SCREEN 10
SCREEN 5 → SCREEN 4

Flow B — Admin Global:
SCREEN 1 → SCREEN 3
SCREEN 3 → SCREEN 9
SCREEN 3 → SCREEN 14
SCREEN 3 → SCREEN 15
SCREEN 9 → SCREEN 3

Flow C — IT Support:
SCREEN 1 → SCREEN 12
SCREEN 12 → SCREEN 11
SCREEN 12 → SCREEN 15
SCREEN 11 → SCREEN 2
