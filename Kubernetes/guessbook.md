






```shell
cd /home/project
[ ! -d 'guestbook' ] && git clone https://github.com/ibm-developer-skills-network/guestbook
￼cd v1/guestbook
export MY_NAMESPACE=sn-labs-$USERNAME
￼echo $MY_NAMESPACE
```

```shell
vim Dockerfile
FROM golang as builder
RUN go get github.com/codegangsta/negroni
RUN go get github.com/gorilla/mux github.com/xyproto/simpleredis
COPY main.go .
RUN go build main.go

FROM busybox:ubuntu-14.04

COPY --from=builder /go//main /app/guestbook

ADD public/index.html /app/public/index.html
ADD public/script.js /app/public/script.js
ADD public/style.css /app/public/style.css
ADD public/jquery.min.js /app/public/jquery.min.js

WORKDIR /app
CMD ["./guestbook"]
EXPOSE 3000
```

```shell
docker push us.icr.io/$MY_NAMESPACE/guestbook:v1

```

```shell
kubectl run -i --tty load-generator --rm --image=busybox:1.36.0 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- <your app URL>; done"
￼

```