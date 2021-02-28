from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


limiter = Limiter(
    key_func=get_remote_address, headers_enabled=True, retry_after='http-date'
)
