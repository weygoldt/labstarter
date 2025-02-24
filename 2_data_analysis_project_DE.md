# Leitfaden zur Datenanalyse-Struktur

**Deutsche Version**: [README_DE.md](README_de_DE.md)

Willkommen zu unserem Leitfaden für Projektstrukturen! Dieser Leitfaden soll
neuen Studierenden helfen, zu verstehen, wie man Datenanalyseprojekte in Python
effektiv strukturiert. Indem du diese Best Practices befolgst, erstellst du Projekte, die
organisiert, wartbar und reproduzierbar sind.

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

Eine gut organisierte Projektstruktur ist entscheidend für die Kollaboration und
Skalierbarkeit. Hier ist eine empfohlene Verzeichnisstruktur:

```
projektname/
├── data/
│   ├── model_weights/          # Gewichte des trainierten Modells
│   ├── raw/                    # Original, unveränderte Datensätze
│   └── processed/              # Bereinigte oder transformierte Daten
├── code/
│   └── my_python_program.py    # Python-Skripte
├── figures/
├── docs/
│   ├── my_fancy_latex_thesis/  # LaTeX-Dateien für die Abschlussarbeit (empfohlen)
│   ├── my_presentation.pptx    # Präsentationsfolien
│   └── my_thesis.docx          # Word-Dokument (nicht empfohlen)
├── .gitignore                  # Dateien und Verzeichnisse, die Git ignorieren soll
├── README.md                   # Projektübersicht und Anweisungen
└── requirements.txt            # Python-Abhängigkeiten
```

### Trennung von Daten und Code

- **Datenverzeichnis (`data/`)**: Hier solltest du alle deine Datensätze speichern.
  - `raw/`: Original, unveränderte Datensätze.
  - `processed/`: Bereinigte oder transformierte Daten.
- **Quellcode-Verzeichnis (`code/`)**: Beinhaltet alle Code-Skripte und Module.

**Vorteile:**

- **Organisation**: Hält deine Daten getrennt vom Code, was die Verwaltung erleichtert.
- **Reproduzierbarkeit**: Eine klare Trennung sorgt dafür, dass Datenverarbeitungsschritte dokumentiert und wiederholbar sind.
- **Kollaboration**: Du und deine Mitstreiter könnt leicht die verschiedenen Komponenten des Projekts finden und verstehen.

### Trennung von Abbildungen und Code

- **Abbildungsverzeichnis (`figures/`)**: Speichere alle generierten Plots, Bilder und Visualisierungen hier.

**Vorteile:**

- **Klarheit**: Trennt Ausgaben vom Code und reduziert Unordnung.
- **Versionskontrolle**: Änderungen im Code sind einfacher nachzuverfolgen, ohne große Binärdateien wie Bilder.
- **Präsentation**: Vereinfacht das Erstellen von Berichten oder Präsentationen, da alle Abbildungen an einem Ort sind.

---

## Versionskontrolle mit Git

Git ist ein mächtiges Versionskontrollsystem, das dir hilft, Änderungen
nachzuverfolgen, mit anderen zusammenzuarbeiten und die Geschichte deines Projekts zu verwalten. Aber was ist Versionskontrolle? Hast du dich schon einmal dabei ertappt, Dateien wie `projekt_final_v2.py` oder `projekt_final_final.py` zu erstellen? Versionskontrolle löst dieses Problem, indem sie Änderungen nachverfolgt und dir ermöglicht, zu vorherigen Versionen zurückzukehren. Als Bonus hast du auch ein Backup deines Projekts, falls etwas schiefgeht. Es gibt keinen guten Grund, es nicht zu benutzen!

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

- **Status überprüfen**

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

- **Auf Remote-Repository pushen**

  ```bash
  git push origin main
  ```

- **Vom Remote-Repository pullen**

  ```bash
  git pull origin main
  ```

  #### Fortgeschrittene Git-Befehle

- **Einen neuen Branch erstellen**

  ```bash
  git branch <branchname>
  ```

- **Zwischen Branches wechseln**

  ```bash
  git checkout <branchname>
  ```

- **Branches zusammenführen**

  ```bash
  git merge <branchname>
  ```

- **Commit-Historie ansehen**

  ```bash
  git log
  ```

**Tipps:**

