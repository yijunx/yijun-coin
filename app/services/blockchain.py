from app.utils.db import get_db
from app.models.blockchain import Blockchain, Block
import app.repositories.blockchain as BlockchainRepo


def get_blockchain() -> Blockchain:
    with get_db() as db:
        blockchain = Blockchain()
        db_blocks = BlockchainRepo.get_all(db=db)
        for db_block in db_blocks:
            blockchain.add(Block.from_orm(db_block))

    assert blockchain.isValid()
    return blockchain


def sync_blockchain(blockchain: Blockchain):
    with get_db() as db:
        BlockchainRepo.delete_all(db=db)
        for block in blockchain.chain:
            BlockchainRepo.create(db=db, block=block)


def delete_blockchain() -> None:
    with get_db() as db:
        BlockchainRepo.delete_all(db=db)

