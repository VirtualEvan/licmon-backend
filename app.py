import os
from flask import Flask
from app import blueprint
from app.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

@app.route('/')
def index():
    product = 'comsol'
    command = f'sudo -u epuentes /eos/project-e/engtools/ITadmintools/licencequerytools/Flex/lmstat -a -c /afs/cern.ch/project/cad/doc/axcad/licstats/data/cvs/licenses_licmon/{product}/license.dat | cat -v'

    stdout, stderr = Popen(command, shell=True, stdout=PIPE).communicate()
    return stdout

app.run(port=5000)