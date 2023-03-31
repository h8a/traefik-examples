import os
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


class AuthHeaders:

    async def on_get(self, req, resp):
        value_header = os.getenv('CUSTOM_HEADER', 'put-some-value-custom-header')
        if req.get_header('CUSTOM-HEADER'):
            value_header = f'{ req.get_header("CUSTOM-HEADER") }, { value_header }'
        resp.set_header('CUSTOM-HEADER', value_header)
        resp.status = falcon.HTTP_200