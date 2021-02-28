import uuid
from subprocess import PIPE, Popen

from flask import current_app


def get_all_features(port, hostnames):
    return lmstat(f'-c {port}@{",".join(hostnames)} -a')


def get_feature(port, hostnames, feature_name):
    return lmstat(f'-c {port}@{",".join(hostnames)} -f {feature_name}')


# TODO: Sanitize input
def lmstat(parameters):
    command = f'{current_app.config["LMUTIL_PATH"]} lmstat {parameters}'
    stdout, stderr = Popen(command, shell=True, stdout=PIPE).communicate()

    return stdout, stderr
