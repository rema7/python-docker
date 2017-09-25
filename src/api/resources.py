from datetime import datetime

class RestResource:
    def on_get(self, _, resp):
        resp.body = {
            'result': 'Wow! Resul!:)',
            'timestamp': datetime.utcnow(),
        }
