# Docker

Docker is a platform used for developing, shipping, and running applications in containers. Installing it can sometimes involve several steps, and if you're setting up multiple machines or doing it frequently, remembering the exact process can be tedious.

This note serves as a quick reference for installing Docker using the convenience script provided by the Docker team.

1.  **Download the script:**
    ```sh
    curl -fsSL https://get.docker.com -o install-docker.sh
    ```
    This command downloads the installation script from [get.docker.com](https://get.docker.com) and saves it as `install-docker.sh`.

2.  **Run the script:**
    ```sh
    sudo sh install-docker.sh
    ```

    ```admonish info
    This executes the downloaded script with superuser privileges to perform the installation.
    ```
3.  **Add your user to the `docker` group:**
    ```sh
    sudo usermod -aG docker (username)
    ```

    ```admonish warning
    Replace `(username)` with your actual username. This command adds your current user to the `docker` group. Membership in this group allows you to run Docker commands without needing `sudo`. While convenient, understand that members of the `docker` group have permissions equivalent to the root user regarding Docker, so exercise caution.
    ```

4.  **Reboot your system:**
    ```sh
    sudo reboot
    ```

    ```admonish tip
    A reboot is usually required for the group changes made in the previous step to take effect.
    ```

5.  **Verify the installation:**
    After your system has restarted and you've logged back in, you can verify that Docker is installed and you can run commands without `sudo` by running the `hello-world` container:
    ```sh
    docker run hello-world
    ```

    ```admonish info
    This command downloads a test image and runs it in a container. If everything is set up correctly, you should see a message confirming that your Docker installation is working.
    ```
