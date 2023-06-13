# Debugging Kubernetes nodes with crictl

[Mapping from dockercli to crictl](https://kubernetes.io/docs/reference/tools/map-crictl-dockercli/)

[crictl](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/)

[download crictl](https://github.com/kubernetes-sigs/cri-tools/releases)

```bash
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.27.0/crictl-v1.27.0-darwin-amd64.tar.gz
sudo tar -xzf crictl-v1.27.0-darwin-amd64.tar.gz -C /usr/local/bin/
```
# OR
```bash
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.27.0/crictl-v1.27.0-linux-amd64.tar.gz
tar -xzvf crictl-v1.27.0-linux-amd64.tar.gz
sudo mv crictl /usr/local/bin
sudo crictl ps
```

```bash
#List all pods:
crictl pods

# List pods by name
crictl pods --name nginx-65899c769f-wv2gp

# List pods by label:
crictl pods --label run=nginx

# List all images:
crictl images

# List images by repository:
crictl images nginx

# Only list image IDs:
crictl images -q

# List containers
crictl ps -a

# List running containers:
crictl ps
```

* Execute a command in a running container
```bash
crictl exec -i -t 1f73f2d81bf98 ls
```

```bash
# Get all container logs:
crictl logs 87d3992f84f74

# Get only the latest N lines of logs:
crictl logs --tail=1 87d3992f84f74
```

### Run a pod sandbox 

```bash
vim pod-config.json
{
  "metadata": {
    "name": "nginx-sandbox",
    "namespace": "default",
    "attempt": 1,
    "uid": "hdishd83djaidwnduwk28bcsb"
  },
  "log_directory": "/tmp",
  "linux": {
  }
}
```

```bash
crictl runp pod-config.json
```

### Create a container
```bash
# Pull a busybox image
crictl pull busybox

```

* Create configs for the pod and the container

```bash
vim pod-config.json
{
  "metadata": {
    "name": "busybox-sandbox",
    "namespace": "default",
    "attempt": 1,
    "uid": "aewi4aeThua7ooShohbo1phoj"
  },
  "log_directory": "/tmp",
  "linux": {
  }
}
```

```bash
vim container-config.json
{
  "metadata": {
    "name": "busybox"
  },
  "image":{
    "image": "busybox"
  },
  "command": [
    "top"
  ],
  "log_path":"busybox.log",
  "linux": {
  }
}

```

* Create the container, passing the ID of the previously-created pod, the container config file, and the pod config file. The ID of the container is returned

```bash
crictl create f84dd361f8dc51518ed291fbadd6db537b0496536c1d2d6c05ff943ce8c9a54f container-config.json pod-config.json
```

```bash
crictl ps -a

crictl start 3e025dd50a72d956c4f14881fbb5b1080c9275674e95fb67f965f6478a957d60

crictl ps
```





