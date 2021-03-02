from flask import Flask

from licmon.config import config_by_name
from licmon.controller.api import api
from licmon.controller.auth import auth
from licmon.core.auth import oauth
from licmon.core.limiter import limiter
from licmon.util import dedent


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
    oauth.register(app.name, **app.config['OAUTH'])
    oauth.init_app(app)


def create_app(use_env_config=True):
    app = Flask('Licmon')
    limiter.init_app(app)
    # TODO: Check this object/static configuration
    # app.config.from_object(config_by_name[config_name])
    _configure_app(app, use_env_config)
    _configure_license_servers(app)
    _configure_auth(app)
    app.add_template_filter(dedent)
    app.register_blueprint(api)
    app.register_blueprint(auth)
    app.add_url_rule('/', 'index', build_only=True)

    return app
