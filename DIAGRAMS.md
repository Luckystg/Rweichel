# DIAGRAM SISTEM
# Sistem Monitoring dan Pelaporan Kinerja Unit PT KAI Divre I Sumatera Utara

> Semua diagram menggunakan sintaks **Mermaid**.
> Untuk render: gunakan VS Code + extension "Mermaid Preview", atau paste ke https://mermaid.live

---

## A. USE CASE DIAGRAM

```mermaid
graph TB
    subgraph Actors["ACTORS"]
        UU["👤 User Unit"]
        AG["👤 Admin Global"]
        IT["👤 IT Support"]
    end

    subgraph System["SISTEM KAI"]
        subgraph Auth["Autentikasi"]
            UC1(["Login"])
            UC2(["Reset Password via Token"])
        end

        subgraph LaporanUC["Manajemen Laporan"]
            UC3(["Input Laporan Harian"])
            UC4(["Tambah Komoditi Barang"])
            UC5(["Input Target / RKAP"])
            UC6(["Validasi Internal Laporan"])
            UC7(["Submit Laporan"])
            UC8(["Lihat Status Laporan"])
            UC9(["Export Laporan PDF / Excel"])
        end

        subgraph AdminUC["Review & Monitoring"]
            UC10(["Review Laporan"])
            UC11(["ACC Laporan"])
            UC12(["Set Status REVISI"])
            UC13(["Monitor Semua Unit"])
            UC14(["Kelola Akun User"])
            UC15(["Kelola Unit"])
            UC16(["Lihat Dashboard & Grafik"])
        end

        subgraph HelpdeskUC["Helpdesk"]
            UC17(["Ajukan Helpdesk TOKEN"])
            UC18(["Ajukan Helpdesk ISSUE"])
            UC19(["Ajukan Helpdesk REVISION"])
            UC20(["Handle Helpdesk TOKEN"])
            UC21(["Handle Helpdesk ISSUE"])
            UC22(["Handle Helpdesk REVISION"])
            UC23(["Generate Token Reset Password"])
        end
    end

    UU --> UC1
    UU --> UC2
    UU --> UC3
    UU --> UC4
    UU --> UC5
    UU --> UC6
    UU --> UC7
    UU --> UC8
    UU --> UC9
    UU --> UC17
    UU --> UC18
    UU --> UC19

    AG --> UC1
    AG --> UC10
    AG --> UC11
    AG --> UC12
    AG --> UC13
    AG --> UC14
    AG --> UC15
    AG --> UC16
    AG --> UC22
    AG --> UC9

    IT --> UC1
    IT --> UC20
    IT --> UC21
    IT --> UC23
    IT --> UC13
```

---

## B. ACTIVITY DIAGRAMS

### B.1 — Activity: Login & Mekanisme Lock Akun

```mermaid
flowchart TD
    Start([Mulai]) --> A[User Buka Halaman Login]
    A --> B[Input Email & Password]
    B --> C{Akun\nTer-lock?}
    C -- Ya --> D[Tampil Pesan: Akun Terkunci\nHubungi IT Support]
    D --> End1([Selesai])
    C -- Tidak --> E{Kredensial\nValid?}
    E -- Ya --> F[Reset loginAttempts = 0]
    F --> G[Generate JWT Token]
    G --> H[Redirect ke Dashboard]
    H --> End2([Selesai])
    E -- Tidak --> I[loginAttempts + 1]
    I --> J{loginAttempts\n>= 3?}
    J -- Tidak --> K[Tampil Pesan: Email/Password Salah\nSisa percobaan: N]
    K --> B
    J -- Ya --> L[Set isLocked = true]
    L --> M[Tampil Pesan: Akun Terkunci\nHubungi IT Support]
    M --> End3([Selesai])
```

---

### B.2 — Activity: Reset Password via Token

