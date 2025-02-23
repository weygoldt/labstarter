# Ein Leitfaden zum Schreiben eines guten Python-Skripts

Dieser Leitfaden hilft dir dabei, effektive und saubere Python-Skripte zu schreiben. Egal, ob du an einer Datenverarbeitungspipeline, einem Machine-Learning-Modell oder einem einfachen Hilfsskript arbeitest – wenn du diese Richtlinien befolgst, erstellst du lesbaren code, der leicht zu warten und zu erweitern ist.

## 1. Verwende einen aussagekräftigen und deklarativen Skriptnamen

Wähle einen Skriptnamen, der klar beschreibt, was das Skript tut. So ist es für andere (und dich selbst) einfacher zu verstehen, was das Skript macht, ohne den Code lesen zu müssen.

**Beispiele:**

- `datenbereinigung.py` statt `skript1.py`
- `bericht_generieren.py` statt `run.py`

## 2. Beginne mit einer kurzen Erklärung (Docstring)

Füge am Anfang deines Skripts einen Docstring ein, der kurz erklärt, was das Skript macht. Das hilft Nutzern, die Funktionalität des Skripts schnell zu erfassen.

```python
"""
Dieses Skript lädt Rohdaten, bereinigt sie durch Entfernen von Nullwerten und Duplikaten und speichert die verarbeiteten Daten in einer neuen Datei.
"""
```

## 3. Importiere alle benötigten Pakete am Anfang

Liste alle deine Importe am Anfang des Skripts auf. Das macht Abhängigkeiten klar und vereinfacht die Wartung.

```python
import sys                # Pakete, die von Python bereitgestellt werden
from pathlib import Path
import numpy as np        # Pakete, die heruntergeladen und in requirements.txt angegeben sind
import pandas as pd
import mein_modul         # Module, die du selbst geschrieben hast
```

## 4. Organisiere Code in Funktionen und Klassen

Organisiere deinen Code, indem du Funktionalitäten in Funktionen oder Klassen einbettest. Das fördert Code-Wiederverwendung, Testbarkeit und Lesbarkeit. Idealerweise sollten Funktionen eine Aufgabe erledigen und diese gut machen. Klassen können für komplexere Logik oder wenn du einen Zustand beibehalten musst, verwendet werden. Saubere Funktionen und Klassen enthalten _Type-Hints_ und _Docstrings_, um ihren Zweck sowie Eingaben/Ausgaben zu erklären.

**Beispiele für Funktionen:**

```python
def lade_daten(dateipfad: str) -> pd.DataFrame:
    """Lädt Daten aus einer CSV-Datei.

    Parameters:
    ----------
    dateipfad : str
        Pfad zur CSV-Datei.

    Returns:
    -------
    pd.DataFrame
        Geladene Daten als DataFrame.
    """
    return pd.read_csv(dateipfad)

def bereinige_daten(df: pd.DataFrame) -> pd.DataFrame:
    """Bereinigt den DataFrame durch Entfernen von Nullwerten und Duplikaten.

    Parameters:
    ----------
    df : pd.DataFrame
        Eingabe-DataFrame.
              
    Returns:
    -------
    pd.DataFrame
        Bereinigter DataFrame.
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def speichere_daten(df: pd.DataFrame, ausgabepfad: str) -> None:
    """Speichert den DataFrame in einer CSV-Datei.

    Parameters:
    ----------
    df : pd.DataFrame
        Zu speichernder DataFrame.
    ausgabepfad : str
        Pfad zum Speichern der CSV-Datei.
    """
    df.to_csv(ausgabepfad, index=False)
```

**Beispiel für eine Klasse:**

```python
class DatenVerarbeiter:
    """Eine Klasse zur Datenverarbeitung."""

    def __init__(self, dateipfad):
        self.daten = self.lade_daten(dateipfad)

    def lade_daten(self, dateipfad):
        return pd.read_csv(dateipfad)

    def bereinige_daten(self):
        self.daten.dropna(inplace=True)
        self.daten.drop_duplicates(inplace=True)

    def speichere_daten(self, ausgabepfad):
        self.daten.to_csv(ausgabepfad, index=False)
```

## 5. Definiere eine `main()`-Funktion

Erstelle eine `main()`-Funktion, die als Einstiegspunkt deines Skripts dient. Diese Funktion sollte den Ablauf deines Programms orchestrieren.

```python
def main():
    """Hauptfunktion, die die Datenverarbeitung steuert."""
    eingabedatei = 'data/raw/data.csv'
    ausgabedatei = 'data/processed/bereinigte_daten.csv'

    # Verwendung von Funktionen
    daten = lade_daten(eingabedatei)
    bereinigte_daten = bereinige_daten(daten)
    speichere_daten(bereinigte_daten, ausgabedatei)

    # Oder Verwendung einer Klasse
    # verarbeiter = DatenVerarbeiter(eingabedatei)
    # verarbeiter.bereinige_daten()
    # verarbeiter.speichere_daten(ausgabedatei)

    print("Datenverarbeitung abgeschlossen.")
```

## 6. Verwende die `if __name__ == "__main__":`-Anweisung

Dies ist ein gängiges Python-Idiom, mit dem du prüfen kannst, ob das Skript als Hauptprogramm ausgeführt wird. So stellst du sicher, dass die `main()`-Funktion nur aufgerufen wird, wenn das Skript direkt ausgeführt wird. Wenn du die `main()`-Funktion direkt ausführst, wird sie nicht ausgeführt, wenn das Modul oder Teile davon in einem anderen Skript importiert werden.

Füge also am Ende deines Skripts hinzu:

```python
if __name__ == "__main__":
    main()
```

Dies prüft, ob das Skript als Hauptprogramm ausgeführt wird, und ruft entsprechend `main()` auf.

