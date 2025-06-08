# Portainer

I could make a whole page for this, so I did.

Some people have found alternatives for Portainer:

- [Rancher](https://www.rancher.com/) - More for Kubernetes (container orchestration)
- [Dockage](https://github.com/louislam/dockge) - Portainer but made by the same people who made [UptimeKuma](https://github.com/louislam/uptime-kuma) mainly focuses on the `docker-compose.yml` side, but some users have found it more helpful than Portainer

To install the Community Edition of Portainer:

Run:

```sh
sudo docker volume create portainer_data
```

```admonish info
This creates a docker volume which Portainer's data will be stored in
```

Then to install the container you'll run:
```sh
sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

We'll also create a docker network for our containers to run on by running the following command:

```sh
sudo docker network create (name of network)
```
