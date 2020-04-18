#!/usr/bin/env bash

openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes -keyout incog.key -out incog.crt -subj "/CN=localhost"
