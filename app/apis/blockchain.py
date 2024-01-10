from flask import Blueprint, Response, request
from logging import getLogger
import app.services.blockchain as BlockchainService

bp = Blueprint("claims_bp", __name__, url_prefix="/apis/yijun-coin/blockchain")
logger = getLogger(__name__)

@bp.route("/", methods=["GET"])
def get_chain():
    actor = request.environ["actor"]
    print(f"{actor=}")
    return BlockchainService.get_blockchain().dict()
