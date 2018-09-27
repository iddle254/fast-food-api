from flask import Flask
from .views.adminorders import profile

def create_app(config_name):	
    app = Flask(__name__)
    app.register_blueprint(profile)
    @app.errorhandler(404)
    def pageNotFound(e):
        return "Page not found. Please check to see if you entered the correct address"

    @app.errorhandler(405)
    def methodNotAllowed(e):
	    return "Method not allowed. Please use the correct method"

    @app.errorhandler(500)
    def methodNotAllowed(e):
	    return "oops.. There is a problem on our part. Please wait as we try to fix it"
    return app
