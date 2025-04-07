# Data Analysis Structure Guide

**German version**: [README_DE.md](README_de.md)

Welcome to our Project Structure Guide! This guide is designed to
help new students understand how to structure data analysis projects in Python
effectively. By following these best practices, you'll create projects that are
organized, maintainable, and reproducible.

## Table of Contents

1. [Project Structure](#project-structure)
   - [Separating Data and Code](#separating-data-and-code)
   - [Separating Figures and Code](#separating-figures-and-code)
2. [Version Control with Git](#version-control-with-git)
   - [Basic Git Commands](#basic-git-commands)
3. [Best Practices for Data Analysis Projects](#best-practices-for-data-analysis-projects)
4. [Additional Resources](#additional-resources)
5. [Conclusion](#conclusion)

---

## Project Structure

A well-organized project structure is crucial for collaboration and
scalability. Here's a recommended directory layout:

```
project-name/
├── data/
│   ├── model_weights/          # Trained model weights
│   ├── raw/                    # Original, unmodified datasets
│   └── processed/              # Cleaned or transformed data
├── code/
│   └── my_python_program.py    # Python scripts
├── figures/
├── docs/
│   ├── my_fancy_latex_thesis/  # LaTeX files for thesis (advised)
│   ├── my_presentation.pptx    # Presentation slides
│   └── my_thesis.docx          # Word document (not recommended)
├── .gitignore                  # Files and directories for Git to ignore
├── README.md                   # Project overview and instructions
└── requirements.txt            # Python dependencies
```

### Separating Data and Code

- **Data Directory (`data/`)**: Store all your datasets here.
  - `raw/`: Original, unmodified datasets.
  - `processed/`: Data that's been cleaned or transformed.
- **Source Code Directory (`code/`)**: Contains all the code scripts and modules.

**Benefits:**

- **Organization**: Keeps your data separate from code, making it easier to manage.
- **Reproducibility**: Clear separation ensures that data processing steps are documented and repeatable.
- **Collaboration**: We/you/collaborators can easily find and understand different components of the project.

### Separating Figures and Code

- **Figures Directory (`figures/`)**: Store all generated plots, images, and visualizations.

**Benefits:**

- **Clarity**: Separates output from code, reducing clutter.
- **Version Control**: Easier to track changes in code without large binary files like images.
- **Presentation**: Simplifies the process of creating reports or presentations by having all figures in one place.

---

## Version Control with Git

Git is a powerful version control system that helps you track changes,
collaborate with others, and manage your project's history. But what is version
control? Have you ever found yourself creating files like `project_final_v2.py`
or `project_final_final.py`? Version control solves this problem by keeping
track of changes and allowing you to revert to previous versions. As a bonus,
you'll also have a backup of your project in case something goes wrong. There
is no good reason to not use it!

### Basic Git Commands

- **Initialize a Repository**

  ```bash
  git init
  ```

- **Add Remote Repository (GitHub, Gittea)**

  ```bash
  git remote add origin <repository-url>
  ```

- **Clone a Repository**

  ```bash
  git clone <repository-url>
  ```

- **Check Status**

  ```bash
  git status
  ```

- **Add Changes**

  ```bash
  git add <file-name>
  # Or add all changes
  git add .
  ```

- **Commit Changes**

  ```bash
  git commit -m "Commit message"
  ```

- **Push to Remote Repository**

  ```bash
  git push origin main
  ```

- **Pull from Remote Repository**

  ```bash
  git pull origin main
  ```
  #### Advanced Git Commands

- **Create a New Branch**

  ```bash
  git branch <branch-name>
  ```

- **Switch Branches**

  ```bash
  git checkout <branch-name>
  ```

- **Merge Branches**

  ```bash
  git merge <branch-name>
  ```

- **View Commit History**

  ```bash
  git log
  ```

**Tips:**

- **Commit Often**: Regular commits make it easier to track changes.
- **Meaningful Messages**: Use descriptive commit messages for better understanding.
- **Use `.gitignore`**: Exclude files and directories that shouldn't be tracked (e.g., large data files, virtual environments).
  This is important as git repositories that store large binary data can quickly blow up in size and become impossible to push or pull. A template for such a `.gitignore` file can be found [here](.gitignore).

If you (and maybe other new students) have never heard of, or used Git before,
and you prefer a formal introduction, approach your supervisor, or your peers
to arrange a workshop to get you started with Git.

---

## Best Practices for Data Analysis Projects

1. **Use Virtual Environments**

   - Utilize `venv`, `conda` or `pyenv` to manage project-specific dependencies.
   - Document dependencies in `requirements.txt` or use `poetry` for package management.

2. **Document Your Work**

   - Maintain a clear and informative `README.md`.
   - Use docstrings and comments in your code.
   - Keep a changelog for significant updates. This is useful but also very rewarding, as it gives you a sense for what you accomplished!

3. **Write Modular Code**

   - Break code into functions and classes.
   - Reuse code to avoid duplication.

4. **Follow Coding Standards**

   - Adhere to PEP 8 guidelines for Python code.
   - Use linters like `flake8` or formatters like `black` or `ruff` to maintain code quality. These can be used as terminal commands or intergrated into your code editor to automatically format your code using best practices.

5. **Automate Data Processing**

   - Write scripts to automate data cleaning and preprocessing.
   - Ensure scripts can be run end-to-end to reproduce results.

6. **Test Your Code**

   - If you write a python package, write unit tests using frameworks like `unittest` or `pytest`.
   - Keep tests in the `tests/` directory.

7. **Handle Data Carefully**

   - Do not commit data to version control.

8. **Version Your Data and Models**

   - Save model versions with timestamps or unique identifiers.

9. **Backup Regularly**

   - Push changes to a remote repository frequently.
   - Create additional backups for critical data! Approach your supervisor if you need storage space or help backing things up.

10. **Collaborate Effectively**

    - Use branches for new features or experiments.
    - Merge changes with pull requests and code reviews.

---

## Additional Resources

- **Git Documentation**: [git-scm.com/docs](https://git-scm.com/docs)
- **PEP 8 Style Guide**: [python.org/dev/peps/pep-0008](https://www.python.org/dev/peps/pep-0008/)
- **Python Virtual Environments**:
  - [`venv` Module](https://docs.python.org/3/library/venv.html)
  - [Anaconda Distribution](https://www.anaconda.com/products/distribution)
  - [`pyenv` Virtual Environments](https://github.com/pyenv/pyenv)

---

## Conclusion

Structuring your data analysis projects effectively is the first step towards
successful and reproducible research. By separating data, code, and figures,
using version control, and following best practices, you set a strong
foundation for your work and collaboration with others.

Happy coding!

You might consider continuing with our guide [writing nice code](3_code.md).
