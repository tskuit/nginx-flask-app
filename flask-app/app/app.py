from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
blax = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route('/')
def hello():
    return "App!"

@app.route('/info')
def info():
    resp = {
        'x-forwarded-host': request.headers['X-Forwarded-Host'],
        'x-forwarded-for': request.headers['X-Forwarded-For'],
        'host': request.headers['Host'],
        'user-agent': request.headers['User-Agent']
    }
    return jsonify(resp)

@app.route('/health')
def flask_health_check():
        return "success"

@app.route('/ip')
def ip():
    ip = request.remote_addr
    return ip

@app.route('/headers')
def headers():
    return jsonify(dict(request.headers))


@blax.route('/')
def index():
    return "Blax!"
