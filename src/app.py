from flask import Flask
from . import routes_and_views


def create_app() -> Flask:
    app = Flask(__name__)
    routes_and_views.init_app(app)

    return app


# scripts baseados na resolução de Roberval Filho:
# https://github.com/tryber/sd-012-project-job-insights/pull/28/files