from flask import Flask
from .views.adminorders import profile

def create_app(app):
    app = Flask(__name__)
    app.register_blueprint(profile)
    return create_app(app)
