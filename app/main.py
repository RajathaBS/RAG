from fastapi import FastAPI
from endpoints import router
app = FastAPI()
app.include_router(router)
@app.get("/")
def read_root():
    return {"status": "ok"}
