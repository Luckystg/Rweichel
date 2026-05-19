# SEQUENCE DIAGRAM — 4
# Admin Review Laporan (ACC / REVISI)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'actorBkg': '#ffffff', 'actorBorder': '#000000', 'actorTextColor': '#000000', 'actorLineColor': '#000000', 'signalColor': '#000000', 'signalTextColor': '#000000', 'labelBoxBkgColor': '#ffffff', 'labelBoxBorderColor': '#000000', 'labelTextColor': '#000000', 'loopTextColor': '#000000', 'noteBkgColor': '#ffffff', 'noteBorderColor': '#000000', 'noteTextColor': '#000000', 'activationBkgColor': '#f0f0f0', 'activationBorderColor': '#000000'}}}%%
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
