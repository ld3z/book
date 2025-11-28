# Minecraft Servers in Docker

I use [itzg/docker-minecraft-server](https://github.com/itzg/docker-minecraft-server) containers whenever possible since they are easy to maintain and run.

I like to run the server in a compose file, because it makes managing it a little easier than trying to remember what run command I would need to use with every single variable needed.

So, I'd like to keep some commands handy that I use to manage them.

For instance, running commands inside the container can be done be running

```sh
docker exec -i mc_server rcon-cli
```

> [!NOTE]
> This command's ```mc_server``` is a placeholder for whatever you called your container name in your compose file

## Some things to keep in mind

There are somethings that you should utilize, regardless of server software. Like online-mode or creating a whitelist.
Enabling both of those options should protect your server from unauthorized visitors.

## Useful Links:
- [itzg docker-minecraft-server wiki](https://docker-minecraft-server.readthedocs.io/) :twemoji-glowing-star: [^tooltip:@mccontainer]
- [Paper-chan's Paper Optimizations](https://paper-chan.moe/paper-optimization/) :twemoji-glowing-star: [^tooltip:@paperchan]
- [YouHaveTrouble's Optimizations](https://github.com/YouHaveTrouble/minecraft-optimization) :twemoji-glowing-star: [^tooltip:@youhavetrouble]
- [Paper](https://papermc.io/downloads/paper) [^tooltip:@paper]
- [Folia](https://papermc.io/downloads/folia) [^tooltip:@folia]
