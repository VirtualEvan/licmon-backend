import uuid
import datetime

from app.main.model.product import Product
from subprocess import Popen, PIPE

def get_product(product_name):
    command = f'sudo -u epuentes /eos/project-e/engtools/ITadmintools/licencequerytools/Flex/lmstat -a -c /afs/cern.ch/project/cad/doc/axcad/licstats/data/cvs/licenses_licmon/{product_name}/license.dat | cat -v'

    stdout, stderr = Popen(command, shell=True, stdout=PIPE).communicate()

    product = Product("test")

    return product