from sqlalchemy import JSON, BigInteger, Column, DateTime, String

from app.models.sqlalchemy.base import Base


class BlockORM(Base):
    __tablename__ = "blocks"

    id = Column(BigInteger, primary_key=True, autoincrement="auto")

    number = Column(BigInteger, nullable=False)
    current_hash = Column(String, nullable=False)
    previous_hash = Column(String, nullable=False)

    data = Column(String, nullable=False)
    nonce = Column(BigInteger, nullable=False)


class UserORM(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
