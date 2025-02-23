# Structuring the `/data` Directory

German version: [README_de.md](README_de.md)

```
project-name/
├── data/
    ├── raw/          # Original, unmodified data
    ├── intermediate/ # Dervided data that is not "final"   
    ├── processed/    # Data derived from raw or intermediate data
    └── models/       # Model weights and outputs (if applicable)
```

## Guidelines

- **`raw/`**:
  - Store all original data exactly as collected.
  - **Do not modify** these files to preserve data integrity.
  - Include metadata or use clear filenames with dates to indicate when the data was recorded.

From your raw data, we usually extract some meaningful features that we want to
further analyze:

- **`intermediate/`**:
  - Place derived data here. This additional layer might not be useful for some projects.
  - For example, intermediate data could be position tracks of animals if your raw data are videos or spectrograms if your raw data are audio files.

So you now analyzed the extracted data and want to create summary figures.
Because you don't want to run your analysis each time you try to plot a figure,
it is best to save the output of your analyses to files, e.g., `.csv` files. A
plotting script then directly loads these files included in the `processed/`
directory.

- **`processed/`**:
  - Place cleaned or transformed data here.
  - Generate these files using scripts.
  - Document processing steps if necessary.
  - This is usually the final version of data that is directly used for plotting

If your analysis contains any model training, we usually store the trained
model weights, checkpoints, and outputs in the `models/` directory.

- **`models/`** (if you are training models):
  - Save model weights, checkpoints, and outputs.
  - Organize by experiment or model version if needed.
  - Include metadata about training parameters or results.
