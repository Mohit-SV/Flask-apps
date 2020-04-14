from flask import Flask
from .routes import simple_page

test_blueprint = Flask(__name__)
test_blueprint.register_blueprint(simple_page)

from test_blueprint import routes