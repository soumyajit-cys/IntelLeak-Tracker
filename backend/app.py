from fastapi import FastAPI
from routes import keywords, alerts, breach
from services.scheduler import start_scheduler

app = FastAPI()

app.include_router(keywords.router)
app.include_router(alerts.router)
app.include_router(breach.router)

@app.on_event("startup")
def startup():
    start_scheduler()

@app.get("/")
def root():
    return {"message": "Dark Web Monitor Running"}