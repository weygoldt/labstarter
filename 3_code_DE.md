# Eine Einführung zum Schreiben eines Guten Python-Skripts

Diese Einführung leitet dich durch die besten Praktiken, um effektive und saubere Python-Skripte zu schreiben. Egal, ob du an einer Datenverarbeitungspipeline, einem Machine-Learning-Modell oder einem einfachen Utility-Skript arbeitest – das Befolgen dieser Richtlinien hilft dir, wartbaren und lesbaren Code zu erstellen.

## 1. Verwende einen deklarativen und aussagekräftigen Skriptnamen

Wähle einen Skriptnamen, der seinen Zweck klar beschreibt. Dadurch wird es einfacher für andere (und dich selbst), zu verstehen, was das Skript macht, ohne den Code lesen zu müssen.

**Beispiele:**

- `data_cleaning.py` anstelle von `script1.py`
- `generate_report.py` anstelle von `run.py`

## 2. Beginne mit einer kurzen Erklärung (Docstring)

Füge zu Beginn deines Skripts einen Docstring hinzu, der kurz erklärt, was das Skript tut. Dies hilft den Benutzern, die Funktionalität des Skripts schnell zu erfassen, falls der Name nicht schon klar genug ist.

```python
"""
Dieses Skript lädt Rohdaten, bereinigt sie durch Entfernen von Nullwerten und Duplikaten und speichert die bearbeiteten Daten in einer neuen Datei.
"""
```

## 3. Importiere alle benötigten Pakete am Anfang

Liste alle deine Importe am Anfang des Skripts auf. Dies macht die Abhängigkeiten klar und vereinfacht die Wartung.

```python
import sys                # Pakete, die von Python bereitgestellt werden
from pathlib import Path

import numpy as np        # Pakete, die heruntergeladen werden, spezifiziert in der requirements.txt
import pandas as pd

import my_module          # Module, die du selbst geschrieben hast
```

## 4. Kapsle Code in Funktionen und Klassen

Organisiere deinen Code, indem du die Funktionalität in Funktionen oder Klassen verpackst. Dies fördert Wiederverwendbarkeit, Testbarkeit und Lesbarkeit des Codes. Idealerweise sollten Funktionen eine einzige Aufgabe gut erledigen. Klassen können für komplexere Logik oder wenn du Zustände beibehalten musst, verwendet werden. Saubere Funktionen und Klassen enthalten Type-Hints und Docstrings, um ihren Zweck und ihre Ein- und Ausgaben zu erklären.

**Beispiele für Funktionen:**

```python
def load_data(file_path: str) -> pd.DataFrame:
    """Lädt Daten aus einer CSV-Datei.

    Parameter:
    ----------
    file_path : str
        Pfad zur CSV-Datei.

    Rückgabe:
    -------
    pd.DataFrame
        Geladene Daten als DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Bereinigt das DataFrame durch Entfernen von Nullwerten und Duplikaten.

    Parameter:
    ----------
    df : pd.DataFrame
        Eingabe-DataFrame.
          
    Rückgabe:
    -------
    pd.DataFrame
        Bereinigtes DataFrame.
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Speichert das DataFrame in einer CSV-Datei.

    Parameter:
    ----------
    df : pd.DataFrame
        Zu speicherndes DataFrame.
    output_path : str
        Speicherpfad der CSV-Datei.
    """
    df.to_csv(output_path, index=False)
```

**Beispiel für eine Klasse:**

```python
class DataProcessor:
    """Eine Klasse zur Datenverarbeitung."""

    def __init__(self, file_path):
        self.data = self.load_data(file_path)

    def load_data(self, file_path):
        return pd.read_csv(file_path)

    def clean_data(self):
        self.data.dropna(inplace=True)
        self.data.drop_duplicates(inplace=True)

    def save_data(self, output_path):
        self.data.to_csv(output_path, index=False)
```

## 5. Definiere eine `main()`-Funktion

Erstelle eine `main()`-Funktion, die als Einstiegspunkt deines Skripts dient. Diese Funktion sollte den Ablauf deines Programms koordinieren.

```python
def main():
    """Hauptfunktion, die die Datenverarbeitung koordiniert."""
    input_file = 'data/raw/data.csv'
    output_file = 'data/processed/clean_data.csv'

    # Verwendung von Funktionen
    data = load_data(input_file)
    clean_data = clean_data(data)
    save_data(clean_data, output_file)

    # Oder mit einer Klasse
    # processor = DataProcessor(input_file)
    # processor.clean_data()
    # processor.save_data(output_file)

    print("Datenverarbeitung abgeschlossen.")
```

## 6. Verwende die `if __name__ == "__main__":`-Anweisung

Dies ist ein übliches Python-Idiom, das es dir ermöglicht, zu prüfen, ob das Skript als Hauptprogramm ausgeführt wird. Dies stellt sicher, dass die `main()`-Funktion nur aufgerufen wird, wenn das Skript direkt ausgeführt wird. Wenn du die `main()`-Funktion direkt ausführst, wird sie nicht ausgeführt, wenn das Modul oder nur Teile davon in einem anderen Skript importiert werden.

Füge daher am Ende deines Skripts hinzu:

```python
if __name__ == "__main__":
    main()
```

Dies überprüft, ob das Skript als Hauptprogramm ausgeführt wird, und ruft `main()` entsprechend auf.

