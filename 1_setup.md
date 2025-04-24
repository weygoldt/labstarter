# 🖥️ Environment Setup Guide

Welcome! This guide will help you set up your computing environment for working
in the lab. Most of our machines run a version of Linux called [Ubuntu](https://ubuntu.com/), and we use Python with [`pyenv`](https://github.com/pyenv/pyenv) or [`uv`](https://docs.astral.sh/uv/) for
managing versions and virtual environments.

## Getting Started with the Linux Terminal
Linux is a powerful, free and open source operating system, perfect for research and data analysis. Here are some basics:

- Open a terminal with `Ctrl + Alt + T`
- Navigate directories: `cd <folder>`
- List files: `ls`
- Create a folder: `mkdir <folder>`
- Move files: `mv <source> <destination>`
- Copy files: `cp <source> <destination>`
- Remove files: `rm <file>` (use with caution! This will permanently delete the file, there is no undo. For example, `rm -rf /` will delete the entire filesystem.)
- Edit files: Terminal editors like `nano <file>` or `vim <file>` allow you to create, edit, and save files from the terminal.

For more, check out [this Linux command guide](https://linuxcommand.org/).

## Installing Software on Ubuntu
Most software can be installed using `apt`. For example:

```sh
sudo apt update && sudo apt upgrade -y  # Update package lists
sudo apt install git python3 python3-venv -y  # Install some essential tools
```

To remove software:

```sh
sudo apt remove <package-name>
```
You might want to install your code editor of choice (e.g., nvim, emacs,
Visual Studio Code, PyCharm, etc.). In many cases, it might be already
installed.

## Using Python with `pyenv`
We use `pyenv` to manage different Python versions. To install it, we first need the python build essentials: 

```sh
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Then, we can download and run the `pyenv` auto-installer.

```sh
curl https://pyenv.run | bash
```

After this finishes, the installer suggests to put some things in your shells config file. To do this automatically, just run these lines in the terminal: 

```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
```

Then, restart your shell and run:

```sh
pyenv install 3.12  # Install Python 3.12
pyenv global 3.12  # Set it as the default
```

To check the installed versions:

```sh
pyenv versions
```

> NOTE: Most machines in our lab currently use `pyenv`, but some people are gradually moving to `uv`, as it is faster. If you want to use `uv` instead, follow the instructions
> [here](https://docs.astral.sh/uv/installation.html). You can use `uv` and `pyenv` together, but it is not recommended. If you want to use `uv`, you should remove `pyenv` first.

## Virtual Environments: Why and How to Use Them
Virtual environments isolate dependencies for different projects, preventing
conflicts. It's like a sandbox for your code and makes it easier to manage
dependencies, thus improving reproducibility.

### Creating a Virtual Environment

```sh
python -m venv venv  # Create a new virtual environment
source venv/bin/activate  # Activate it (Linux/macOS)
```

Now, your prompt should show `(venv)`, meaning it's active. To deactivate:

```sh
deactivate
```

### Using `pyenv` with Virtual Environments
Instead of the standard `venv`, you can use `pyenv-virtualenv` for more flexibility:

```sh
pyenv virtualenv 3.12 myenv  # Create a virtual environment called `myenv`
pyenv activate myenv  # Activate it
pyenv local myenv  # Automatically activate in the current directory
```

This method allows you to use the same virtual environment across multiple projects.

## Next Steps
Congratulations! Now that you have a **comfy** computing environment is set up, check out:

- [General Workflow Guide](0_workflow_and_help.md)
- [Structuring a Data Analysis Project](3_data_analysis_project.md)

