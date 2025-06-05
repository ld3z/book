# Docker

I've been using docker a lot more, and because of that, I was installing it over and over again. I've also been setting up multiple machines lately which hasn't been all to nice having to remember how to install it.

But, there was a site that I could goto, but ended up not working correctly.

So, I just decided to leave myself a note about installing it so that I could just copy and paste (1 click) and not have to worry about installing it.

Going to [get docker](https://get.docker.com/) brings you to the web page that hosts the awesome script provided by docker and following the commands below will help make the process even more simple.

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

4. Then reboot
```sh
sudo reboot
```

{{#author ld3z}}
