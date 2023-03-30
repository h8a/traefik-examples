import falcon


class AuthSuccess:

    async def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = {
            'status': True,
            'message': 'Authorized!'
        }


class AuthDenied:

    async def on_get(self, req, resp):
        resp.status = falcon.HTTP_401
        resp.media = {
            'status': True,
            'message': 'Unauthorization'
        }