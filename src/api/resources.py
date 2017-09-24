
class RestResource:
    def on_get(self, _, resp):
        resp.body = {
            'result': 'Test rest method',
        }