```mermaid
flowchart TD
    Start([Mulai]) --> A[User Ajukan Helpdesk\nJenis TOKEN]
    A --> B[Notifikasi WA dikirim ke IT Support]
    B --> C[IT Support Terima Request]
    C --> D[IT Support Generate Token\none-time, ada expiry]
    D --> E[Token Dikirim ke User via WhatsApp]
    E --> F[User Buka Halaman Reset Password]
    F --> G[Input Token + Password Baru]
    G --> H{Token\nValid & Belum\nExpired?}
    H -- Tidak --> I[Tampil Pesan: Token Tidak Valid / Expired]
    I --> F
    H -- Ya --> J{Token\nSudah Dipakai?}
    J -- Ya --> I
    J -- Tidak --> K[Update Password Baru di DB - Atomic]
    K --> L[Invalidate Token\nisUsed = true]
    L --> M[Set isLocked = false\nloginAttempts = 0]
    M --> N[Tampil Pesan: Password Berhasil Diubah]
    N --> O[Redirect ke Halaman Login]
    O --> End([Selesai])
```

---

### B.3 — Activity: Input Laporan & Validasi Internal

```mermaid
flowchart TD
    Start([Mulai]) --> A[User Buka Form Input Laporan]
    A --> B{Sudah Ada Laporan\nHari Ini?}
    B -- Ya --> C[Tampil Pesan: Laporan Hari Ini Sudah Ada]
    C --> End1([Selesai])
    B -- Tidak --> D[Isi Data Wajib:\nHarian + Kumulatif + Target vs Realisasi]
    D --> E[Isi Box Detail\nOpsional - Boleh Kosong]
    E --> F[Simpan sebagai DRAFT]
    F --> G[User Cek Kelengkapan Data]
    G --> H{Data\nSudah Lengkap\n& Benar?}
    H -- Tidak --> I[Set Status: NEED_REVISION_INTERNAL]
    I --> J[User Perbaiki Data]
    J --> G
    H -- Ya --> K[Set Status: READY_TO_SUBMIT]
    K --> L{User Mau\nSubmit?}
    L -- Tidak --> M[Simpan sebagai READY_TO_SUBMIT\nBisa Submit Nanti]
    M --> End2([Selesai])
    L -- Ya --> N[Submit Laporan]
    N --> O[Set Status: WAITING]
    O --> P[Notifikasi Realtime ke Admin]
    P --> End3([Selesai])
```

---

### B.4 — Activity: Admin Review Laporan

```mermaid
flowchart TD
    Start([Mulai]) --> A[Admin Buka Dashboard]
    A --> B[Lihat Daftar Laporan Status WAITING]
    B --> C[Pilih Laporan untuk Direview]
    C --> D[Baca Detail Laporan]
    D --> E{Laporan\nSudah Sesuai?}
    E -- Ya --> F[Set Status: ACC]
    F --> G[Tampil Notifikasi Realtime ke User Unit]
    G --> End1([Selesai])
    E -- Tidak --> H[Input Catatan Revisi]
    H --> I[Set Status: REVISI]
    I --> J[Kirim Notifikasi WA ke User Unit]
    J --> K[Kirim Notifikasi Realtime ke User Unit]
    K --> End2([Selesai])
```

---

### B.5 — Activity: Edit Laporan Setelah Submit (via Helpdesk)

```mermaid
flowchart TD
    Start([Mulai]) --> A[User Lihat Laporan\nStatus WAITING / ACC]
    A --> B[User Ajukan Helpdesk\nJenis REVISION]
    B --> C[Sistem Kirim Notifikasi WA\nke Admin Global]
    C --> D[Admin Terima Notifikasi]
    D --> E{Admin\nSetuju Revisi?}
    E -- Tidak --> F[Admin Tolak Request\nInfokan ke User]
    F --> End1([Selesai])
    E -- Ya --> G[Admin Set Status Laporan\nmenjadi REVISI]
    G --> H[Notifikasi Realtime ke User]
    H --> I[User Edit Laporan]
    I --> J[User Validasi Internal Ulang]
    J --> K{Status\nREADY_TO_SUBMIT?}
    K -- Tidak --> I
    K -- Ya --> L[User Submit Ulang]
    L --> M[Status kembali ke WAITING]
    M --> N[Admin Review Ulang]
    N --> End2([Selesai])
```

---

### B.6 — Activity: Helpdesk System

