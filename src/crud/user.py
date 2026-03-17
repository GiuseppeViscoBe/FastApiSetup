from sqlalchemy.orm import Session

from src.models.user import User
from src.schemas.user import UserCreate


def get_users(db: Session) -> list[User]:
    return db.query(User).order_by(User.id.asc()).all()


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(
        name=user_in.name,
        email=user_in.email,
        age=user_in.age,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user