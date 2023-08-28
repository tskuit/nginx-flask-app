## how to start
```
docker-compose build
docker-compose up
```

## accepted environment variables
If you change gunicorn port you have to manually edit nginx configuration file, 8082 is hardcoded there.
```
GUNICORN_APP="${GUNICORN_APP:-app:app}"
GUNICORN_HOST="${GUNICORN_HOST:-127.0.0.1}"
GUNICORN_PORT="${GUNICORN_PORT:-8082}"
GUNICORN_WORKERS="${GUNICORN_WORKERS:-5}"
```

## useful blogs
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

## gunicorn
https://docs.gunicorn.org/en/stable/index.html

## flask
# deployment (nginx, gunicorn, others)
https://flask.palletsprojects.com/en/2.3.x/deploying/
# gunicorn
https://flask.palletsprojects.com/en/2.3.x/deploying/gunicorn/
# proxy fix
https://werkzeug.palletsprojects.com/en/2.3.x/middleware/proxy_fix/
