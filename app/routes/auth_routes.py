from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth():
    """
    This route is the authentification route
    """
    return {"message": "You are in Auth", "authentification": False}