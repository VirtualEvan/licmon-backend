from flask import current_app
from app.main.util.lmutil import lmstat_all

# TODO: Ths is not being used
# This should be used to handle single feature requests
def get_feature_info(product_name, feature_name):
    if (server := current_app.config['LICENSE_SERVERS'].get(product_name)) is None:
        return None

    # TODO: Handle stderr
    # TODO: port and hostnames should be defined
    stdout, stderr = get_feature(
        **server,
        feature_name=feature_name
    )

    return parse_feature(product_name, stdout)

# TODO: Parse features separately
# Right now all the parsing is being made in the product service
def parse_feature(product_name, stdout):
    pass
