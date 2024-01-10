from sqlalchemy.orm import Session
from app.models.sqlalchemy import BlockORM
from app.models.blockchain import Block


def get_all(db: Session) -> list[BlockORM]:
    return db.query(BlockORM).order_by(BlockORM.number.asc()).all()


def delete_all(db: Session) -> None:
    db.query(BlockORM).delete()


def create(db: Session, block: Block) -> BlockORM:
    db_block = BlockORM(
        number = block.number,
        current_hash = block.hash(),
        previous_hash = block.previous_hash,
        data = block.data,
        nonce = block.nonce
    )
    db.add(db_block)
    return db_block


