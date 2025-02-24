# 🖥️ Anleitung zur Einrichtung der Umgebung

Willkommen! Diese Anleitung hilft dir, deine Computerumgebung für die Arbeit im Labor einzurichten. Die meisten unserer Maschinen laufen mit einer Linux-Version namens [Ubuntu](https://ubuntu.com/), und wir verwenden Python mit [`pyenv`](https://github.com/pyenv/pyenv), um Versionen und virtuelle Umgebungen zu verwalten.

## Erste Schritte mit dem Linux-Terminal
Linux ist ein leistungsfähiges, kostenloses und open-source Betriebssystem, perfekt für Forschung und Datenanalyse. Hier einige Grundlagen:

- Öffne ein Terminal mit `Strg + Alt + T`
- Verzeichnisse navigieren: `cd <ordner>`
- Dateien auflisten: `ls`
- Einen Ordner erstellen: `mkdir <ordner>`
- Dateien verschieben: `mv <quelle> <ziel>`
- Dateien kopieren: `cp <quelle> <ziel>`
- Dateien entfernen: `rm <datei>` (vorsichtig verwenden! Dies löscht die Datei dauerhaft, es gibt kein Rückgängig. Zum Beispiel wird `rm -rf /` das gesamte Dateisystem löschen.)
- Dateien bearbeiten: Terminal-Editoren wie `nano <datei>` oder `vim <datei>` ermöglichen es dir, Dateien innerhalb des Terminals zu erstellen, zu bearbeiten und zu speichern.

Für mehr Informationen, schau dir [diese Linux-Kommandoanleitung](https://linuxcommand.org/) an.

## Software auf Ubuntu installieren
Die meiste Software kann mit `apt` installiert werden. Zum Beispiel:

```sh
sudo apt update && sudo apt upgrade -y  # Paketlisten aktualisieren
sudo apt install git python3 python3-venv -y  # Einige wichtige Werkzeuge installieren
```

Um Software zu entfernen:

```sh
sudo apt remove <paket-name>
```
Du möchtest wahrscheinlich deinen bevorzugten Code-Editor installieren (z.B. nvim, emacs, Visual Studio Code, PyCharm, etc.). In vielen Fällen könnte dieser bereits installiert sein.

## Verwendung von Python mit `pyenv`
Wir verwenden `pyenv`, um verschiedene Python-Versionen zu verwalten. Um es zu installieren, benötigen wir zuerst die notwendigen Build-Essentials für Python:

```sh
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Danach können wir den `pyenv` Auto-Installer herunterladen und ausführen.

```sh
curl https://pyenv.run | bash
```

Nach Abschluss schlägt der Installer vor, einige Dinge in die Konfigurationsdatei deiner Shell einzutragen. Um dies automatisch zu tun, führe einfach diese Zeilen im Terminal aus:

```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
```

Starte dann deine Shell neu und führe aus:

```sh
pyenv install 3.12  # Installiere Python 3.12
pyenv global 3.12  # Setze es als Standard
```

Um die installierten Versionen zu überprüfen:

```sh
pyenv versions
```

## Virtuelle Umgebungen: Warum und wie du sie benutzt
Virtuelle Umgebungen isolieren Abhängigkeiten für verschiedene Projekte und verhindern Konflikte. Sie funktionieren wie eine Sandbox für deinen Code und erleichtern das Management von Abhängigkeiten, was die Reproduzierbarkeit verbessert.

### Erstellen einer virtuellen Umgebung

```sh
python -m venv venv  # Erstelle eine neue virtuelle Umgebung
source venv/bin/activate  # Aktiviere sie (Linux/macOS)
```

Jetzt sollte dein Prompt `(venv)` anzeigen, was bedeutet, dass sie aktiv ist. Um sie zu deaktivieren:

```sh
deactivate
```

### Verwenden von `pyenv` mit virtuellen Umgebungen
Anstatt des standardmäßigen `venv` kannst du `pyenv-virtualenv` für mehr Flexibilität verwenden:

```sh
pyenv virtualenv 3.12 myenv  # Erstelle eine virtuelle Umgebung namens `myenv`
pyenv activate myenv  # Aktiviere sie
pyenv local myenv  # Automatische Aktivierung im aktuellen Verzeichnis
```

Diese Methode ermöglicht es dir, dieselbe virtuelle Umgebung über mehrere Projekte hinweg zu verwenden.

## Nächste Schritte
Glückwunsch! Nun, da du eine **bequeme** Computerumgebung eingerichtet hast, schau dir folgendes an:

- [Allgemeine Arbeitsabläufe Anleitung](0_workflow_and_help_DE.md)
- [Strukturierung eines Datenanalyse-Projekts](3_data_analysis_project_DE.md)
