from fastapi import FastAPI
from app.config.database import Base, engine
from app.routes.auth import auth_router
from app.routes.users import users_router
from fastapi.responses import FileResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])

# Serve static HTML file
@app.get("/", response_class=FileResponse)
def read_root():
    return "app/static/index.html"
