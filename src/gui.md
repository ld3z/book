# Enabling Gui

Sometimes, I find it helpful to run a install in GUI mode, but sometimes I like to work with the command line.

So, here are the commands to enable and disable the GUI.

## Disable:

```sh
1. sudo systemctl set-default multi-user.target
2. sudo reboot
```

## Enable:

```sh
1. sudo systemctl set-default graphical.target
2. sudo reboot
```
