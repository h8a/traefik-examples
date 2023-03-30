import os
import falcon


class MessageResource:

    async def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = {
            'status': True,
            'data': {
                'message': str(os.getenv('API_MESSAGE_RESPONSE'))
            }
        }