

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

activate_this = '/home/username/huskypantry/venv/public_html/husky_pantry/3.11/bin/activate_this.py'
with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from run import app as application
