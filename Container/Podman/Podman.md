# شروع به کار با  Podman
======

* Works with containers.
* works with pods.
  * Pod: group of container that are deployed together on the same host.

## Pod
* Collection of containers shared a namespace.


## Podman
* Daemon-less architecture which is more flexible and secure.
* Run OCI containers on Linux.
## Dcoker
* Runs as a daemon on linux. 
  * Daemons Create amount of overhead, 
  * and it also requires root access to build a container 
    * that create security risks.
    * Docker run --privileged .. 
  * The daemon approach also stifles innovation in the container community.
    * If you want to change the way containers work, you need to change the docker daemon and push those changes upstream. 
    * without a daemon, the container infrastructure is more modular, and it's easier to make changes.
# Install podman on Fedorated
    
```shell
sudo dnf -y update
sudo dnf -y install podman
alias docker=podman
podman -v
podman info
```

## Create first pod
```shell
vim DOCKERFILE


```
* Create pod using DOCKERFILE
```shell
podman build -t open-adventure:podman .
```
* list images
```shell
podman images
```

* Create container from image
```shell
podman run --rm -it open-adventure:podman /bin/bash
```

* Show the running container
```shell
podman ps
```