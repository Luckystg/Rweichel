# USE CASE DIAGRAM — IT SUPPORT
# Sistem Monitoring & Pelaporan PT KAI Divre I Sumut

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000', 'secondaryColor': '#ffffff', 'tertiaryColor': '#ffffff', 'clusterBkg': '#ffffff', 'clusterBorder': '#000000', 'titleColor': '#000000', 'edgeLabelBackground': '#ffffff', 'background': '#ffffff'}}}%%
flowchart LR
    subgraph SISTEM["SISTEM KAI"]
        direction TB
        subgraph Auth["Autentikasi"]
            UC1["Login"]
        end
        subgraph Rev["Monitoring"]
            UC13["Monitor Semua Unit"]
        end
        subgraph Help["Helpdesk"]
            UC20["Handle Helpdesk TOKEN"]
            UC21["Handle Helpdesk ISSUE"]
            UC23["Generate Token Reset Password"]
        end
    end

    IT@{ shape: person, label: "IT Support" }

    UC1 & UC13 & UC20 & UC21 & UC23 --- IT

    UC20 -. "«include»" .-> UC23
```
