from flask import Flask
from app import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)
app.app_context().push()

@app.route('/')
def index():
    product = 'comsol'
    command = f'sudo -u epuentes /eos/project-e/engtools/ITadmintools/licencequerytools/Flex/lmstat -a -c /afs/cern.ch/project/cad/doc/axcad/licstats/data/cvs/licenses_licmon/{product}/license.dat | cat -v'

    stdout, stderr = Popen(command, shell=True, stdout=PIPE).communicate()
    return stdout

app.run(port=5000)