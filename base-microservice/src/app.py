import falcon.asgi

from resources.auth import AuthDenied, AuthSuccess
from resources.message import MessageResource

class Service(falcon.asgi.App):

    def __init__(self, *args, **kwargs) -> None:
        super(Service, self).__init__()

        self.add_route('/api/v1.0.0/messages', MessageResource())
        self.add_route('/api/v1.0.0/auth/denied', AuthDenied())
        self.add_route('/api/v1.0.0/auth/success', AuthSuccess())