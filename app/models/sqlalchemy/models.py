from sqlalchemy import JSON, BigInteger, Column, DateTime, String

from app.models.sqlalchemy.base import Base


class Block(Base):
    __tablename__ = "blocks"

    id = Column(BigInteger, primary_key=True, autoincrement="auto")

    number = Column(BigInteger, nullable=False)
    current_hash = Column(String, nullable=False)
    previous_hash = Column(String, nullable=False)

    data = Column(String, nullable=False)
    nonce = Column(BigInteger, nullable=False)
