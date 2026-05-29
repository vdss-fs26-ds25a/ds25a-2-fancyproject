# VDSS Team 2: Marktwerte & Ligadaten von Transfermarkt.de
# Das grosse Geld im Europäischen Fussball

[![Dashboard](https://img.shields.io/badge/Status-Live_Dashboard-brightgreen?style=for-the-badge&logo=quarto)](https://vdss-fs26-ds25a.github.io/ds25a-2-fancyproject)

## Projektbeschreibung
Dieses Projekt umfasst Visualisierungen und Analysen von Marktwerten, Transfersummen und weiteren Geldgeschäften im europäischen Spitzenfussball für den Zeitraum 2010–2025. 

Das Dashboard bietet Einblicke in Marktwerttrends, Transferausgaben und Vergleiche in den Top-5 Ligen des europäischen Fussballverbands UEFA und dient als Analysewerkzeug für Sportdaten-Interessierte, Fussballfans und Soccer-Analytics-Spezialisten.

## Daten & Methodik
* **Datenakquise:** Wir nutzen einen automatisierten Scraper, um aktuelle und historische Marktwert- und Transferdaten direkt aus Transfermarkt.de zu beziehen.
* **Visualisierung:** Die aufbereiteten Datensätze werden mit Python (`pandas`, `plotly`) innerhalb des Quarto-Frameworks zu interaktiven Visualisierungen verarbeitet.
* **Deployment:** Das Dashboard wird via GitHub Actions auf GitHub Pages bereitgestellt.

## Anerkennung
Ein besonderer Dank gilt **[dcaribou](https://github.com/dcaribou)**. Die Modifikation und Integration seines Transfermarkt-Scrapers war die Grundlage für die Realisierung der Daten-Pipeline dieses Projekts.

## Dashboard lokal erstellen:

### Voraussetzungen
Stelle sicher, dass [uv](https://github.com/astral-sh/uv) auf deinem System installiert ist.

### Installation
1. Repository klonen und in den Ordner 'docs' gehen.
2. Abhängigkeiten installieren:
   ```bash
   uv sync
   ```

### Rendering
Um das Dashboard lokal zu bauen und zu testen, führe den Render-Befehl im Ordner 'docs' aus:

```bash
uv run quarto render docs
```

Die generierte Webseite befindet sich anschließend im Verzeichnis `docs/build/`.

## Lizenz
Weitere Informationen finden sich in der `LICENSE`-Datei.

## Projektstruktur
Das Repository ist strukturiert, um Dashboard-Logik, Daten und explorative Analysen sauber zu trennen:

```text
.
├── docs/                 # Hauptverzeichnis für das Quarto-Dashboard
│   ├── assets/           # Visualisierungen & Grafiken
│   ├── data/             # Roh- und verarbeitete Datensätze (JSONL/CSV)
│   ├── logos/            # Ligalogos
│   ├── backlog.qmd       # Methodik und Projekt-Backlog
│   ├── report.qmd        # Hauptdashboard (Einstiegspunkt)
│   ├── _quarto.yml       # Quarto-Konfiguration
│   └── ...
├── eda/                  # Explorative Datenanalyse-Skripte
├── template-backup/      # Archivierte Vorlagen
├── pyproject.toml        # Projekt-Abhängigkeiten 
├── uv.lock               # Dependency Lockfile
└── README.md
```
