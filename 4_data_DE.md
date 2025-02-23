# Strukturierung des `/data`-Verzeichnisses

```
project-name/
├── data/
    ├── raw/          # Originale, unveränderte Daten
    ├── processed/    # Aus Rohdaten abgeleitete Daten
    └── models/       # Modellgewichte und Ausgaben (optional)
```

## Richtlinien

- **`raw/`**:
  - Speichere alle originalen Daten genau so, wie sie gesammelt wurden.
  - **Verändere diese Dateien nicht**, um die Datenintegrität zu bewahren.
  - Füge Metadaten hinzu oder verwende klare Dateinamen mit Datumsangaben, um anzugeben, wann die Daten aufgezeichnet wurden.

- **`processed/`**:
  - Lege hier bereinigte oder transformierte Daten ab.
  - Erstelle diese Dateien mithilfe von Skripten.
  - Dokumentiere bei Bedarf die Verarbeitungsschritte.

- **`models/`** (falls du machine learning verwendest):
  - Speichere Modellgewichte, Checkpoints und Ausgaben.
  - Organisiere nach Experiment oder Modellversion, falls erforderlich.
  - Füge Metadaten über Trainingsparameter oder Ergebnisse hinzu.
