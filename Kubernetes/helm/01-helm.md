# Helm

# Concept

- **chart:**  **collection** of files organized in a specific directory structure
  - The configuration information related to a chart is managed **in the configuration**
- **release:** running instance of a chart with a specific config
  - Helm tracks an installed chart in the Kubernetes cluster using releases.
  - allows us to install a single chart multiple times with different releases in a cluster.
- **library charts:** **enable support** for common charts that we can use to define chart **primitives or definitions**.
- we can share charts as archives through repositories.  Artifact Hub

# Install Helm on Ubuntu 22.04
```bash
wget https://get.helm.sh/helm-v3.8.2-linux-amd64.tar.gz
tar xvf helm-*-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin
helm version
```
```bash
helm install mysql oci://registry-1.docker.io/bitnamicharts/mysql

kubectl get all
NAME          READY   STATUS    RESTARTS   AGE
pod/mysql-0   0/1     Pending   0          2m5s

helm list

NAME                     TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
service/kubernetes       ClusterIP   10.233.0.1    <none>        443/TCP    39m
service/mysql            ClusterIP   10.233.8.77   <none>        3306/TCP   2m5s
service/mysql-headless   ClusterIP   None          <none>        3306/TCP   2m5s

NAME                     READY   AGE
statefulset.apps/mysql   0/1     2m5s
```

# 03- How to find heml chart


# 04- how to install promethous and graphana
```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm repo list
helm install prometheus prometheus-community/prometheus

kubectl edit svc prometheus
	ports:
	- name: service
	port:80
	protocol: TCP
	targetPort: 3000
	nodePort: 30001
	
  type: NodePort
```
## 05- Working
```shell
helm show values prometheus-community/prometheus > values.yaml
vim values.yaml
adminpassword: arman

heml upgrade prometheus prometheus-community/prometheus --set grafana.adminPassword=admin
```

# 06- How to override values.yaml
```bash
heml upgrade prometheus prometheus-community/prometheus --set grafana.adminPassword=admin grafana.service.type=NodePort 

vim values.yaml
grafana:
	adminPassword: admin
	service:
		portName: service
		type: NodePort
		nodePort: 30008
		
heml upgrade prometheus prometheus-community/prometheus  --values=values.yaml
```

# 07- Avoiding Snowflake Clusters

```bash
never use helm install <remote>
```

# 08- Using helm pull

```bash
kebectl get pod

helm list
helm uninstall monitoring
helm uninstall mysql

mkdir my_cluster_config && cd my_cluster_config
helm repo add stable https://charts.helm.sh/stable
helm pull stable/mysql
ls 

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

helm pull bitnami/mysql --untar
cd mysql
vim values.yaml

cd ..
helm install mysql ./mysql
```

```bash
helm pull bitnami/prometheus --untar
cd prometheus/
grafana:
	adminPassword: admin
	service:
		portName: service
		type: NodePort
		nodePort: 30008
```

+ better method

```bash
vim myvalues.yaml
grafana:
	adminPassword: admin
	service:
		portName: service
		type: NodePort
		nodePort: 30008
	
helm upgrade prometheus --values=myvalues.yaml .
```

# 09- Create yaml from a Helm Chart

```bash
helm template monitoring ./prometheus --values=./prometheus/values.yaml > monitoring-stack.yaml
```

# 10- Why make your own charts

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: 1
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: richardchesterwood/k8s-fleetman-helm-demo:v1.0.0
---
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
```

# 11- Creating a Chart - writing Go templates

```bash
cd prometheus/
helm create fleetman-helm-chart && cd fleetman-helm-chart/ && tree fleetman-helm-chart
```
- **Chart.yaml:** **main file** that contains the **description of our chart**
- **values.yaml:** Contains the **default values** for our **chart**
- **templates:** the directory where **Kubernetes resources** are defined as templates
- **charts:**  optional directory that may contain **sub-charts**
- **.helmignore:** where we can define patterns to **ignore when packaging**

```shell
vim Chart.yaml
 apiVersion: v2
name: fleetman-helm-chart
description: A Helm chart for Kubernetes

type: application

version: 0.1.0

appVersion: "1.1.0"

