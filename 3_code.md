# Writing a Good Python Script: A Primer

This primer will guide you through best practices to write effective and clean
Python scripts. Whether you're working on a data processing pipeline, a machine
learning model, or a simple utility script, following these guidelines will
help you create maintainable and readable code.

## 1. Use a Declarative and Meaningful Script Name

Choose a script name that clearly describes its purpose. This makes it easier
for others (and yourself) to understand what the script does without reading
the code.

**Examples:**

- `data_cleaning.py` instead of `script1.py`
- `generate_report.py` instead of `run.py`

## 2. Start with a Short Explanation (Docstring)

At the beginning of your script, include a docstring that briefly explains what
the script does. This helps users quickly grasp the script's functionality, if
the name is not already clear enough.

```python
"""
This script loads raw data, cleans it by removing null values and duplicates,
and saves the processed data to a new file.
"""
```

## 3. Import All Required Packages at the Beginning

List all your imports at the top of the script. This makes dependencies clear
and simplifies maintenance.

```python
import sys                # Packages that are provided by Python
from pathlib import Path

import numpy as np        # Packages that are downloaded, specified in the requierements.txt
import pandas as pd

import my_module          # Modules that are written by yourself
```

## 4. Encapsulate Code in Functions and Classes

Organize your code by wrapping functionality within functions or classes. This
promotes code reuse, testing, and readability. Ideally, functions should do one
thing and do it well. Classes can be used for more complex logic or when you need
to maintain state. Clean functions and classes contain type hints and docstrings
to explain their purpose and inputs/outputs.

**Examples of Functions:**

```python
def load_data(file_path: str) -> pd.DataFrame:
    """Loads data from a CSV file.

    Parameters:
    ----------
    file_path : str
        Path to the CSV file.

    Returns:
    -------
    pd.DataFrame
        Loaded data as a DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the DataFrame by removing null values and duplicates.

    Parameters:
    ----------
    df : pd.DataFrame
        Input DataFrame.
          
    Returns:
    -------
    pd.DataFrame
        Cleaned DataFrame.
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Saves the DataFrame to a CSV file.

    Parameters:
    ----------
    df : pd.DataFrame
        DataFrame to save.
    output_path : str
        Path to save the CSV file.
    """
    df.to_csv(output_path, index=False)
```

**Example of a Class:**

```python
class DataProcessor:
    """A class for processing data."""

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

## 5. Define a `main()` Function

Create a `main()` function that serves as the entry point of your script. This
function should orchestrate the flow of your program.

```python
def main():
    """Main function that orchestrates the data processing."""
    input_file = 'data/raw/data.csv'
    output_file = 'data/processed/clean_data.csv'

    # Using functions
    data = load_data(input_file)
    clean_data = clean_data(data)
    save_data(clean_data, output_file)

    # Or using a class
    # processor = DataProcessor(input_file)
    # processor.clean_data()
    # processor.save_data(output_file)

    print("Data processing complete.")
```

## 6. Use the `if __name__ == "__main__":` Statement

This is a common Python idiom that allows you to check if the script is being
run as the main program. This ensures that the `main()` function is only called
when the script is executed directly. If you execute the `main()` function
directly, it will be executed when the module, or just parts of it, are
imported in another script.

So at the end of your script, add:

```python
if __name__ == "__main__":
    main()
```

This checks if the script is being run as the main program and calls `main()` accordingly.

## Putting It All Together

Here's how your script might look when you combine all these best practices:

```python
"""
This script loads raw data, cleans it by removing null values and duplicates, and saves the processed data to a new file.
"""

import os
import sys
import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """Loads data from a CSV file.

    Parameters:
    ----------
    file_path : str
        Path to the CSV file.

    Returns:
    -------
    pd.DataFrame
        Loaded data as a DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the DataFrame by removing null values and duplicates.

    Parameters:
    ----------
    df : pd.DataFrame
        Input DataFrame.
          
    Returns:
    -------
    pd.DataFrame
        Cleaned DataFrame.
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Saves the DataFrame to a CSV file.

    Parameters:
    ----------
    df : pd.DataFrame
        DataFrame to save.
    output_path : str
        Path to save the CSV file.
    """
    df.to_csv(output_path, index=False)

def main():
    """Main function that orchestrates the data processing."""
    input_file = 'data/raw/data.csv'
    output_file = 'data/processed/clean_data.csv'

    data = load_data(input_file)
    clean_data = clean_data(data)
    save_data(clean_data, output_file)

    print("Data processing complete.")

if __name__ == "__main__":
    main()
```

## Additional Tips

- **Comment Your Code:** Use comments to explain non-obvious parts of your code. However, strive to write code that is self-explanatory.
- **Follow PEP 8 Guidelines:** Adhere to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code to improve readability. To make this easy, use an auto-formatter like `black` or `ruff`.
- **Use Meaningful Variable, Function and ClasE Names:** Choose names that convey their purpose. Avoid single-letter variable names except for simple iterators. Instead of `x` and `y` use e.g., `time` and `signal`.
- **Handle Exceptions:** Use try-except blocks to handle potential errors gracefully.
  
  ```python
  try:
      data = load_data(input_file)
  except FileNotFoundError:
      print(f"Error: The file {input_file} was not found.")
      sys.exit(1)
  ```

- **Use Logging Instead of Print Statements:** For larger scripts, consider using the `logging` module for better control over logging levels and outputs.
  
  ```python
  import logging

  logging.basicConfig(level=logging.INFO)

  logging.info("Data processing complete.")
  ```

- **Parameterize Your Scripts:** Use command-line arguments or a configuration file to make your script more flexible.
  
  ```python
  import argparse

  def parse_arguments():
      parser = argparse.ArgumentParser(description="Process and clean data.")
      parser.add_argument('--input', required=True, help='Input file path')
      parser.add_argument('--output', required=True, help='Output file path')
      return parser.parse_args()

  def main():
      args = parse_arguments()
      data = load_data(args.input)
      clean_data = clean_data(data)
      save_data(clean_data, args.output)
  ```

  - **Make Your Code Modular:** Break down your script into multiple files or
  modules for better organization and reusability. For example, move data
  processing functions that are used in multiple scripts to a separate module
  called `data_processing.py`.
  
  - **Coding a figure:** If you are coding a figure, you can follow our [coding
  a figure
  guide](https://github.com/bendalab/plottools/blob/master/docs/guide.md).
  Applying the same principles to your figure code will make it easier to
  modify and reuse.
  

## Conclusion

By following these best practices, you'll create Python scripts that are:

- **Readable:** Clear structure and naming make your code easy to understand.
- **Maintainable:** Encapsulation and modularity simplify updates and debugging.
- **Reusable:** Functions and classes can be imported and used in other scripts.
- **Robust:** Error handling ensures your script can handle unexpected situations gracefully.

Remember, good coding practices not only make your life easier but also help
others who may work with your code in the future. The effort you put into
writing clean and effective scripts will pay off in the long run.

Happy coding!

You might want to consider continuing with reading our guide to [structuring your dataset](4_data.md). 

