#!/bin/bash

certbot certonly --standalone --http-01-port 8080 --rsa-key-size 4096 -d $1
