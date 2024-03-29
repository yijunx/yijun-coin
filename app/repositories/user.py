from sqlalchemy.orm import Session

from app.models.exception import CustomException
from app.models.sqlalchemy import UserORM
from app.models.user import UserInJWT


def save_or_update_user(db: Session, user: UserInJWT):
    db_user: UserORM = db.query(UserORM).filter(UserORM.id == user.id).first()

    if db_user:
        db_user.name = user.name
        db_user.email = user.email

    else:
        db_user = UserORM(id=user.id, name=user.name, email=user.email)
        db.add(db_user)
        db.flush()
    return db_user


def get_one(db: Session, user_id: int):
    db_user: UserORM = db.query(UserORM).filter(UserORM.id == user_id).first()
    if db_user:
        return db_user
    else:
        raise CustomException(http_code=404, message="User does not exist")