```mermaid
flowchart TD
    Start([Mulai]) --> A[User Buka Form Helpdesk]
    A --> B[Pilih Jenis Helpdesk]
    B --> C{Jenis\nHelpdesk?}

    C -- TOKEN --> D[Isi Deskripsi Masalah Lock Akun]
    D --> E[Submit ke IT Support]
    E --> F[IT Support Terima Tiket]
    F --> G[IT Generate Token Reset Password]
    G --> H[Kirim Token via WA ke User]
    H --> End1([Selesai])

    C -- ISSUE --> I[Isi Deskripsi Masalah Teknis]
    I --> J[Submit ke IT Support]
    J --> K[IT Support Analisis & Handle]
    K --> L[Update Status Tiket]
    L --> End2([Selesai])

    C -- REVISION --> M[Isi Alasan Permintaan Revisi Laporan]
    M --> N[Submit ke Admin Global]
    N --> O[Kirim Notifikasi WA ke Admin]
    O --> P[Admin Handle Request Revisi]
    P --> End3([Selesai])
```

---

## C. SEQUENCE DIAGRAMS

### C.1 — Sequence: Login

```mermaid
sequenceDiagram
    actor U as User
    participant FE as Frontend (React)
    participant BE as Backend (Express)
    participant DB as Database (MySQL)

    U->>FE: Input email & password
    FE->>BE: POST /api/auth/login
    BE->>DB: SELECT user WHERE email = ?
    DB-->>BE: Data user

    alt Akun ter-lock
        BE-->>FE: 403 - Akun terkunci
        FE-->>U: Tampil pesan: Hubungi IT Support
    else Kredensial salah
        BE->>DB: UPDATE loginAttempts + 1
        alt loginAttempts >= 3
            BE->>DB: UPDATE isLocked = true
            BE-->>FE: 403 - Akun terkunci
            FE-->>U: Tampil pesan: Akun dikunci
        else loginAttempts < 3
            BE-->>FE: 401 - Email/Password salah
            FE-->>U: Tampil sisa percobaan
        end
    else Kredensial benar
        BE->>DB: UPDATE loginAttempts = 0
        BE->>BE: Generate JWT Token
        BE-->>FE: 200 - JWT Token + data user
        FE->>FE: Simpan token di localStorage
        FE-->>U: Redirect ke Dashboard
    end
```

---

### C.2 — Sequence: Reset Password via Token

```mermaid
sequenceDiagram
    actor U as User Unit
    actor IT as IT Support
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database
    participant WA as WhatsApp (Baileys)

    U->>FE: Ajukan helpdesk jenis TOKEN
    FE->>BE: POST /api/helpdesk (jenis: TOKEN)
    BE->>DB: INSERT SupportRequest
    BE->>WA: Kirim notifikasi ke IT Support
    WA-->>IT: Notifikasi WA masuk

    IT->>FE: Buka tiket helpdesk
    IT->>FE: Generate token untuk user
    FE->>BE: POST /api/token/generate (userId)
    BE->>BE: Generate random token + set expiry
    BE->>DB: INSERT ResetToken
    BE->>WA: Kirim token ke nomor WA user
    WA-->>U: Terima token via WA

    U->>FE: Buka halaman reset password
    U->>FE: Input token + password baru
    FE->>BE: POST /api/auth/reset-password
    BE->>DB: SELECT ResetToken WHERE token = ?
    DB-->>BE: Data token

    alt Token valid & belum expired & belum dipakai
        BE->>DB: UPDATE User SET password = hash(passwordBaru) [atomic]
        BE->>DB: UPDATE ResetToken SET isUsed = true
        BE->>DB: UPDATE User SET isLocked = false, loginAttempts = 0
        BE-->>FE: 200 - Password berhasil diubah
        FE-->>U: Redirect ke Login
    else Token tidak valid / expired / sudah dipakai
        BE-->>FE: 400 - Token tidak valid
        FE-->>U: Tampil pesan error
    end
```

---

### C.3 — Sequence: Submit Laporan

