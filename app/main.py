# -------------------------------------------------------------------------------------------------------------
# Copyright (c) UCARE.AI Pte Ltd. All rights reserved.
# -------------------------------------------------------------------------------------------------------------

from flask import Flask, jsonify, make_response

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
