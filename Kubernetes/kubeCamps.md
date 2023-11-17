# ClusterIP
```shell
kubectl run nginx --image=nginx --restart=Never --port=80 --expose

kubectl get svc nginx

kubectl run busybox --rm --image=busybox -it --restart=Never -- wget -O- nginx:80
```

# NodePort
```shell
cat <<'EOF' | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 80
    nodePort: 32000
  selector:
    run: nginx
EOF
```

```shell
kubectl get nodes -o wide # Get the Internal IP address
kubectl get svc nginx-nodeport # Get the nodePort 32000
```

```shell
TARGET=$(kubectl get nodes -o jsonpath='{.items[*].status.addresses[0].address}{"\n"}'):32000
```

```shell
TARGET=$(kubectl get nodes -o jsonpath='{.items[*].status.addresses[0].address}{"\n"}'):32000
```

```shell
curl $TARGET
```

-------------------------------------------

# The KubeCon + CloudNativeCon Special Edition Lab

Kasten’s K10 data management platform, purpose-built for Kubernetes, provides enterprise operations teams an easy-to-use, scalable, and secure system for backup and restore, disaster recovery, and mobility of Kubernetes applications.

K10’s application-centric approach and deep integrations with relational and NoSQL databases, Kubernetes distributions, and all clouds provides teams the freedom of infrastructure choice without sacrificing operational simplicity. Policy-driven and extensible, K10 provides a native Kubernetes API and includes features such full-spectrum consistency, database integrations, automatic application discovery, multi-cloud mobility, and a powerful web-based user interface.


MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace mysql mysql -o jsonpath="{.data.mysql-root-password}" | base64 --decode; echo)
kubectl exec -it --namespace=mysql $(kubectl --namespace=mysql get pods -o jsonpath='{.items[0].metadata.name}') -- mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "SHOW DATABASES LIKE 'k10demo'"

Click Create New Policy and:

Give the policy the name mysql-backup
Select Snapshot for the Action
Select Hourly for the Action Frequency
Leave the Snapshot Retention selection as-is
Select By Name for Select Applications and then, from the dropdown, select mysql
Leave all other settings as-is and select Create Policy

Causing Data Loss
MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace mysql mysql -o jsonpath="{.data.mysql-root-password}" | base64 --decode; echo)
kubectl exec -it --namespace=mysql $(kubectl --namespace=mysql get pods -o jsonpath='{.items[0].metadata.name}') -- mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "DROP DATABASE k10demo"



kubectl get --raw /apis/apps.kio.kasten.io/v1alpha1/restorepointcontents/mysql-scheduled-tmh72

MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace mysql mysql -o jsonpath="{.data.mysql-root-password}" | base64 --decode; echo)
kubectl exec -it --namespace=mysql $(kubectl --namespace=mysql get pods -o jsonpath='{.items[0].metadata.name}') -- mysql -u root --password=$MYSQL_ROOT_PASSWORD -e "SHOW DATABASES LIKE 'k10demo'"


--------------------------------
A Job creates one or more Pods and ensures that a specified number of them successfully terminate.

A DaemonSet ensures that all (or some) Nodes run a copy of a Pod.

A StatefulSet manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods.



