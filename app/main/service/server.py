from flask import current_app

from app.main.model.server import Server

def get_servers_info():
    servers = [
        Server(key, **value)
        for (key, value) in current_app.config['LICENSE_SERVERS'].items()
    ]
    return servers
