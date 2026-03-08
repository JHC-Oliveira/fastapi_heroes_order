from fastapi import APIRouter, Depends
from app.models.db_models import User
from app.dependencies.database import get_session
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    This route is the authentification route
    """
    return {"message": "You are in Auth", "authentification": False}

@auth_router.post("/create_account")
async def create_account(email: str, password: str, name: str, session = Depends(get_session)):
    user = session.query(User).filter(User.email == email).first()     #type:ignore
    if user:
        return{"message": "user already exists"}
    else:
        new_user = User(name, email, password)
        session.add(new_user)
        session.commit()
        return{"message": "user created"}