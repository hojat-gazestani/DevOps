# Helm

```bash
helm create hello-world

hello-world /
  Chart.yaml
  values.yaml
  templates /
  charts /
  .helmignore
  
hello-world /
  templates /
    deployment.yaml
    service.yaml
    ingress.yaml
```

```shell
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "hello-world.fullname" . }}
  labels:
    app.kubernetes.io/name: {{ include "hello-world.name" . }}
    helm.sh/chart: {{ include "hello-world.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "hello-world.name" . }}
      app.kubernetes.io/instance: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app.kubernetes.io/name: {{ include "hello-world.name" . }}
        app.kubernetes.io/instance: {{ .Release.Name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: 8080
              protocol: TCP

```

```shell
apiVersion: v1
kind: Service
metadata:
  name: {{ include "hello-world.fullname" . }}
  labels:
    app.kubernetes.io/name: {{ include "hello-world.name" . }}
    helm.sh/chart: {{ include "hello-world.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: {{ include "hello-world.name" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
```

```shell
replicaCount: 1
image:
  repository: "hello-world"
  tag: "1.0"
  pullPolicy: IfNotPresent
service:
  type: NodePort
  port: 80

```

```shell
helm lint ./hello-world
helm template ./hello-world

helm install hello-world ./hello-world
helm ls --all

helm upgrade hello-world ./hello-world
helm rollback hello-world 1

helm uninstall hello-world
helm package ./hello-world

helm repo index my-repo/ --url https://<username>.github.io/my-repo
helm repo add my-repo https://my-pages.github.io/my-repo
helm install my-repo/hello-world --name=hello-world
helm search repo <KEYWORD>
```