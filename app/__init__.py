from flask import Flask

from app import routes
from app.configs import database, env_config, jwt_auth, migration, mail


def create_app():
    app = Flask(__name__)

    mail.init_app(app)
    env_config.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt_auth.init_app(app)
    routes.init_app(app)

    return app
