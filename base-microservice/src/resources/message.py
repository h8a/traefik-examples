import os
import falcon


class MessageResource:

    async def on_get(self, req, resp):

        # this section if, is only for example of middleware chain
        if req.get_header('CUSTOM-HEADER'):
            print(f'CUSTOM-HEADER: {req.get_header("CUSTOM-HEADER")}')

        resp.status = falcon.HTTP_200
        resp.media = {
            'status': True,
            'data': {
                'message': str(os.getenv('API_MESSAGE_RESPONSE'))
            }
        }