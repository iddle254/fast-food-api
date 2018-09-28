# fast-food-api/__init__.py
from flask import Flask
from .views.adminorders import adminorders
from .views.clientorders import clientorders

app = Flask(__name__)
app.register_blueprint(adminorders, url_prefix='/api/v1/orders')
app.register_blueprint(clientorders, url_prefix='/api/v1/orders')