from flask import current_app
from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer
from werkzeug.local import LocalProxy
import re


secure_serializer = LocalProxy(
    lambda: URLSafeSerializer(current_app.config['SECRET_KEY'], b'licmon')
)

secure_timed_serializer = LocalProxy(
    lambda: URLSafeTimedSerializer(current_app.config['SECRET_KEY'], b'licmon')
)

def dedent(value, *, _re=re.compile(r'^ +', re.MULTILINE)):
    """Remove leading whitespace from each line."""
    return _re.sub('', value)
