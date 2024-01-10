import json
import re
from logging import getLogger
from typing import Iterable

import jwt
from flask import Flask
from werkzeug.wrappers import Request, Response

from app.models.user import UserInJWT
from app.utils.db import get_db as session_scope

logger = getLogger(__name__)


class AuthMiddleware:
    """
    Authorization WSGI middleware
    """

    def __init__(self, app: Flask):
        self.app = app.wsgi_app
        app.wsgi_app = self

    def __call__(self, environ, start_response) -> Iterable[bytes]:
        request = Request(environ)

        if (
            request.path.startswith(("/internal", "/docs"))
            or request.method == "OPTIONS"
        ):
            return self.app(environ, start_response)

        token: str = request.cookies.get("token", None)

        if token is None:
            try:
                authorization = request.headers["authorization"]
            except KeyError:
                logger.warning("no athorization header provided")
                return self.unauth(environ, start_response)
            m = re.match(r"bearer (.+)", authorization, re.IGNORECASE)
            if m is None:
                logger.warning("invalid authorization type")
                return self.unauth(environ, start_response)
            token = m.group(1)

        try:
            # well here we dont verify signature just for test purpose
            actor = UserInJWT(**jwt.decode(token, options={"verify_signature": False}))
        except Exception as e:
            logger.warning(f"error in authentication: {e}")
            return self.unauth(environ, start_response)

        environ["actor"] = actor

        # try:
        #     UsersRepository.save_or_update_tpa_user_from_token(
        # except Exception as e:
        #     logger.error(e, exc_info=True)

        return self.app(environ, start_response)

    @staticmethod
    def unauth(environ, start_response):
        json_resp = json.dumps(
            {"code": 4, "response": None, "message": "Authorization failed"}
        )
        return Response(json_resp, mimetype="application/json", status=401)(
            environ, start_response
        )