## Alles zusammenführen

So könnte dein Skript aussehen, wenn du all diese Best Practices kombinierst:

```python
"""
Dieses Skript lädt Rohdaten, bereinigt sie durch Entfernen von Nullwerten und Duplikaten, und speichert die verarbeiteten Daten in einer neuen Datei.
"""

import os
import sys
import pandas as pd
import numpy as np

def lade_daten(dateipfad: str) -> pd.DataFrame:
    """Lädt Daten aus einer CSV-Datei.

    Parameter:
    ----------
    dateipfad : str
        Pfad zur CSV-Datei.

    Rückgabe:
    -------
    pd.DataFrame
        Geladene Daten als DataFrame.
    """
    return pd.read_csv(dateipfad)

def bereinige_daten(df: pd.DataFrame) -> pd.DataFrame:
    """Bereinigt den DataFrame durch Entfernen von Nullwerten und Duplikaten.

    Parameter:
    ----------
    df : pd.DataFrame
        Eingabe-DataFrame.
              
    Rückgabe:
    -------
    pd.DataFrame
        Bereinigter DataFrame.
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def speichere_daten(df: pd.DataFrame, ausgabepfad: str) -> None:
    """Speichert den DataFrame in einer CSV-Datei.

    Parameter:
    ----------
    df : pd.DataFrame
        Zu speichernder DataFrame.
    ausgabepfad : str
        Pfad zum Speichern der CSV-Datei.
    """
    df.to_csv(ausgabepfad, index=False)

def main():
    """Hauptfunktion, die die Datenverarbeitung steuert."""
    eingabedatei = 'data/raw/data.csv'
    ausgabedatei = 'data/processed/bereinigte_daten.csv'

    daten = lade_daten(eingabedatei)
    bereinigte_daten = bereinige_daten(daten)
    speichere_daten(bereinigte_daten, ausgabedatei)

    print("Datenverarbeitung abgeschlossen.")

if __name__ == "__main__":
    main()
```

## Zusätzliche Tipps

- **Kommentiere deinen Code:** Verwende Kommentare, um nicht offensichtliche Teile deines Codes zu erklären. Strebe jedoch danach, Code zu schreiben, der selbsterklärend ist.
- **Befolge die PEP 8-Richtlinien:** Halte dich an den [PEP 8](https://www.python.org/dev/peps/pep-0008/)-Styleguide für Python-Code, um die Lesbarkeit zu verbessern. Um dies zu erleichtern, verwende einen Auto-Formatter wie `black` oder `ruff`.
- **Verwende aussagekräftige Variablen-, Funktions- und Klassennamen:** Wähle Namen, die ihren Zweck vermitteln. Vermeide Ein-Buchstaben-Variablennamen, außer für einfache Iteratoren. Statt `x` und `y` verwende z. B. `zeit` und `signal`.
- **Behandle Ausnahmen:** Verwende try-except-Blöcke, um potenzielle Fehler elegant zu handhaben.

  ```python
  try:
      daten = lade_daten(eingabedatei)
  except FileNotFoundError:
      print(f"Fehler: Die Datei {eingabedatei} wurde nicht gefunden.")
      sys.exit(1)
  ```

- **Verwende Logging anstelle von Print-Anweisungen:** Für größere Skripte solltest du das `logging`-Modul verwenden, um eine bessere Kontrolle über Logging-Level und -Ausgaben zu haben.

  ```python
  import logging

  logging.basicConfig(level=logging.INFO)

  logging.info("Datenverarbeitung abgeschlossen.")
  ```

- **Parameterisiere deine Skripte:** Verwende Kommandozeilenargumente oder eine Konfigurationsdatei, um dein Skript flexibler zu gestalten.

  ```python
  import argparse

  def parse_arguments():
      parser = argparse.ArgumentParser(description="Daten verarbeiten und bereinigen.")
      parser.add_argument('--input', required=True, help='Pfad zur Eingabedatei')
      parser.add_argument('--output', required=True, help='Pfad zur Ausgabedatei')
      return parser.parse_args()

  def main():
      args = parse_arguments()
      daten = lade_daten(args.input)
      bereinigte_daten = bereinige_daten(daten)
      speichere_daten(bereinigte_daten, args.output)
  ```

- **Mache deinen Code modular:** Zerlege dein Skript in mehrere Dateien oder Module für bessere Organisation und Wiederverwendbarkeit. Verschiebe beispielsweise Datenverarbeitungsfunktionen, die in mehreren Skripten verwendet werden, in ein separates Modul namens `datenverarbeitung.py`.

- **Coding einer Abbildung:** Wenn du eine Abbildung codest, kannst du unserem [Leitfaden zum Codieren einer Abbildung](https://github.com/bendalab/plottools/blob/master/docs/guide.md) folgen. Wenn du die gleichen Prinzipien auf deinen Abbildungscode anwendest, wird es einfacher, ihn zu modifizieren und wiederzuverwenden.

## Fazit

Wenn du diese Best Practices befolgst, erstellst du Python-Skripte, die:

- **Lesbar** sind: Klare Struktur und Benennung machen deinen Code leicht verständlich.
- **Wartbar** sind: Kapselung und Modularität vereinfachen Updates und Debugging.
- **Wiederverwendbar** sind: Funktionen und Klassen können in anderen Skripten importiert und verwendet werden.
- **Robust** sind: Fehlerbehandlung stellt sicher, dass dein Skript unerwartete Situationen handhaben kann.

Denke daran, dass gute Codingraktiken nicht nur dir das Leben erleichtern, sondern auch anderen helfen, die vielleicht mit deinem Code arbeiten. Die Mühe, die du in das Schreiben sauberer und effektiver Skripte steckst, wird sich langfristig auszahlen.

Viel Spaß beim Programmieren!
