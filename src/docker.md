# Docker

I've been using docker a lot more, and because of that, I was installing it over and over again. I've also been setting up multiple machines lately which hasn't been all too nice having to remember how to install it.

So, I just decided to leave myself a note about installing it so that I could just copy and paste (1 click) and not have to worry about installing it.

Going to [get.docker.com](https://get.docker.com/) brings you to the web page that hosts the awesome script provided by the docker team and following the commands below will help make the process even more simple.

1. Download the script:
```sh
curl -fsSL https://get.docker.com -o install-docker.sh
```

2. Then run the script:
```sh
sudo sh install-docker.sh
```

3. Then run:
```sh
sudo usermod -aG docker (username)
```

```admonish info
This command adds your user to the docker group, effectively allowing you to run docker commands without ```sudo```
```

4. Then reboot
```sh
sudo reboot
```

{{#author ld3z}}
