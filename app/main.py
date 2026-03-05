from fastapi import FastAPI

app = FastAPI()

from app.routes.auth_routes import auth_router  # noqa: E402
from app.routes.order_routes import order_router  # noqa: E402

app.include_router(auth_router)
app.include_router(order_router)








#to run the application: uvicorn app.main:app --reload