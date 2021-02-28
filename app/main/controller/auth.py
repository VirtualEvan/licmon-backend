from flask import (
    Blueprint,
    current_app,
    g,
    jsonify,
    redirect,
    render_template,
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


auth = Blueprint('auth', __name__, url_prefix='/auth')

# TODO: Error handler to avoid CORS when error 500
# https://stackoverflow.com/questions/29825235/getting-cors-headers-in-a-flask-500-error
# https://github.com/corydolphin/flask-cors/issues/67


@auth.before_app_request
def require_token():
    auth = request.headers.get('Authorization', None)
    token = auth[7:] if auth and auth.startswith('Bearer ') else None
    if not token:
        function = current_app.view_functions[request.endpoint]
        # TODO: Check for the method somewhere else
        if getattr(function, '_allow_anonymous', False) or request.method == 'OPTIONS':
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
def user():
    return UserSchema().jsonify(g.user)


@auth.route('/login')
@allow_anonymous
def login():
    if current_app.config['SKIP_LOGIN']:
        payload = {'error': None, 'token': dummy_token()}
        return render_template('login_response.html', payload=payload)
        # TODO: To be used when changing the login procedure
        # return {'error': None, 'token': dummy_token()}
    redirect_uri = url_for('auth.authorize', _external=True)
    return oauth.client.authorize_redirect(redirect_uri)


@auth.route('/authorize')
@allow_anonymous
def authorize():
    token = oauth.client.authorize_access_token()
    user = oauth.client.parse_id_token(token)
    app_user = map_user_fields(user)
    session['user'] = app_user
    return render_template(
        'login_response.html',
        payload={'error': None, 'token': token_from_user(app_user)},
    )


@auth.route('/logout')
@allow_anonymous
def logout():
    session.clear()
    logout_uri = oauth.client.load_server_metadata().get('end_session_endpoint')
    query = url_encode({'post_logout_redirect_uri': url_for('index', _external=True)})
    return redirect(f'{logout_uri}?{query}')
