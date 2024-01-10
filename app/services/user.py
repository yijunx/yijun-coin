import app.repositories.user as UserRepo
from app.models.user import UserInJWT
from app.utils.db import get_db


def get_user(user_id: int) -> UserInJWT:
    with get_db() as db:
        db_user = UserRepo.get_one(db=db, user_id=user_id)
        user = UserInJWT.from_orm(db_user)
    return user


def create_user(user: UserInJWT) -> UserInJWT:
    with get_db() as db:
        db_user = UserRepo.save_or_update_user(db=db, user=user)
        user = UserInJWT.from_orm(db_user)
    return user
