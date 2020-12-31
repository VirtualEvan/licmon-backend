from flask import Flask

from .config import config_by_name


def _load_configuration(app, from_env=True):
    app.config.from_pyfile('licmon.cfg.example')
    if from_env:
        app.config.from_envvar('LICMON_CONFIG')


def _load_license_servers(app, from_env=True):
    # TODO: Modify to get sample data from config ?
    app.config.from_pyfile('servers.cfg.example')
    if from_env:
        app.config.from_envvar('SERVERS_CONFIG')


# def create_app(config_name):
def create_app(app_name, use_env_config=True):
    app = Flask(app_name)
    # TODO: Check this object/static configuration
    # app.config.from_object(config_by_name[config_name])
    _load_configuration(app, use_env_config)
    _load_license_servers(app)
    return app
