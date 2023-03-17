from flask import Flask
import secrets

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(5)

    from project.routes import views

    app.register_blueprint(views)

    return app