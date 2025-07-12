# eShopOnSysbox
Complete .Net 7 microservices architecture using a sysbox powered master container (with systemd functionality) to run all 22 eShop docker containers within docker securely. 

# prerequisites
Install and configure sysbox on your dev server/laptop

install with yay on arch distros (refer to sysbox documentation for others - https://github.com/nestybox/sysbox) 

`yay -S sysbox-ce-bin`

enable and start sysbox
-----------------------
`sudo systemctl enable --now sysbox`

make sure this entry is in your docker deamon.json file (/etc/docker/daemon.json)
```
{
    "runtimes": {
        "sysbox-runc": {
            "path": "/usr/bin/sysbox-runc"
        }
    }
}
```


`sudo systemctl daemon-reload`

`sudo systemctl restart docker`

check that docker can see the sysbox runtime
--------------------------------------------
`docker info | grep -i runtime`
> Runtimes: sysbox-runc io.containerd.runc.v2 runc

# docker image
`docker pull karlpothast/eshoponsysbox:1.0.0`

# docker run
`docker run --runtime=sysbox-runc -itd -p 5100:5100 -p 5104:5104 -p 5107:5107 --name eshop karlpothast/eshoponsysbox:1.0.0`

# docker exec
`docker exec -it eshop bash`

# start containers script
`cd $HOME`
`./start-all-containers.sh`

![image](https://user-images.githubusercontent.com/13120778/227142708-a9e11b5d-d569-4f0a-aff0-0fc8766a7cdc.png)

You should be able to see the catalog, SPA app and health checker with the following URLs :
> http://localhost:5100
>
> http://localhost:5104
> 
> http://localhost:5107

![image](https://user-images.githubusercontent.com/13120778/227143805-10bb346e-d53e-43b4-be34-67ef73de5343.png)

# references
.net7 eShopOnContainers microservices architecture
https://github.com/dotnet-architecture/eShopOnContainers

Sysbox
https://github.com/nestybox/sysbox

Ubuntu 22.04 with systemd :
[jrei/systemd-ubuntu](https://hub.docker.com/r/jrei/systemd-ubuntu)
*this worked easier than nestybox's ubuntu 22.04 iamge

# to do
add docker-compose functionality to always get the latest version
