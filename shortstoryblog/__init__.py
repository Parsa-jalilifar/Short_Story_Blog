from flask import Flask
from shortstoryblog.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from shortstoryblog.main.routes import main
    from shortstoryblog.users.routes import users
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
