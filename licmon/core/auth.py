from authlib.integrations.flask_client import OAuth
from flask import current_app

from licmon.util import secure_timed_serializer


class _LicmonOAuth(OAuth):
    def register(self, name, overwrite=False, **kwargs):
        self._client = super().register(name, overwrite, **kwargs)

    @property
    def client(self):
        return self._client


oauth = _LicmonOAuth()


def iteritems(arg, **kwargs):
    return iter(arg.items(**kwargs))


def map_user_fields(oauth_user):
    return {
        key: oauth_user.get(value, None)
        for key, value in iteritems(current_app.config['OAUTH_MAPPING'])
    }


def dummy_token():
    return secure_timed_serializer.dumps(
        {
            'username': 'dummy',
            'email': 'example@example.com',
            'name': 'Dummy User',
            'roles': ['default-role', 'licmon-admins'],
            'uid': 0,
        },
        salt='app-token',
    )


def token_from_user(user):
    return secure_timed_serializer.dumps(user, salt='app-token')


def user_from_token(token):
    return secure_timed_serializer.loads(
        token, salt='app-token', max_age=current_app.config['TOKEN_LIFETIME']
    )


def allow_anonymous(function):
    function._allow_anonymous = True
    return function
