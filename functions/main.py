from firebase_functions import https_fn
from firebase_admin import initialize_app
from agent_app.main import app
from a2wsgi import ASGIMiddleware
import werkzeug.wrappers

initialize_app()

wsgi_app = ASGIMiddleware(app)

@https_fn.on_request(max_instances=10)
def api(req: https_fn.Request) -> https_fn.Response:
    return werkzeug.wrappers.Response.from_app(wsgi_app, req.environ)
