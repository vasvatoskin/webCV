from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.models import *

db.init_app(app)