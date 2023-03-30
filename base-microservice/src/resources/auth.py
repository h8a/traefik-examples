import falcon


class Auth:

    async def on_get(self, req, resp):
        if not req.get_header('Authorization'):
            resp.status = falcon.HTTP_401
            resp.media = {
                'status': True,
                'message': 'Unauthorization'
            }
            return

        resp.status = falcon.HTTP_200
        resp.media = {
            'status': True,
            'message': 'Authorized!'
        }