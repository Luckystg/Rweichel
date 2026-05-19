# USE CASE DIAGRAM — ADMIN GLOBAL
# Sistem Monitoring & Pelaporan PT KAI Divre I Sumut

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000', 'secondaryColor': '#ffffff', 'tertiaryColor': '#ffffff', 'clusterBkg': '#ffffff', 'clusterBorder': '#000000', 'titleColor': '#000000', 'edgeLabelBackground': '#ffffff', 'background': '#ffffff'}}}%%
flowchart LR
    subgraph SISTEM["SISTEM KAI"]
        direction TB
        subgraph Auth["Autentikasi"]
            UC1["Login"]
        end
        subgraph Lap["Manajemen Laporan"]
            UC9["Export Laporan PDF / Excel"]
        end
        subgraph Rev["Review & Monitoring"]
            UC10["Review Laporan"]
            UC11["ACC Laporan"]
            UC12["Set Status REVISI"]
            UC13["Monitor Semua Unit"]
            UC14["Kelola Akun User"]
            UC15["Kelola Unit"]
            UC16["Lihat Dashboard & Grafik"]
        end
        subgraph Help["Helpdesk"]
            UC22["Handle Helpdesk REVISION"]
        end
    end

    AG@{ shape: person, label: "Admin Global" }

    UC1 & UC9 & UC10 & UC11 & UC12 & UC13 & UC14 & UC15 & UC16 & UC22 --- AG

    UC11 -. "«include»" .-> UC10
    UC12 -. "«include»" .-> UC10
    UC22 -. "«extend»" .-> UC12
```
