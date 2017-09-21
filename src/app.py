import falcon

from api.resources import (
    RestResource,
)

app = falcon.API()

app.add_route('/rest', RestResource())