import json
from datetime import date, datetime

import falcon

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode("utf-8")
        if isinstance(obj, date, datetime):
            return str(obj.isoformat())
        return super(JSONEncoder, self).default(obj)


class ContentEncodingMiddleware(object):
    def process_response(self, req, resp, resource, req_succeeded):
        if not req_succeeded:
            return
        if req.client_accepts_json:
            resp.set_header('Content-Type', 'application/json')
            resp.body = json.dumps(resp.body, cls=JSONEncoder)

    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
        try:
            req.context['body'] = json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')
