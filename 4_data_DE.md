# Strukturierung des `/data` Verzeichnisses

```
project-name/
├── data/
    ├── raw/          # Originale, unveränderte Daten
    ├── intermediate/ # Abgeleitete Daten, die nicht "final" sind
    ├── processed/    # Daten abgeleitet aus raw oder intermediate Daten
    └── models/       # Modellgewichte und Ausgaben (falls zutreffend)
```

## Richtlinien

- **`raw/`**:
  - Speichere alle originalen Daten genau so, wie sie gesammelt wurden.
  - **Verändere** diese Dateien **nicht**, um die Datenintegrität zu bewahren.
  - Füge Metadaten hinzu oder verwende klare Dateinamen mit Datumsangaben, um zu kennzeichnen, wann die Daten aufgezeichnet wurden.

Aus deinen raw Daten extrahieren wir normalerweise einige bedeutungsvolle Merkmale, die wir weiter analysieren wollen:

- **`intermediate/`**:
  - Platziere abgeleitete Daten hier. Diese zusätzliche Ebene ist möglicherweise nicht für alle Projekte nützlich.
  - Zum Beispiel könnten intermediate Daten die Positionstracks von Tieren sein, wenn deine raw Daten Videos sind, oder Spektrogramme, wenn deine raw Daten Audiodateien sind.

Nachdem du die extrahierten Daten analysiert hast, möchtest du Zusammenfassungsdiagramme erstellen. Da du nicht jedes Mal deine Analyse erneut ausführen möchtest, wenn du ein Diagramm zeichnen willst, ist es am besten, die Ergebnisse deiner Analysen in Dateien zu speichern, z.B. `.csv` Dateien. Ein Plotting-Skript kann dann direkt diese Dateien laden, die im `processed/` Verzeichnis enthalten sind.

- **`processed/`**:
  - Platziere bereinigte oder transformierte Daten hier.
  - Erzeuge diese Dateien mithilfe von Skripten.
  - Dokumentiere die Verarbeitungsschritte bei Bedarf.
  - Dies ist normalerweise die finale Version der Daten, die direkt für die Visualisierung verwendet werden.
  - Wenn du planst, deine Arbeit zu veröffentlichen, sind dies auch die Daten, die normalerweise zusammen mit deinem Manuskript und deinem Code veröffentlicht werden.

Wenn deine Analyse ein Modelltraining beinhaltet, speichern wir normalerweise die trainierten Modellgewichte, Checkpoints und Ausgaben im `models/` Verzeichnis.

- **`models/`** (wenn du Modelle trainierst):
  - Speichere Modellgewichte, Checkpoints und Ausgaben.
  - Organisiere nach Experiment oder Modellversion, wenn nötig.
  - Füge Metadaten über Trainingsparameter oder Ergebnisse bei.

Jetzt hast du eine gute Verzeichnisstruktur für dein Datenanalyseprojekt. Ein Blick in unseren Leitfaden über [remote computing](5_remote_computing_DE.md) ist ein guter nächster Schritt zum Weiterlernen.
