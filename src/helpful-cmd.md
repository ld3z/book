# Some helpful command line programs

This page lists some command-line tools that can significantly enhance your productivity and make working in the terminal easier and more efficient.

## Tmux :simple-icons-tmux:

Tmux ([Terminal Multiplexer]^(A tool that lets you switch between several programs in one terminal, detach them, and reattach them later.)) allows you to create and control multiple terminal sessions within a single window. This is incredibly useful for keeping tasks organized, detaching from sessions without losing progress, and pair programming.

Hover over <span data-tippy-content="This is a tooltip!">this text</span> to see a tooltip.

Can be installed by running:

```sh
sudo apt-get install tmux
```

Tmux has a comprehensive [cheat sheet](https://tmuxcheatsheet.com) for all of its commands. It's a great resource to keep handy.

**Basic Usage:**

To start a new Tmux session:

```sh
tmux
```

```admonish tip
To detach from a session (leaving it running in the background):
Press `Ctrl+b` followed by `d`.
```

To list existing sessions:

```sh
tmux list-sessions
```

To reattach to the most recent session:

```sh
tmux attach
```

To reattach to a specific session (replace `0` with the session number):

```sh
tmux attach -t 0
```

## TLDR :simple-icons-tldraw:

```admonish info
Shows simplified examples for command-line tools.
```

TLDR provides simplified, community-maintained examples for command-line programs. It cuts through lengthy man pages to give you just the common use cases. There is a site version and a terminal version.

Terminal can be installed by running:

```sh
sudo apt-get install tldr
tldr -u # Update the cache after installation
```

The site can be found [here](https://tldr.inbrowser.app).

**Basic Usage:**

To see examples for the `tar` command:

```sh
tldr tar
```

To see examples for the `ls` command with macOS options:

```sh
tldr ls --platform osx
```

## htop :simple-icons-htop:

```admonish info
htop is an interactive process viewer for Unix-like systems. It provides a dynamic real-time view of processes running on the system, showing CPU usage, memory usage, swap usage, and tasks. It's an improved version of the standard `top` command with a more user-friendly interface.
```

Can be installed by running:

```sh
sudo apt-get install htop
```

**Basic Usage:**

Simply run `htop` to launch the interactive viewer:

```sh
htop
```

```admonish tip
Inside `htop`, you can use arrow keys to navigate and function keys (like F1 for Help, F3 for Search, F9 for Kill, F10 to Quit) for various actions.
```
