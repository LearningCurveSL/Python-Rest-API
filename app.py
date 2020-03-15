import connexion
from connexion.resolver import RestyResolver
from flask_injector import FlaskInjector
from injector import Binder

from provider.userprovider import userProvider

def configure(binder: Binder) -> Binder:
    binder.bind(userProvider, userProvider())
    return binder


def create_app():
    #service = 'registration'
    port = 8900
    app = connexion.App(__name__, port=port, specification_dir='swagger/')

    app.add_api('user.yaml', resolver=RestyResolver('services.login'))
    return app, port


g_app, g_port = create_app()
FlaskInjector(app=g_app.app, modules=[configure])
application = g_app.app
application.debug = True

if __name__ == "__main__":
    application.run(port=g_port, host="0.0.0.0")
