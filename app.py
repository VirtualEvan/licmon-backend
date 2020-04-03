from flask import Flask
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/')
def index():
    product = 'comsol'
    command = f'sudo -u epuentes /eos/project-e/engtools/ITadmintools/licencequerytools/Flex/lmstat -a -c /afs/cern.ch/project/cad/doc/axcad/licstats/data/cvs/licenses_licmon/{product}/license.dat | cat -v'

    stdout, stderr = Popen(command, shell=True, stdout=PIPE).communicate()
    return stdout

app.run(port=5000)