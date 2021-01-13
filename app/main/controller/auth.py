from flask import (
    Blueprint,
    current_app,
    g,
    jsonify,
    redirect,
    request,
    session,
    url_for,
)
from itsdangerous import BadData, SignatureExpired
from werkzeug.urls import url_encode

from app.main.core.auth import (
    allow_anonymous,
    dummy_token,
    map_user_fields,
    oauth,
    token_from_user,
    user_from_token,
)
from app.main.schemas.user import UserSchema


auth = Blueprint('auth', __name__)


@auth.before_app_request
def require_token():
    auth = request.headers.get('Authorization', None)
    token = auth[7:] if auth and auth.startswith('Bearer ') else None
    if not token:
        function = current_app.view_functions[request.endpoint]
        if getattr(function, '_allow_anonymous', False):
            return
        return jsonify(error='token_missing'), 401
    try:
        user = user_from_token(token)
    except SignatureExpired:
        return jsonify(error='token_expired'), 401
    except BadData:
        return jsonify(error='token_invalid'), 401
    g.user = user


@auth.route('/user')
@allow_anonymous
def user():
    return UserSchema().jsonify(g.user)


@auth.route('/login')
@allow_anonymous
def login():
    if current_app.config['SKIP_LOGIN']:
        return {'error': None, 'token': dummy_token()}
    redirect_uri = url_for('auth.authorize', _external=True)
    return oauth.client.authorize_redirect(redirect_uri)


@auth.route('/authorize')
@allow_anonymous
def authorize():
    token = oauth.client.authorize_access_token()
    user = oauth.client.parse_id_token(token)
    app_user = map_user_fields(user)
    session['user'] = app_user
    return token_from_user(app_user)


@auth.route('/logout')
# TODO: Should be allowed only for logged in sessinos
@allow_anonymous
def logout():
    session.clear()
    logout_uri = oauth.client.load_server_metadata().get('end_session_endpoint')
    query = url_encode(
        {'post_logout_redirect_uri': url_for('auth.login', _external=True)}
    )
    return redirect(f'{logout_uri}?{query}')