import json

import app.services.blockchain as BlockChainService
import app.services.transaction as TransactionService
import app.services.user as UserService
from app.models.transaction import Transaction
from app.models.user import UserInJWT


def make_user(id: int):
    return UserInJWT(id=id, name=f"tom{id}", email=f"tom{id}@tom.com")


def test_create_or_update_user():
    for i in range(3):
        UserService.create_user(user=make_user(id=i))


def test_cleanup_blockchain():
    BlockChainService.delete_blockchain()


def test_create_transaction():
    # back gives user0 100
    TransactionService.send_money(
        transaction=Transaction(sender_id=None, recipient_id=0, amount_in_cents=100)
    )

    TransactionService.send_money(
        transaction=Transaction(sender_id=0, recipient_id=1, amount_in_cents=50)
    )

    TransactionService.send_money(
        transaction=Transaction(sender_id=1, recipient_id=2, amount_in_cents=20)
    )


def test_get_chain():
    blockchain = BlockChainService.get_blockchain()
    assert blockchain.get_balance_of_a_user(user_id=0) == 50
    assert blockchain.get_balance_of_a_user(user_id=1) == 30
    assert blockchain.get_balance_of_a_user(user_id=2) == 20

    assert Transaction(**json.loads(blockchain.chain[-1].data)).sender_id == 1
