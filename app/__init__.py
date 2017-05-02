import os
from flask import Flask
from .db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.User.controllers as User

    app.register_blueprint(User.module)

    return app
