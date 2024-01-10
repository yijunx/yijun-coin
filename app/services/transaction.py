import app.services.blockchain as BlockchainService
import app.services.user as UserService
from app.models.blockchain import Block
from app.models.exception import CustomException
from app.models.transaction import Transaction


def send_money(transaction: Transaction) -> Block:
    blockchain = BlockchainService.get_blockchain()
    if transaction.sender_id:
        sender_balance = blockchain.get_balance_of_a_user(user_id=transaction.sender_id)
        if transaction.amount_in_cents > sender_balance:
            raise CustomException(http_code=400, message="Insufficent Funds")
    else:
        # sender is bank
        pass

    if transaction.recipient_id:
        # need to make sure user exsits
        _ = UserService.get_user(user_id=transaction.recipient_id)
    else:
        # recipient is back
        pass

    # ok now everything is nice, time to add it into chain
    number = len(blockchain.chain)
    data = transaction.json()
    blockchain.mine(block=Block(number=number, data=data))
    BlockchainService.sync_blockchain(blockchain=blockchain)

    return blockchain.chain[-1]
