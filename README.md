# Das grosse Geld im Europäischen Fussball

[![Action](https://img.shields.io/badge/zum_Dashboard-blue?style=for-the-badge&logo=quarto)](https://vdss-fs26-ds25a.github.io/ds25a-2-fancyproject) [![Quarto](https://img.shields.io/badge/Quarto-000000?style=flat&logo=quarto&logoColor=white)](https://quarto.org)
[![uv](https://img.shields.io/badge/uv-deed00?style=flat&logo=uv&logoColor=black)](https://astral.sh/uv)

## Projektbeschreibung
Dieses Projekt umfasst Visualisierungen und Analysen von Marktwerten, Transfersummen und weiteren Geldgeschäften im europäischen Spitzenfussball für den Zeitraum 2010–2025. 

Das Dashboard bietet Einblicke in Marktwerttrends, Transferausgaben und Vergleiche in den Top-5 Ligen des europäischen Fussballverbands UEFA und dient als Analysewerkzeug für Sportdaten-Interessierte, Fussballfans und Soccer-Analytics-Spezialisten.

## Daten & Methodik
* **Datenakquise:** Wir nutzen einen automatisierten Scraper, um aktuelle und historische Marktwert- und Transferdaten direkt aus Transfermarkt.de zu beziehen.
* **Visualisierung:** Die aufbereiteten Datensätze werden mit Python (`pandas`, `plotly`) innerhalb des Quarto-Frameworks zu interaktiven Visualisierungen verarbeitet.
* **Deployment:** Das Dashboard wird via GitHub Actions auf GitHub Pages bereitgestellt.

## Scraper
Für die Vervollständigung der Datensätze und die Zusammenstellung von Saisons-Datensätzen mit einem Eintrag pro Club und pro Jahr wurde der
Scraper von **[dcaribou](https://github.com/dcaribou)** über eine Github-Codespace geladen und leicht verändert ausgeführt.

## Dashboard lokal erstellen:

### Voraussetzungen
Stelle sicher, dass [uv](https://github.com/astral-sh/uv) auf deinem System installiert ist.

### Installation
1. Repository klonen und Ordner 'docs' öffnen
2. Abhängigkeiten installieren und Render (Befehle in Terminal/Powershell ausführen):
   ```bash
   uv sync
   ```
   ```bash
   uv run quarto render
   ```

Die Webpage  im .html-Format befindet sich danach im Ordner `docs/build/`.

## Quellen
Siehe Datei /resources/sources.md

## Lizenz
Weitere Informationen finden sich in der `LICENSE`-Datei.

## Ordnerstruktur

```text
.
├── docs/                   # Verzeichnis für Quarto-Skripte und alle Logic elements des Dashboards
│   ├── assets/             # Grafiken, Design-elemente
│   ├── data/               # Datensätze
│   ├── logos/              # Logos
│   ├── data_report.qmd     # Skript Datenbericht
│   ├── index.qmd           # Skript Hauptseite Dashboard
│   ├── project_charta.qmd  # Skript Projektcharta
│   ├── styles.css          # Stylesheet 
│   └── (...)
├── resources/               # Berichte, Präsentationen, PDFs, andere Abgaben ausserhalb von Quarto
├── template-backup/         # Back-up der Vorlagenskripts
├── LICENSE                  # Lizenz
├── README.md                # Anleitung
└── (...)
```
