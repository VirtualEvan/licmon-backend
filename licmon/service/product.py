import datetime
import re

from flask import current_app

from licmon.model.feature import Feature
from licmon.model.license import License
from licmon.model.product import Product
from licmon.util.lmutil import get_all_features


def get_product_info(product_name):
    if (server := current_app.config['LICENSE_SERVERS'].get(product_name)) is None:
        return None

    # TODO: Handle stderr
    # TODO: port and hostnames should be defined
    stdout, stderr = get_all_features(**server)

    return parse_product(product_name, stdout)


def parse_product(product_name, stdout):
    product = Product(product_name)
    product.raw = stdout
    current_feature = None

    # Users of PERMANENT:  (Uncounted, node-locked)
    regex_uncounted_feature = re.compile('Users of (.*?):  \(Uncounted, node-locked\)')

    # Users of COMSOLUSER:  (Total of 28 licenses issued;  Total of 18 licenses in use)
    regex_feature = re.compile(
        'Users of (.*?):  \(Total of (\d+) licenses? issued;  Total of (\d+) licenses? in use\)'
    )

    # "COMSOLUSER" v5.5, vendor: LMCOMSOL
    regex_feature_details = re.compile('\"(.*)\" v(\d+\.\d+), vendor: (.*)')

    # opsepu vmapp002 EVAN-PC (v1.0) (lxlicen14a/27005 24757), start Wed 4/8 10:55, 212 licenses
    regex_license = re.compile(
        '(\w+) (.*) (.*) (?:\(v(.*)\))? \((.*)\/(\d+) (\d+)\), start (\w+ \d+\/\d+ \d+\:\d+)(?:, (\d+) licenses)?'
    )

    # Users of visualhdlpro_c:  (Error: 5 licenses, unsupported by licensed server)
    regex_error_unsupported = re.compile(
        'Users of (\S+):\s*\(Error: (\d+) licenses, (unsupported by licensed server)\)'
    )

    # lmgrd is not running: License server machine is down or not responding.
    regex_error_down = re.compile(
        'lmgrd is not running: License server machine is down or not responding.'
    )

    # TODO: Handle this error
    # Error getting status: Cannot connect to license server system. (-15,570:36 "Operation now in progress")
    # regex_error_connection = re.compile(
    #     'Error getting status: Cannot connect to license server system. (-15,570:36 "Operation now in progress")'
    # )

    for line in str(stdout).split(r'\n'):

        # TODO: Refactorize this, so it does not doublecheck
        if regex_uncounted_feature.search(line):
            matches = regex_uncounted_feature.search(line)
            feature = Feature(name=matches.group(1))

            # Add the previous feature
            if current_feature is not None:
                product.add_feature(current_feature)
            current_feature = feature

        elif regex_feature.search(line):
            matches = regex_feature.search(line)
            feature = Feature(
                name=matches.group(1),
                licenses_issued=matches.group(2),
                licenses_in_use=matches.group(3),
            )

            # Add the previous feature
            if current_feature is not None:
                product.add_feature(current_feature)
            current_feature = feature

        # TODO: Check if this is relevant to know
        # elif regex_feature_details.search(line):
        #     matches = regex_feature_details.search(line)
        #     current_feature.version = matches.group(2)
        #     current_feature.vendor = matches.group(3)

        elif regex_license.search(line):
            matches = regex_license.search(line)
            license = License(
                username=matches.group(1),
                hostname=matches.group(2),
                display=matches.group(3),
                version=matches.group(4),
                server=matches.group(5),
                port=matches.group(6),
                handle=matches.group(7),
                checkout=matches.group(8),
                num_licenses=matches.group(9),
            )
            current_feature.add_license(license)

        elif regex_error_unsupported.search(line):
            matches = regex_error_unsupported.search(line)

            feature = Feature(
                name=matches.group(1),
                licenses_issued=matches.group(2),
                message=matches.group(3),
            )

            # Add the previous feature
            if current_feature is not None:
                product.add_feature(current_feature)
            current_feature = feature

        # TODO: Imporve error handling returning a more specific error code
        elif regex_error_down.search(line):
            matches = regex_error_down.search(line)
            return

        # TODO: Handle this error
        # elif regex_error_connection.search(line):
        #     matches = regex_error_connection.search(line)
        #     return

    # Add the last feature
    if current_feature is not None:
        product.add_feature(current_feature)

    return product
