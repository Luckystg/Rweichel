# USE CASE DIAGRAM — USER UNIT
# Sistem Monitoring & Pelaporan PT KAI Divre I Sumut

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000', 'secondaryColor': '#ffffff', 'tertiaryColor': '#ffffff', 'clusterBkg': '#ffffff', 'clusterBorder': '#000000', 'titleColor': '#000000', 'edgeLabelBackground': '#ffffff', 'background': '#ffffff'}}}%%
flowchart LR
    UU@{ shape: person, label: "User Unit" }

    subgraph SISTEM["SISTEM KAI"]
        direction TB
        subgraph Auth["Autentikasi"]
            UC1["Login"]
            UC2["Reset Password via Token"]
        end
        subgraph Lap["Manajemen Laporan"]
            UC3["Input Laporan Harian"]
            UC4["Tambah Komoditi Barang"]
            UC5["Input Target / RKAP"]
            UC6["Validasi Internal Laporan"]
            UC7["Submit Laporan"]
            UC8["Lihat Status Laporan"]
            UC9["Export Laporan PDF / Excel"]
        end
        subgraph Help["Helpdesk"]
            UC17["Ajukan Helpdesk TOKEN"]
            UC18["Ajukan Helpdesk ISSUE"]
            UC19["Ajukan Helpdesk REVISION"]
        end
    end

    UU --- UC1 & UC2
    UU --- UC3 & UC4 & UC5 & UC6 & UC7 & UC8 & UC9
    UU --- UC17 & UC18 & UC19

    UC7 -. "«include»" .-> UC6
    UC4 -. "«extend»" .-> UC3
    UC2 -. "«include»" .-> UC17
    UC8 -. "«extend»" .-> UC7
```
