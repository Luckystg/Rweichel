# SEQUENCE DIAGRAM — 1
# Login

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
