from flask import Blueprint, Response, request

bp = Blueprint("claims_bp", __name__, url_prefix="/apis/yijun-coin/coins")


@bp.route("/", methods=["GET"])
def get_coins():
    return {"hey": "world"}
