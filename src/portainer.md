# Portainer :simple-icons-portainer:

Portainer is a lightweight management UI for Docker :skill-icons-docker:, Kubernetes :skill-icons-kubernetes:, Docker Swarm, and Azure ACI :mdi-microsoft-azure:. It allows you to manage your containers, images, networks, and volumes from a web browser. This page provides instructions for installing the Portainer Community Edition (CE).

While Portainer is a popular choice, here are some alternatives you might consider:

- [Rancher :simple-icons-rancher:](https://www.rancher.com/) - More for Kubernetes (container orchestration)
- [Dockage](https://github.com/louislam/dockge) - Portainer but made by the same people who made [Uptime Kuma :simple-icons-uptimekuma:](https://github.com/louislam/uptime-kuma) mainly focuses on the `docker-compose.yml` side, but some users have found it more helpful than Portainer

## Installation Steps

Follow these steps to install the Portainer Community Edition:

1.  **Create a Docker Volume:**

    ```sh
    sudo docker volume create portainer_data
    ```

    ```admonish info
    This volume will store Portainer's persistent data.
    ```

2.  **Deploy the Portainer Container:** Run the following command to download and start the Portainer container.

    ```sh
    sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
    ```

3.  **Create a Docker Network (Optional but recommended):**

    ```admonish tip
    It's good practice to put your containers on a dedicated network. Replace `(name of network)` with your desired network name (e.g., `my-app-network`).
    ```

    ```sh
    sudo docker network create (name of network)
    ```

### App Templates :material-symbols-touch-app:

In Portainer, [App Templates](https://docs.portainer.io/user/docker/templates) enable you to easily deploy services with a predetermined configuration, while allowing you to customize options through the web UI. While Portainer ships with some default templates (see [portainer/templates](https://github.com/portainer/templates)), it’s often helpful to have 1-click access to many more apps + stacks, without having to constantly switch template sources.

Under Settings → App Templates in your Portainer GUI, paste this URL:

```sh
https://raw.githubusercontent.com/Lissy93/portainer-templates/main/templates.json
```
