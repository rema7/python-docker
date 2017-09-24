import json
from datetime import date, datetime

import falcon

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode("utf-8")
        return super(JSONEncoder, self).default(obj)


class ContentEncodingMiddleware(object):
    def process_response(self, req, resp, _, req_succeeded):
        if not req_succeeded:
            return
        if req.client_accepts_json:
            resp.set_header('Content-Type', 'application/json')
            resp.body = json.dumps(resp.body, cls=JSONEncoder)
