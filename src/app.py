import falcon

from api.resources import (
    RestResource,
)
from middlewares import (
    ContentEncodingMiddleware,
)

app = falcon.API(middleware=[
    ContentEncodingMiddleware(),
])

app.add_route('/rest', RestResource())