# 🌍 Leitfaden für Remote-Computing

Die Arbeit mit Remote-Maschinen ist ein zentraler Bestandteil des Workflows in unserem Labor. Dieser Leitfaden führt dich in die wesentlichen Tools für das Verbinden, Übertragen von Dateien, Einhängen von Remote-Laufwerken und effizientes Ausführen von Code ein. So kannst du dein Multi-Terabyte-Dataset auf einer performanten Maschine in unserem Labor von deinem Sofa zu Hause aus analysieren!

## 🔑 Verbinden mit Remote-Hosts mit SSH
Alle Laborrechner haben einen Standardbenutzer namens `efish`. Frage bitte jemanden im Labor nach dem Passwort. Um eine Verbindung zu einem Remote-Rechner herzustellen, benutze:

```sh
ssh efish@remote-host.am28.uni-tuebingen.de
```

Du bist jetzt in einer Terminalsitzung auf diesem Rechner und kannst alles machen, was du auch auf deinem lokalen Rechner tun kannst!

Alle Computer haben einen Hostnamen. Normalerweise befindet sich ein Aufkleber an der Vorderseite des Rechners mit dem Hostnamen. Zum Beispiel, wenn die Maschine `torpedo` heißt:

```sh
ssh efish@torpedo.am28.uni-tuebingen.de
```

### SSH-Schlüssel für passwortloses Anmelden
Um zu vermeiden, dein Passwort wiederholt einzugeben, richte einen SSH-Schlüssel ein:

```sh
ssh-keygen -t ed25519  # Erzeuge einen Schlüssel (Eingabetaste für Standardwerte)
ssh-copy-id efish@remote-host.am28.uni-tuebingen.de  # Kopiere deinen Schlüssel zur Remote-Maschine
```

Nun kannst du dich anmelden, ohne ein Passwort einzugeben.

## 📂 Dateien übertragen mit Rsync
Für effiziente Dateiübertragungen verwenden wir `rsync`, das Dateien zwischen lokalen und Remote-Systemen oder auch zwischen Verzeichnissen auf deinem lokalen Gerät synchronisiert.

Eine Datei **zu** einer Remote-Maschine kopieren:

```sh
rsync -av file.txt efish@remote-host:/pfad/zum/ziel/
```

Eine Datei **von** einer Remote-Maschine kopieren:

```sh
rsync -av efish@remote-host:/pfad/zur/datei.txt ./lokaler-ordner/
```

Um ganze Verzeichnisse zu kopieren und Berechtigungen zu erhalten:

```sh
rsync -av --progress quelle-ordner/ efish@remote-host:/ziel-ordner/
```

## 🔗 Remote-Laufwerke mit SSHFS einhängen
Große Datensätze werden normalerweise auf unserem Speicher-Server gespeichert. Da sich dieser Server in unserem Labor befindet, kannst du jedes Laufwerk oder Verzeichnis dieses Servers auf deiner eigenen Maschine im Labor remot einhängen. Da alle Geräte über Ethernet verbunden sind, kannst du auf diese Daten zugreifen, als wären sie auf einer Festplatte direkt mit deiner Maschine verbunden. Wenn du mit großen Datensätzen arbeitest, kannst du **Remote-Verzeichnisse lokal einhängen** mit SSHFS:

```sh
mkdir ~/remote-daten  # Erstelle einen Einhängepunkt
sshfs efish@remote-host:/pfad/zu/daten ~/remote-daten
```

Jetzt kannst du auf Remote-Dateien zugreifen, als wären sie lokal. Um auszuhängen:

```sh
fusermount -u ~/remote-daten
```

## 🧑‍💻 Code auf Remote-Maschinen ausführen
### Mit SSH-Tunneling in VS Code
VS Code bietet eingebaute Unterstützung für die Remote-Entwicklung über SSH. Um es zu nutzen:
1. Installiere die [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) Erweiterung.
2. Öffne die Befehlspalette (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf macOS).
3. Wähle **Remote-SSH: Connect to Host...** und gib `efish@remote-host.am28.uni-tuebingen.de` ein.

Auf diese Weise kannst du Code remote bearbeiten und ausführen mit voller VS Code-Unterstützung.

### Code manuell synchronisieren und ausführen
Wenn du es vorziehst, kannst du Code lokal bearbeiten und mit `rsync` synchronisieren, dann über SSH ausführen:

```sh
rsync -av mein_skript.py efish@remote-host:~/arbeitsbereich/
ssh efish@remote-host 'python3 ~/arbeitsbereich/mein_skript.py'
```

Für häufige Verwendung solltest du ein kleines Skript schreiben, um das Synchronisieren und Ausführen zu automatisieren.

## 📝 Effiziente Remote-Workflows mit Terminal-Tools
### Verwendung von Neovim zum Remote-Editieren
Wenn du Dateien nicht manuell synchronisieren möchtest, ziehe einen terminalbasierten Code-Editor wie `neovim` in Betracht, der es dir erlaubt, Code auf dem Remote-Host in deiner `ssh`-Sitzung zu bearbeiten. Für weitere Hilfe können **Patrick und Alex** im Labor beim Einrichten von Neovim unterstützen. Dieser Code-Editor hat eine steile Lernkurve, ist aber extrem leistungsfähig.

### Ausführen persistenter Sitzungen mit Tmux
Wenn du dich über ssh mit einem Remote-Host verbindest, ein Skript startest und die Verbindung trennst, bevor es beendet ist, wird deine Remote-Terminalsitzung geschlossen und das Skript wird gestoppt. `tmux` behebt dies, indem es dir erlaubt, eine Sitzung zu starten, Prozesse auszuführen und später erneut zu verbinden — auch wenn du die Verbindung verlierst.

Starte eine neue Sitzung auf einer Remote-Maschine:

```sh
tmux new -s meine_sitzung
```

Von einer Sitzung trennen (lässt sie laufen):

```sh
Strg + B, dann D drücken
```

Erneut mit einer laufenden Sitzung verbinden:

```sh
tmux attach -t meine_sitzung
```

Dies ist nützlich, wenn du lange Experimente oder Skripte remote ausführst.

## 🔗 Zusammenfassung
| Aufgabe                       | Empfohlenes Tool     |
|-------------------------------|----------------------|
| Verbindung zu Remote-Maschine | `ssh`                |
| Dateien effizient kopieren    | `rsync`              |
| Remote-Verzeichnisse mounten  | `sshfs`              |
| Dateien remote editieren      | `Neovim`, `VS Code SSH` |
| Persistente Prozesse ausführen| `tmux`               |

Jetzt da wir dich für Remote-Computing fit gemacht haben, solltest du unseren kurzen Leitfaden zum [Schreiben und Literaturrecherche](6_literature_DE.md) anschauen.
