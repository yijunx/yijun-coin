from app.models.user import UserInJWT
import app.services.blockchain as BlockchainService
from app.models.transaction import Transaction
import json


def send_money():
    ...


def get_balance(actor: UserInJWT) -> int:
    balance = 0
    blockchain = BlockchainService.get_blockchain()
    for block in blockchain.chain:
        transaction = Transaction(**json.loads(block.data))
        if actor.id == transaction.sender_id:
            balance -= transaction.amount_in_cents
        if actor.id == transaction.recipient_id:
            balance += transaction.amount_in_cents
    return balance
