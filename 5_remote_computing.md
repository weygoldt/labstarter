# 🌍 Remote Computing Guide

Working with remote machines is a key part of our lab's workflow. This guide
will introduce you to the essential tools for connecting, transferring files,
mounting remote drives, and running code efficiently. This way, you can
analyze your multi-terrabyte dataset on a perfomant machine in our lab
from your couch at home!

## 🔑 Connecting to Remote Hosts with SSH
All lab machines have a default user called `efish`. For its password, please
ask anybody in the lab. To connect to a remote machine, use:

```sh
ssh efish@remote-host.am28.uni-tuebingen.de
```

You are now in a terminal session on this machine and can do anything you
can also do on your local machine!

All computers have a host name. Usually, a sticker on the front of the machine
contains the host name. For example, if the machine is called `torpedo`:

```sh
ssh efish@torpedo.am28.uni-tuebingen.de
```

### SSH Keys for Passwordless Login
To avoid entering your password repeatedly, set up an SSH key:

```sh
ssh-keygen -t ed25519  # Generate a key (press Enter for defaults)
ssh-copy-id efish@remote-host.am28.uni-tuebingen.de  # Copy your key to the remote machine
```

Now you can log in without typing a password.

## 📂 Transferring Files with Rsync
For efficient file transfers, we use `rsync`, which syncs files between local
and remote systems or also between directories on your local device.

Copy a file **to** a remote machine:

```sh
rsync -av file.txt efish@remote-host:/path/to/destination/
```

Copy a file **from** a remote machine:

```sh
rsync -av efish@remote-host:/path/to/file.txt ./local-folder/
```

To copy entire directories and preserve permissions:

```sh
rsync -av --progress source-folder/ efish@remote-host:/destination-folder/
```

## 🔗 Mounting Remote Drives with SSHFS
Large datasets are usually stored on our storage server. Because this server is
located in our lab, you can remotely mount any drive or directory of that
server on your own machine in the lab. Because all devices are connected via
ethernet, you can access this data as if it is on a harddrive directly
connected to your machine. If you work with large datasets, you can **mount
remote directories locally** using SSHFS:

```sh
mkdir ~/remote-data  # Create a mount point
sshfs efish@remote-host:/path/to/data ~/remote-data
```

Now you can access remote files as if they were local. To unmount:

```sh
fusermount -u ~/remote-data
```

## 🧑‍💻 Running Code on Remote Machines
### Using SSH Tunneling with VS Code
VS Code has built-in support for remote development over SSH. To use it:
1. Install the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension.
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
3. Select **Remote-SSH: Connect to Host...** and enter `efish@remote-host.am28.uni-tuebingen.de`.

This allows you to edit and run code remotely with full VS Code support.

### Syncing and Running Code Manually
If you prefer, you can edit code locally and sync it with `rsync`, then execute it via SSH:

```sh
rsync -av my_script.py efish@remote-host:~/workspace/
ssh efish@remote-host 'python3 ~/workspace/my_script.py'
```

For frequent use, consider writing a small script to automate syncing and running.

## 📝 Efficient Remote Workflows with Terminal Tools
### Using Neovim for Remote Editing
If you want to avoid syncing files manually, consider a terminal-based code
editor like `neovim`, which allows to edit code on the remote host in your
`ssh` session. For further help, **Patrick and Alex** in the lab can assist
with Neovim setup. This code editor has a steep learning curve, but it is
extremely powerful.

### Running Persistent Sessions with Tmux
If you connect to a remote host via ssh, start a script, and disconnect before
it finishes, you will close your remote terminal session and the script will
stop. `tmux` fixes this by letting you start a session, run processes, and
reconnect later—even if you lose connection.

Start a new session on a remote machine:

```sh
tmux new -s mysession
```

Detach from a session (leaves it running):

```sh
Ctrl + B, then press D
```

Reconnect to a running session:

```sh
tmux attach -t mysession
```

This is useful when running long experiments or scripts remotely.

## 🔗 Summary
| Task                         | Recommended Tool |
|------------------------------|----------------|
| Connect to remote machine   | `ssh` |
| Copy files efficiently      | `rsync` |
| Mount remote directories    | `sshfs` |
| Edit files remotely         | `Neovim`, `VS Code SSH` |
| Run persistent processes    | `tmux` |

Now that we got you setup with remote computing, you might check out our short
guide to [writing and literature research](6_literature.md).
