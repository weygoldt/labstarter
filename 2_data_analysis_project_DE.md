# Leitfaden zur Datenanalyse-Struktur

Willkommen zu diesem Leitfaden zur Projektstruktur! Dieser Leitfaden soll dir helfen zu verstehen, wie du Datenanalyseprojekte in Python effektiv strukturierst.

## Inhaltsverzeichnis

1. [Projektstruktur](#projektstruktur)
   - [Trennung von Daten und Code](#trennung-von-daten-und-code)
   - [Trennung von Abbildungen und Code](#trennung-von-abbildungen-und-code)
2. [Versionskontrolle mit Git](#versionskontrolle-mit-git)
   - [Grundlegende Git-Befehle](#grundlegende-git-befehle)
3. [Best Practices für Datenanalyseprojekte](#best-practices-für-datenanalyseprojekte)
4. [Zusätzliche Ressourcen](#zusätzliche-ressourcen)
5. [Fazit](#fazit)

---

## Projektstruktur

Eine gut organisierte Projektstruktur ist entscheidend für Zusammenarbeit und Skalierbarkeit. Hier ist ein empfohlenes Verzeichnislayout:

```
project-name/
├── data/
│   ├── model_weights/          # Trainierte Modellgewichte
│   ├── raw/                    # Originale, unveränderte Datensätze
│   └── processed/              # Bereinigte oder transformierte Daten
├── code/
│   └── my_python_program.py    # Python-Skripte
├── figures/
├── docs/
│   ├── my_fancy_latex_thesis/  # LaTeX-Dateien für die Abschlussarbeit (empfohlen)
│   ├── my_presentation.pptx    # Präsentationsfolien
│   └── my_thesis.docx          # Word-Dokument (nicht empfohlen)
├── .gitignore                  # Dateien und Verzeichnisse, die von Git ignoriert werden sollen
├── README.md                   # Projektübersicht und Anleitungen
└── requirements.txt            # Python-Abhängigkeiten
```

### Trennung von Daten und Code

- **Datenverzeichnis (`data/`)**: Speichere hier alle deine Datensätze.
  - `raw/`: Originale, unveränderte Datensätze.
  - `processed/`: Daten, die bereinigt oder transformiert wurden.
- **Quellcode-Verzeichnis (`code/`)**: Enthält alle Codeskripte und Module.

**Vorteile:**

- **Organisation**: Hält Daten getrennt vom Code, was die Verwaltung erleichtert.
- **Reproduzierbarkeit**: Klare Trennung stellt sicher, dass Datenverarbeitungsschritte dokumentiert und wiederholbar sind.
- **Zusammenarbeit**: Du und deine Kollaborateure können leicht verschiedene Komponenten des Projekts finden und verstehen.

### Trennung von Abbildungen und Code

- **Abbildungsverzeichnis (`figures/`)**: Speichere hier alle generierten Plots, Bilder und Visualisierungen.

**Vorteile:**

- **Klarheit**: Trennt Ausgaben vom Code und reduziert Unordnung.
- **Versionskontrolle**: Einfachere Nachverfolgung von Änderungen im Code ohne große Binärdateien wie Bilder.
- **Präsentation**: Vereinfacht das Erstellen von Berichten oder Präsentationen, indem alle Abbildungen an einem Ort gesammelt sind.

---

## Versionskontrolle mit Git

Git ist ein leistungsstarkes Versionskontrollsystem, das dir hilft, Änderungen zu verfolgen, mit anderen zusammenzuarbeiten und die Historie deines Projekts zu verwalten. Aber was ist Versionskontrolle? Hast du jemals Dateien wie `project_final_v2.py` oder `project_final_final.py` erstellt? Versionskontrolle löst dieses Problem, indem sie Änderungen verfolgt und dir ermöglicht, zu früheren Versionen zurückzukehren. Als Bonus hast du auch ein Backup deines Projekts, falls etwas schiefgeht.

### Grundlegende Git-Befehle

- **Ein Repository initialisieren**

  ```bash
  git init
  ```

- **Remote-Repository hinzufügen (GitHub, Gittea)**

  ```bash
  git remote add origin <repository-url>
  ```

- **Ein Repository klonen**

  ```bash
  git clone <repository-url>
  ```

- **Status prüfen**

  ```bash
  git status
  ```

- **Änderungen hinzufügen**

  ```bash
  git add <dateiname>
  # Oder alle Änderungen hinzufügen
  git add .
  ```

- **Änderungen committen**

  ```bash
  git commit -m "Commit-Nachricht"
  ```

- **Zum Remote-Repository pushen**

  ```bash
  git push origin main
  ```

- **Vom Remote-Repository pullen**

  ```bash
  git pull origin main
  ```

#### Erweiterte Git-Befehle

- **Einen neuen Branch erstellen**

  ```bash
  git branch <branch-name>
  ```

- **Zwischen Branches wechseln**

  ```bash
  git checkout <branch-name>
  ```

- **Branches zusammenführen**

  ```bash
  git merge <branch-name>
  ```

- **Commit-Historie anzeigen**

  ```bash
  git log
  ```

**Tipps:**

- **Oft committen**: Regelmäßige Commits erleichtern das Nachverfolgen von Änderungen.
- **Aussagekräftige Nachrichten**: Verwende beschreibende Commit-Nachrichten für besseres Verständnis.
- **Verwende `.gitignore`**: Schließe Dateien und Verzeichnisse aus, die nicht verfolgt werden sollten (z. B. große Datendateien, virtuelle Umgebungen).

---

## Best Practices für Datenanalyseprojekte

1. **Verwende virtuelle Umgebungen**

   - Nutze `venv`, `conda` oder `pyenv`, um projektspezifische Abhängigkeiten zu verwalten.
   - Dokumentiere Abhängigkeiten in `requirements.txt` oder verwende `poetry` für das Paketmanagement.

2. **Dokumentiere deine Arbeit**

   - Pflege eine klare und informative `README.md`.
   - Verwende Docstrings und Kommentare in deinem Code.
   - Führe ein Changelog für bedeutende Updates.

3. **Schreibe modularen Code**

   - Unterteile Code in Funktionen und Klassen.
   - Nutze Code wieder, um Duplikate zu vermeiden.

4. **Befolge Codierungsstandards**

   - Halte dich an die PEP 8-Richtlinien für Python-Code.
   - Verwende Linter wie `flake8` oder Formatter wie `black` oder `ruff`, um die Codequalität zu gewährleisten.

5. **Automatisiere die Datenverarbeitung**

   - Schreibe Skripte, um die Datenbereinigung und -vorverarbeitung zu automatisieren.
   - Stelle sicher, dass Skripte von Anfang bis Ende ausgeführt werden können, um Ergebnisse zu reproduzieren.

6. **Teste deinen Code**

   - Implementiere Unit-Tests mit Frameworks wie `unittest` oder `pytest`.
   - Halte Tests im Verzeichnis `tests/`.

7. **Gehe sorgfältig mit Daten um**

   - Committe keine Daten in die Versionskontrolle.

8. **Versioniere Daten und Modelle**

   - Speichere Modellversionen mit Zeitstempeln oder eindeutigen Kennungen.

9. **Sichere regelmäßig**

   - Pushe Änderungen häufig in ein Remote-Repository.
   - Erwäge zusätzliche Backups für kritische Daten.

10. **Arbeite effektiv zusammen**

    - Verwende Branches für neue Funktionen oder Experimente.
    - Führe Änderungen mit Pull Requests und Code Reviews zusammen.

---

## Zusätzliche Ressourcen

- **Git-Dokumentation**: [git-scm.com/docs](https://git-scm.com/docs)
- **PEP 8 Style Guide**: [python.org/dev/peps/pep-0008](https://www.python.org/dev/peps/pep-0008/)
- **Python Virtual Environments**:
  - [`venv` Modul](https://docs.python.org/3/library/venv.html)
  - [Anaconda Distribution](https://www.anaconda.com/products/distribution)
  - [`pyenv` Virtuelle Umgebungen](https://github.com/pyenv/pyenv)

---

## Fazit

Die effektive Strukturierung deiner Datenanalyseprojekte ist der erste Schritt zu erfolgreicher und reproduzierbarer Forschung. Indem du Daten, Code und Abbildungen trennst, Versionskontrolle verwendest und bewährte Methoden befolgst, legst du ein starkes Fundament für deine Arbeit und die Zusammenarbeit mit anderen.

Viel Spaß beim Programmieren!