- **Oft committen**: Regelmäßige Commits erleichtern das Nachverfolgen von Änderungen.
- **Aussagekräftige Nachrichten**: Verwende beschreibende Commit-Nachrichten für ein besseres Verständnis.
- **Nutze `.gitignore`**: Schließe Dateien und Verzeichnisse aus, die nicht verfolgt werden sollen (z.B. große Datendateien, virtuelle Umgebungen).

Wenn du (und vielleicht andere neue Studierende) noch nie von Git gehört oder benutzt hast und eine formelle Einführung bevorzugst, sprich deinen Betreuer oder Mitstudierende an, um einen Workshop zur Einführung in Git zu organisieren.

---

## Best Practices für Datenanalyseprojekte

1. **Verwende virtuelle Umgebungen**

   - Nutze `venv`, `conda` oder `pyenv`, um projektspezifische Abhängigkeiten zu verwalten.
   - Dokumentiere Abhängigkeiten in `requirements.txt` oder nutze `poetry` für das Paketmanagement.

2. **Dokumentiere deine Arbeit**

   - Halte eine klare und informative `README.md` aufrecht.
   - Verwende Docstrings und Kommentare in deinem Code.
   - Führe ein Änderungsprotokoll für wichtige Aktualisierungen. Das ist nützlich, aber auch sehr befriedigend, da es dir zeigt, was du erreicht hast!

3. **Schreibe modularen Code**

   - Teile den Code in Funktionen und Klassen.
   - Wiederverwende Code, um Duplikate zu vermeiden.

4. **Folge Coding-Standards**

   - Halte dich an die PEP 8-Richtlinien für Python-Code.
   - Verwende Linter wie `flake8` oder Formatter wie `black` oder `ruff`, um die Codequalität zu sichern. Diese können als Terminalbefehle genutzt oder in deinen Code-Editor integriert werden, um deinen Code automatisch mit Best Practices zu formatieren.

5. **Automatisiere Datenverarbeitung**

   - Schreibe Skripte, um Datenbereinigung und -vorverarbeitung zu automatisieren.
   - Stelle sicher, dass Skripte von Anfang bis Ende ausführbar sind, um Ergebnisse zu reproduzieren.

6. **Teste deinen Code**

   - Wenn du ein Python-Paket schreibst, führe Unit-Tests mit Frameworks wie `unittest` oder `pytest` durch.
   - Halte Tests im `tests/`-Verzeichnis.

7. **Geh mit Daten sorgfältig um**

   - Commite keine Daten zur Versionskontrolle.

8. **Versioniere deine Daten und Modelle**

   - Speichere Modellversionen mit Zeitstempeln oder eindeutigen Bezeichnern.

9. **Backup regelmäßig**

   - Pushe Änderungen häufig auf ein Remote-Repository.
   - Erstelle zusätzliche Backups für wichtige Daten! Sprich deinen Betreuer an, wenn du Speicherplatz oder Hilfe beim Backup benötigst.

10. **Kollaborier effektiv**

    - Verwende Branches für neue Funktionen oder Experimente.
    - Führe Änderungen mit Pull-Requests und Code-Reviews zusammen.

---

## Zusätzliche Ressourcen

- **Git-Dokumentation**: [git-scm.com/docs](https://git-scm.com/docs)
- **PEP 8 Style Guide**: [python.org/dev/peps/pep-0008](https://www.python.org/dev/peps/pep-0008/)
- **Python Virtuelle Umgebungen**:
  - [`venv` Modul](https://docs.python.org/3/library/venv.html)
  - [Anaconda Distribution](https://www.anaconda.com/products/distribution)
  - [`pyenv` Virtuelle Umgebungen](https://github.com/pyenv/pyenv)

---

## Fazit

Eine effektive Strukturierung deiner Datenanalyseprojekte ist der erste Schritt
zu einer erfolgreichen und reproduzierbaren Forschung. Indem du Daten, Code und Abbildungen trennst, Versionskontrolle nutzt und Best Practices befolgst, legst du ein starkes Fundament für deine Arbeit und die Zusammenarbeit mit anderen.

Viel Spaß beim Programmieren!

Vielleicht interessierst du dich weiterhin für unseren Leitfaden zu [gutem Code](3_code_DE.md).
