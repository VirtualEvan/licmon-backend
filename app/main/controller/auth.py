from flask import Blueprint, current_app, redirect, session, url_for
from werkzeug.urls import url_encode

from app.main.core.auth import oauth


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    redirect_uri = url_for('auth.authorize', _external=True)
    return oauth.licmonqa.authorize_redirect(redirect_uri)


@auth.route('/logout')
def logout():
    session.clear()
    logout_uri = oauth.licmonqa.load_server_metadata().get('end_session_endpoint')
    query = url_encode(
        {'post_logout_redirect_uri': url_for('auth.login', _external=True)}
    )
    return redirect(logout_uri + '?' + query)


@auth.route('/authorize')
def authorize():
    token = oauth.licmonqa.authorize_access_token()
    user = oauth.licmonqa.parse_id_token(token)
    session['user'] = user
    print(user)
    return redirect('/api/servers')