## Alles Zusammenfügen

So könnte dein Skript aussehen, wenn du all diese Best Practices kombinierst:

```python
"""
Dieses Skript lädt Rohdaten, bereinigt sie durch Entfernen von Nullwerten und Duplikaten und speichert die bearbeiteten Daten in einer neuen Datei.
"""

import os
import sys
import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """Lädt Daten aus einer CSV-Datei.

    Parameter:
    ----------
    file_path : str
        Pfad zur CSV-Datei.

    Rückgabe:
    -------
    pd.DataFrame
        Geladene Daten als DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Bereinigt das DataFrame durch Entfernen von Nullwerten und Duplikaten.

    Parameter:
    ----------
    df : pd.DataFrame
        Eingabe-DataFrame.
          
    Rückgabe:
    -------
    pd.DataFrame
        Bereinigtes DataFrame.
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Speichert das DataFrame in einer CSV-Datei.

    Parameter:
    ----------
    df : pd.DataFrame
        Zu speicherndes DataFrame.
    output_path : str
        Speicherpfad der CSV-Datei.
    """
    df.to_csv(output_path, index=False)

def main():
    """Hauptfunktion, die die Datenverarbeitung koordiniert."""
    input_file = 'data/raw/data.csv'
    output_file = 'data/processed/clean_data.csv'

    data = load_data(input_file)
    clean_data = clean_data(data)
    save_data(clean_data, output_file)

    print("Datenverarbeitung abgeschlossen.")

if __name__ == "__main__":
    main()
```

## Zusätzliche Tipps

- **Kommentiere deinen Code:** Verwende Kommentare, um nicht offensichtliche Teile deines Codes zu erklären. Strebe jedoch danach, Code zu schreiben, der sich selbst erklärt.
- **Befolge die PEP 8-Richtlinien:** Halte dich an den [PEP 8](https://www.python.org/dev/peps/pep-0008/) Styleguide für Python-Code, um die Lesbarkeit zu verbessern. Nutze dazu Auto-Formatierer wie `black` oder `ruff`.
- **Verwende aussagekräftige Variablen-, Funktions- und Klassennamen:** Wähle Namen, die ihren Zweck vermitteln. Vermeide einbuchstabige Variablennamen, außer für einfache Iterationen. Anstelle von `x` und `y` verwende zum Beispiel `time` und `signal`.
- **Behandle Ausnahmen:** Verwende try-except-Blöcke, um potenzielle Fehler elegant zu behandeln.

  ```python
  try:
      data = load_data(input_file)
  except FileNotFoundError:
      print(f"Fehler: Die Datei {input_file} wurde nicht gefunden.")
      sys.exit(1)
  ```

- **Verwende Logging anstelle von Print-Anweisungen:** Für größere Skripte erwäge die Verwendung des `logging`-Moduls, um mehr Kontrolle über Logging-Level und Ausgaben zu erhalten.
  
  ```python
  import logging

  logging.basicConfig(level=logging.INFO)

  logging.info("Datenverarbeitung abgeschlossen.")
  ```

- **Parameterisiere deine Skripte:** Verwende Befehlszeilenargumente oder eine Konfigurationsdatei, um dein Skript flexibler zu machen.
  
  ```python
  import argparse

  def parse_arguments():
      parser = argparse.ArgumentParser(description="Daten verarbeiten und bereinigen.")
      parser.add_argument('--input', required=True, help='Eingabepfad zur Datei')
      parser.add_argument('--output', required=True, help='Ausgabepfad zur Datei')
      return parser.parse_args()

  def main():
      args = parse_arguments()
      data = load_data(args.input)
      clean_data = clean_data(data)
      save_data(clean_data, args.output)
  ```

  - **Mache deinen Code modular:** Zerlege dein Skript in mehrere Dateien oder
    Module für bessere Organisation und Wiederverwendbarkeit. Verschiebe beispielsweise
    Datenverarbeitungsfunktionen, die in mehreren Skripten verwendet werden, in ein
    separates Modul namens `data_processing.py`.
  
  - **Coding a figure:** Wenn du eine Figur programmierst, kannst du unserem
    [Coding a figure guide](https://github.com/bendalab/plottools/blob/master/docs/guide_DE.md)
    folgen. Die Anwendung der gleichen Prinzipien auf deinen Code wird es einfacher
    machen, ihn zu ändern und wiederzuverwenden.

## Fazit

Durch das Befolgen dieser Best Practices wirst du Python-Skripte erstellen, die:

- **Lesbar:** Klare Struktur und Benennung machen deinen Code leicht verständlich.
- **Wartbar:** Kapselung und Modularität vereinfachen Updates und Debugging.
- **Wiederverwendbar:** Funktionen und Klassen können in anderen Skripten importiert und verwendet werden.
- **Robust:** Fehlerbehandlung stellt sicher, dass dein Skript unerwartete Situationen elegant bewältigt.

Denke daran, dass gute Codierpraktiken nicht nur dein Leben erleichtern, sondern auch anderen helfen, die in Zukunft mit deinem Code arbeiten. Der Aufwand, den du in das Schreiben sauberer und effektiver Skripte steckst, wird sich langfristig auszahlen.

Viel Spaß beim Programmieren!

Vielleicht möchtest du weiterlesen und unseren Leitfaden zur [Strukturierung deines Datensatzes](4_data_DE.md) anschauen.
