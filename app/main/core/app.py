from flask import Flask
from flask_cors import CORS

from app.main.config import config_by_name
from app.main.controller.api import api
from app.main.controller.auth import auth
from app.main.core.auth import oauth
from app.main.core.limiter import limiter
from app.main.util import dedent


def _configure_app(app, from_env=True):
    app.config.from_pyfile('licmon.cfg.example')
    if from_env:
        app.config.from_envvar('LICMON_CONFIG')


def _configure_license_servers(app, from_env=True):
    # TODO: Modify to get sample data from config ?
    app.config.from_pyfile('servers.cfg.example')
    if from_env:
        app.config.from_envvar('SERVERS_CONFIG')


def _configure_auth(app):
    # TODO: Usar super para hacer client = register(...)   ???
    # Probar cómo se ven en el objeto los atributos de configuración con nombre LICMON_CLIENT_ID, LICMON_CLIENT_SECRET, etc.
    oauth.register(app.name, **app.config['OAUTH'])
    oauth.init_app(app)


def create_app(use_env_config=True):
    app = Flask('Licmon')
    limiter.init_app(app)
    CORS(app, supports_credentials=True)
    # TODO: Check this object/static configuration
    # app.config.from_object(config_by_name[config_name])
    _configure_app(app, use_env_config)
    _configure_license_servers(app)
    _configure_auth(app)
    app.add_template_filter(dedent)
    app.register_blueprint(api)
    app.register_blueprint(auth)

    return app
