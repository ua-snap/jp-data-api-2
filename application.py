from datetime import datetime
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from marshmallow import Schema, fields, validate
import re

from routes import routes, request

# Elastic Beanstalk wants `application` to be present.
application = app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)
