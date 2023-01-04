from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "하이 빵까루"}