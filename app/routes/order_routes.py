from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def orders():
    """
    This route show every order in our application, every order needs an authentification
    """
    
    return {"message": "You are in order page"}