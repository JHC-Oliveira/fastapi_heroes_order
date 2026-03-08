from fastapi import APIRouter
from app.models.database import User, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    This route is the authentification route
    """
    return {"message": "You are in Auth", "authentification": False}

@auth_router.post("/create_account")
async def create_account(email: str, password: str, name: str):
    """
        problems:
        1- session opened but if there is any error until the end, it will still be opened
        2- no pattern for message, should be returning 200, 404 ....
        3- no pattern for parameters, passing 3 variables, it will be cleaner if I pass a class instead 
    """
    Session = sessionmaker(bind=db)
    session = Session()
    user = session.query(User).filter(User.email == email).first()     #type:ignore
    if user:
        return{"message": "user already exists"}
    else:
        new_user = User(name, email, password)
        session.add(new_user)
        session.commit()
        return{"message": "user created"}