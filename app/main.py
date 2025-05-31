from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import userRoutes, tweetRoutes, loginRoute


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(loginRoute.router)
app.include_router(userRoutes.router)
app.include_router(tweetRoutes.router)