```mermaid
sequenceDiagram
    actor U as User Unit
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database
    participant SO as Socket.io

    U->>FE: Buka form input laporan
    FE->>BE: GET /api/report/today (unitId)
    BE->>DB: SELECT report WHERE unitId & tanggal = today
    DB-->>BE: Result

    alt Laporan sudah ada
        BE-->>FE: Data laporan existing
        FE-->>U: Tampil pesan sudah ada laporan hari ini
    else Laporan belum ada
        BE-->>FE: 404 - Belum ada
        FE-->>U: Tampil form input kosong

        U->>FE: Isi data laporan + box detail (opsional)
        FE->>BE: POST /api/report (data laporan)
        BE->>DB: INSERT Report (status: DRAFT)
        BE->>DB: INSERT ReportKNA / ReportPassenger / ReportCargo / ReportFinance
        DB-->>BE: Success
        BE-->>FE: 201 - Laporan tersimpan sebagai DRAFT

        U->>FE: Klik Validasi Internal
        FE->>BE: PATCH /api/report/:id/validate-internal
        BE->>BE: Cek kelengkapan data
        BE->>DB: UPDATE Report SET internalStatus = READY_TO_SUBMIT
        BE-->>FE: 200 - Status: READY_TO_SUBMIT

        U->>FE: Klik Submit
        FE->>BE: PATCH /api/report/:id/submit
        BE->>DB: Cek internalStatus = READY_TO_SUBMIT
        BE->>DB: UPDATE Report SET status = WAITING
        BE->>SO: Emit event 'new-report' ke Admin
        SO-->>FE: Admin terima notifikasi realtime
        BE-->>FE: 200 - Laporan berhasil disubmit
        FE-->>U: Tampil status: WAITING
    end
```

---

### C.4 — Sequence: Admin Review Laporan (ACC / REVISI)

```mermaid
sequenceDiagram
    actor A as Admin Global
    actor U as User Unit
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database
    participant SO as Socket.io
    participant WA as WhatsApp (Baileys)

    A->>FE: Buka daftar laporan WAITING
    FE->>BE: GET /api/report?status=WAITING
    BE->>DB: SELECT reports WHERE status = WAITING
    DB-->>BE: List laporan
    BE-->>FE: Data laporan
    FE-->>A: Tampil daftar laporan

    A->>FE: Buka detail laporan
    FE->>BE: GET /api/report/:id
    BE-->>FE: Detail laporan
    FE-->>A: Tampil detail

    alt Admin ACC
        A->>FE: Klik ACC
        FE->>BE: PATCH /api/report/:id/review (status: ACC)
        BE->>DB: UPDATE Report SET status = ACC
        BE->>DB: INSERT AuditLog
        BE->>SO: Emit 'report-reviewed' ke User Unit
        SO-->>FE: User terima notifikasi realtime
        BE-->>FE: 200 - Status ACC
        FE-->>A: Tampil konfirmasi ACC
    else Admin REVISI
        A->>FE: Isi catatan revisi + Klik REVISI
        FE->>BE: PATCH /api/report/:id/review (status: REVISI, catatan)
        BE->>DB: UPDATE Report SET status = REVISI
        BE->>DB: INSERT AuditLog
        BE->>SO: Emit 'report-revised' ke User Unit
        SO-->>FE: User terima notifikasi realtime
        BE->>WA: Kirim notifikasi WA ke User Unit
        WA-->>U: Terima notifikasi WA revisi laporan
        BE-->>FE: 200 - Status REVISI
        FE-->>A: Tampil konfirmasi REVISI
    end
```

---

### C.5 — Sequence: Helpdesk REVISION (Edit Laporan Setelah Submit)

```mermaid
sequenceDiagram
    actor U as User Unit
    actor A as Admin Global
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database
    participant WA as WhatsApp (Baileys)
    participant SO as Socket.io

    U->>FE: Ajukan helpdesk jenis REVISION
    FE->>BE: POST /api/helpdesk (jenis: REVISION, reportId)
    BE->>DB: INSERT SupportRequest
    BE->>WA: Kirim notifikasi WA ke Admin Global
    WA-->>A: Terima notifikasi WA

    A->>FE: Buka tiket helpdesk REVISION
    FE->>BE: GET /api/helpdesk/:id
    BE-->>FE: Detail tiket
    FE-->>A: Tampil detail request

    A->>FE: Set status laporan → REVISI
    FE->>BE: PATCH /api/report/:id/set-revisi
    BE->>DB: UPDATE Report SET status = REVISI
    BE->>DB: UPDATE SupportRequest SET status = RESOLVED
    BE->>SO: Emit 'report-set-revisi' ke User Unit
    SO-->>FE: User terima notifikasi realtime
    BE-->>FE: 200 - Success

    U->>FE: Edit laporan
    FE->>BE: PUT /api/report/:id (data baru)
    BE->>DB: UPDATE Report + detail
    BE-->>FE: 200 - Tersimpan

    U->>FE: Validasi internal + Submit ulang
    FE->>BE: PATCH /api/report/:id/submit
    BE->>DB: UPDATE Report SET status = WAITING
    BE->>SO: Emit 'report-resubmitted' ke Admin
    BE-->>FE: 200 - Status WAITING
    FE-->>U: Tampil status WAITING
```

