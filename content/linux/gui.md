+++
insert_anchor_links = "left"
title = "Managing the Graphical User Interface (GUI)"
[extra]
go_to_top = true
+++

This document provides commands to switch your system's default boot target between the graphical user interface (GUI) mode and the command-line interface (CLI) mode.

Switching between these modes can be useful depending on whether you need a graphical environment or prefer working solely from the command line.

> [!NOTE]
> These commands are applicable for systems using `systemd`.

## Disable GUI (Boot to Command Line):

To set the system to boot directly into the command line (multi-user mode) without a graphical environment, use the following commands:

1.  Set the default target to `multi-user.target`:
    ```sh
    sudo systemctl set-default multi-user.target
    ```
2.  Reboot the system for the change to take effect:
    ```sh
    sudo reboot
    ```

## Enable GUI (Boot to Graphical Interface):

To set the system to boot into the graphical user interface, use the following commands:

1.  Set the default target to `graphical.target`:
    ```sh
    sudo systemctl set-default graphical.target
    ```
2.  Reboot the system for the change to take effect:
    ```sh
    sudo reboot
    ```
