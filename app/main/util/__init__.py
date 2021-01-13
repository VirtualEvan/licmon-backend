from flask import current_app
from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer
from werkzeug.local import LocalProxy


secure_serializer = LocalProxy(
    lambda: URLSafeSerializer(current_app.config['SECRET_KEY'], b'licmon')
)

secure_timed_serializer = LocalProxy(
    lambda: URLSafeTimedSerializer(current_app.config['SECRET_KEY'], b'licmon')
)