---

## D. ERD (ENTITY RELATIONSHIP DIAGRAM)

```mermaid
erDiagram
    USER {
        int id PK
        string nama
        string email
        string password
        enum role "USER_UNIT, ADMIN_GLOBAL, IT_SUPPORT"
        int unitId FK
        int loginAttempts
        boolean isLocked
        string noHP
        datetime createdAt
        datetime updatedAt
    }

    UNIT {
        int id PK
        string namaUnit
        enum jenisUnit "KNA, PENUMPANG, BARANG, KEUANGAN"
        datetime createdAt
    }

    REPORT {
        int id PK
        int unitId FK
        int userId FK
        date tanggal
        enum internalStatus "DRAFT, NEED_REVISION_INTERNAL, READY_TO_SUBMIT"
        enum status "WAITING, ACC, REVISI"
        text boxDetail "nullable - opsional"
        datetime createdAt
        datetime updatedAt
    }

    REPORT_KNA {
        int id PK
        int reportId FK
        int jumlahKontrakROW
        float luasROW
        float nilaiROW
        int jumlahKontrakNonROW
        float luasNonROW
        float nilaiNonROW
        float rkadTarget
        float rkadRealisasi
    }

    REPORT_PASSENGER {
        int id PK
        int reportId FK
        string namaKA
        int jumlahPenumpang
        float pendapatan
    }

    REPORT_CARGO {
        int id PK
        int reportId FK
        int komoditiId FK
        int jumlahKA
        float volume
        float pendapatan
    }

    CARGO_COMMODITY {
        int id PK
        int unitId FK
        string namaKomoditi
        string satuan
        datetime createdAt
    }

    REPORT_FINANCE {
        int id PK
        int reportId FK
        float pendapatan
        float pengeluaran
        float labaRugi
    }

    TARGET {
        int id PK
        int unitId FK
        int tahun
        string kategori
        float nilai
        datetime createdAt
    }

    SUPPORT_REQUEST {
        int id PK
        int userId FK
        int reportId FK "nullable"
        enum jenis "TOKEN, ISSUE, REVISION"
        text deskripsi
        enum status "OPEN, IN_PROGRESS, RESOLVED"
        int handledById FK "nullable"
        datetime createdAt
        datetime updatedAt
    }

    RESET_TOKEN {
        int id PK
        int userId FK
        string token
        boolean isUsed
        datetime expiredAt
        datetime createdAt
    }

    AUDIT_LOG {
        int id PK
        int userId FK
        string aksi
        text detail
        datetime createdAt
    }

    USER ||--o{ REPORT : "membuat"
    UNIT ||--|{ REPORT : "memiliki"
    UNIT ||--o{ USER : "memiliki"
    UNIT ||--o{ TARGET : "memiliki"
    UNIT ||--o{ CARGO_COMMODITY : "memiliki"

    REPORT ||--o| REPORT_KNA : "detail KNA"
    REPORT ||--o{ REPORT_PASSENGER : "detail penumpang"
    REPORT ||--o{ REPORT_CARGO : "detail barang"
    REPORT ||--o| REPORT_FINANCE : "detail keuangan"

    REPORT_CARGO }|--|| CARGO_COMMODITY : "menggunakan"

    USER ||--o{ SUPPORT_REQUEST : "mengajukan"
    USER ||--o{ RESET_TOKEN : "memiliki"
    USER ||--o{ AUDIT_LOG : "mencatat"
    REPORT ||--o{ SUPPORT_REQUEST : "terkait"
```

---

## E. DFD (DATA FLOW DIAGRAM)

### E.1 — DFD Level 0: Context Diagram

