# -------------------------------------------------------------------------------------------------------------
# Copyright (c) UCARE.AI Pte Ltd. All rights reserved.
# -------------------------------------------------------------------------------------------------------------

from logging import getLogger

from flask import Flask, Response, jsonify, make_response
from flask_pydantic.core import make_json_response

from app.apis.blockchain import bp as blockchain_bp
from app.middleware.auth import AuthMiddleware
from app.utils.config import configurations


def create_app():
    app = Flask(__name__)

    # auth
    AuthMiddleware(app=app)

    # blueprints
    app.register_blueprint(blueprint=blockchain_bp)

    return app


app = create_app()


## -- errorhandler -- ##
@app.after_request
def modify_validation_error(response: Response):
    if (
        response.status_code == 400
        and response.is_json
        and "validation_error" in response.json
    ):
        errmsg = "validation error:"
        for where, errors in response.json["validation_error"].items():
            for error in errors:
                loc = error.get("loc", "")
                msg = error.get("msg") or error.get("type")
                errmsg += f"\n{where}{loc}: {msg}"

        return make_response(jsonify({"msg": errmsg}), 400)
    return response


@app.errorhandler(500)
def internal_server_error(err):
    getLogger(__file__).error(err, exc_info=True)
    return make_response(jsonify({"msg": "internal server error"}), 500)
