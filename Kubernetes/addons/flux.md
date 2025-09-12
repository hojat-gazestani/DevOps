

```bash
export GITLAB_TOKEN=<Your-Token>
```





My Gitlab container is running on docker container bind 2222 host port to 22 container:

```bash
flux bootstrap git \
  --url=http://git.zaraamad.ir/test/argocd.git \
  --branch=voting-app \
  --path=clusters/testing \
  --username=git \
  --password=$GITLAB_TOKEN \
  --allow-insecure-http=true \
  --ssh-hostname=git.zaraamad.ir:2222
```