```mermaid
flowchart LR
    UU["👤 User Unit"]
    AG["👤 Admin Global"]
    IT["👤 IT Support"]
    WA["📱 WhatsApp\nGateway"]

    subgraph SYS["⬛ SISTEM KAI"]
        S(["Sistem Monitoring\n& Pelaporan\nKinerja Unit\nPT KAI Divre I Sumut"])
    end

    UU -- "Data laporan,\ndata target,\ndata komoditi,\nrequest helpdesk" --> S
    S -- "Status laporan,\nnotifikasi revisi,\nexport PDF/Excel" --> UU

    AG -- "Keputusan ACC/REVISI,\nkelola user & unit" --> S
    S -- "Data semua laporan,\ndashboard grafik,\ntiket helpdesk" --> AG

    IT -- "Token reset password,\npenanganan isu teknis" --> S
    S -- "Tiket helpdesk TOKEN/ISSUE,\ndata monitoring sistem" --> IT

    S -- "Notifikasi revisi,\nreminder 16:30,\ntoken reset password" --> WA
    WA -- "Konfirmasi pengiriman" --> S
```

---

### E.2 — DFD Level 1: Dekomposisi Proses Utama

```mermaid
flowchart TD
    UU["👤 User Unit"]
    AG["👤 Admin Global"]
    IT["👤 IT Support"]
    WA["📱 WhatsApp"]

    P1["1.0\nManajemen\nAutentikasi"]
    P2["2.0\nManajemen\nLaporan"]
    P3["3.0\nValidasi\nLaporan"]
    P4["4.0\nManajemen\nHelpdesk"]
    P5["5.0\nSistem\nNotifikasi"]
    P6["6.0\nDashboard &\nVisualisasi"]
    P7["7.0\nManajemen\nToken"]

    DS1[("🗄 D1: User")]
    DS2[("🗄 D2: Report")]
    DS3[("🗄 D3: SupportRequest")]
    DS4[("🗄 D4: ResetToken")]
    DS5[("🗄 D5: AuditLog")]
    DS6[("🗄 D6: Unit & Target")]

    UU -- "email, password" --> P1
    AG -- "email, password" --> P1
    IT -- "email, password" --> P1
    P1 -- "JWT Token" --> UU
    P1 -- "JWT Token" --> AG
    P1 -- "JWT Token" --> IT
    P1 -- "baca/update user" --> DS1
    P1 -- "log aktivitas" --> DS5

    UU -- "data laporan" --> P2
    P2 -- "status laporan" --> UU
    P2 -- "baca/tulis laporan" --> DS2
    P2 -- "baca unit & target" --> DS6
    P2 -- "log aktivitas" --> DS5

    UU -- "request validasi & submit" --> P3
    AG -- "keputusan ACC/REVISI" --> P3
    P3 -- "update status laporan" --> DS2
    P3 -- "trigger notifikasi" --> P5
    P3 -- "log aktivitas" --> DS5

    UU -- "request helpdesk" --> P4
    IT -- "handle TOKEN/ISSUE" --> P4
    AG -- "handle REVISION" --> P4
    P4 -- "baca/tulis tiket" --> DS3
    P4 -- "trigger notifikasi" --> P5
    P4 -- "trigger generate token" --> P7

    P5 -- "kirim pesan" --> WA
    P5 -- "emit event realtime" --> UU
    P5 -- "emit event realtime" --> AG

    AG -- "request dashboard" --> P6
    UU -- "request dashboard" --> P6
    P6 -- "baca laporan" --> DS2
    P6 -- "baca unit & target" --> DS6
    P6 -- "data grafik & statistik" --> AG
    P6 -- "data grafik & statistik" --> UU

    IT -- "generate token" --> P7
    P7 -- "simpan token" --> DS4
    P7 -- "kirim token via WA" --> P5
    P7 -- "update password" --> DS1
```

---

## F. RINGKASAN STATUS DIAGRAM

| Diagram | Jumlah | Keterangan |
|---------|--------|-----------|
| Use Case | 1 | 3 aktor, 23 use case |
| Activity | 6 | Login, Reset PW, Input Laporan, Admin Review, Edit via Helpdesk, Helpdesk |
| Sequence | 5 | Login, Reset PW, Submit Laporan, Admin Review, Helpdesk REVISION |
| ERD | 1 | 12 tabel, relasi lengkap |
| DFD Level 0 | 1 | Context diagram |
| DFD Level 1 | 1 | 7 proses utama |

---

*Untuk membuka diagram: gunakan VS Code + extension "Markdown Preview Mermaid Support", atau copy-paste tiap blok ke https://mermaid.live*
