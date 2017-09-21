
class RestResource:
    def on_get(self, _, resp):
        resp.body = {
            'name': 'TestName',
            'result': 'Result',
        }
