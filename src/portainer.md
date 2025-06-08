# Portainer

Portainer is a lightweight management UI for Docker, Kubernetes, Docker Swarm, and Azure ACI. It allows you to manage your containers, images, networks, and volumes from a web browser. This page provides instructions for installing the Portainer Community Edition (CE).

While Portainer is a popular choice, here are some alternatives you might consider:

- [Rancher](https://www.rancher.com/) - More for Kubernetes (container orchestration)
- [Dockage](https://github.com/louislam/dockge) - Portainer but made by the same people who made [UptimeKuma](https://github.com/louislam/uptime-kuma) mainly focuses on the `docker-compose.yml` side, but some users have found it more helpful than Portainer

### Installation Steps

Follow these steps to install the Portainer Community Edition:

1.  **Create a Docker Volume:** This volume will store Portainer's persistent data.

    ```sh
    sudo docker volume create portainer_data
    ```

    ```admonish info
    This creates a docker volume which Portainer's data will be stored in
    ```

2.  **Deploy the Portainer Container:** Run the following command to download and start the Portainer container.

    ```sh
    sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
    ```

3.  **Create a Docker Network (Optional but recommended):** It's good practice to put your containers on a dedicated network. Replace `(name of network)` with your desired network name (e.g., `my-app-network`).

    ```sh
    sudo docker network create (name of network)
    ```