ls templates/
deployment.yaml  _helpers.tpl  hpa.yaml  ingress.yaml  NOTES.txt  serviceaccount.yaml  service.yaml  tests
rm -rf templates/*
ls templates/

vim templates/one.yaml
hello:
  world: true
  
rm values.yaml
touch  values.yaml

ls
charts  Chart.yaml  templates  values.yaml

helm template .
---
# Source: fleetman-helm-chart/templates/one.yaml
hello:
  world: true
``` 
 
```bash
vim templates/two.yaml 
something:
  not:
    - insteresting
    - useful
```

```bash    
helm template .
---
# Source: fleetman-helm-chart/templates/one.yaml
hello:
  world: true
---
# Source: fleetman-helm-chart/templates/two.yaml
something:
  not:
    - insteresting
    - useful
```

```bash    
vim templates/one.yaml 
hello:
  world: {{ printf "true" }}
  
helm template .
---
# Source: fleetman-helm-chart/templates/one.yaml
hello:
  world: true
---
# Source: fleetman-helm-chart/templates/two.yaml
something:
  not:
    - insteresting
    - useful
```

```bash
rm -rf templates/*

vim templates/fleetman-full.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: 1
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: richardchesterwood/k8s-fleetman-helm-demo:v1.0.0
---
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
```

```bash
helm template .
---
# Source: fleetman-helm-chart/templates/fleetman-full.yaml
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
---
# Source: fleetman-helm-chart/templates/fleetman-full.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: 1
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: richardchesterwood/k8s-fleetman-helm-demo:v1.0.0
```


```bash
vim values.yaml
webapp:
  numberOfWebAppReplicas: 4

vim templates/fleetman-full.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: {{ .Values.webapp.numberOfWebAppReplicas }}
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: richardchesterwood/k8s-fleetman-helm-demo:v1.0.0
---
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
```

```bash
helm template .
---
# Source: fleetman-helm-chart/templates/fleetman-full.yaml
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
---
# Source: fleetman-helm-chart/templates/fleetman-full.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: 4
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: richardchesterwood/k8s-fleetman-helm-demo:v1.0.0
```

```bash
helm template . --set webapp.numberOfWebAppReplicas=127
```

# 12- Function and Pipline

```bash
vim templates/fleetman-full.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: {{ .Values.webapp.numberOfWebAppReplicas }}
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: {{ .Values.dockerRepoName }}/k8s-fleetman-helm-demo:v1.0.0
---
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
```

```bash
vim values.yaml
dockerRepoName: richardchesterwood
```

# 13- Template flow control

```bash
vim values.yaml

# "prod" or "dev"
environment: prod

```

```bash
vim templates/fleetman-full.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: {{ .Values.webapp.numberOfWebAppReplicas }}
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: {{ .Values.dockerRepoName }}/k8s-fleetman-helm-demo:v1.0.0-{{ if eq .Values.environment "dev" }}-dev{{ end }}
---
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
```

# OR

```bash
vim values.yaml
development: true
```

```bash
vim templates/fleetman-full.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: {{ .Values.webapp.numberOfWebAppReplicas }}
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: {{ .Values.dockerRepoName }}/k8s-fleetman-helm-demo:v1.0.0-{{ if eq .Values.develpment true }}-dev{{ end }}
---
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
```

# OR

```bash
vim values.yaml
development: true

```

```bash
vim templates/fleetman-full.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: {{ .Values.webapp.numberOfWebAppReplicas }}
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        # Note to deployer - add -dev at the end of here for development version
        image: {{ .Values.dockerRepoName }}/k8s-fleetman-helm-demo:v1.0.0-{{ if .Values.develpment }}-dev{{ else }}-prod{{ end }}
---
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
```

# 14- Named Templates - partial - subtemplate

```bash
vim templates/_common-blocks.tpl
{{- define "webappImage" }}
- name: webapp
  image: {{ .Values.dockerRepoName }}/k8s-fleetman-helm-demo:v1.0.0-{{ if .Values.develpment }}-dev{{ else }}-prod{{ end }}
{{- end }}

```

```bash
vim templates/fleetman-full.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: {{ .Values.webapp.numberOfWebAppReplicas }}
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        # we need to substitute some yaml here.
		# template OR include
		{{- include "webappImage" . | indent 6 }}
		
---
apiVersion: v1
kind: Service
metadata:
  name: fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: 30080

  type: NodePort
```

# 15- Professional helm Charts

```bash
helm install my-fleetman-release .  --set development=true

kubectl get all

vim values.yaml
webapp:
  numberOfWebAppReplicas: 4
  
helm upgrade my-fleetman-release .  --set development=false
```

```bash
vim values.yaml
webapp:
  numberOfWebAppReplicas: 1
  nodePort: 30080
  
dockerReopName: richardchesterwood
 
development: true

vim templates/fleetman-full.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-webapp
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: {{ .Values.webapp.numberOfWebAppReplicas }}
  template: # template for the pods
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        # we need to substitute some yaml here.
		# template OR include
		{{- include "webappImage" . | indent 6 }}
		
---
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-fleetman-webapp

spec:
  selector:
    app: webapp

  ports:
    - name: http
      port: 80
      nodePort: {{ .Values.webapp.nodePort  }}

  type: NodePort
```

