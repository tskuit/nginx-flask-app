#!/bin/bash

config="/etc/nginx/conf.d/flask-app.conf"
upstream="${GUNICORN_NAME:-localhost}:${GUNICORN_PORT:-8082}"
echo "Reconfigure nginx upstream in ${config} to ${upstream}."

sed -i -e "s/server localhost:8082/server ${upstream}/" \
        /etc/nginx/conf.d/flask-app.conf

echo "Remove /etc/nginx/conf.d/default.conf"
rm -f /etc/nginx/conf.d/default.conf
