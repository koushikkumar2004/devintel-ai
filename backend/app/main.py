from fastapi import FastAPI
from app.database import engine, Base
from app.models import user
from app.routes.user_routes import router as user_router
from app.routes.ai_routes import router as ai_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(ai_router)

@app.get("/")
def root():
    return {"message": "DevIntel AI Backend Running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}