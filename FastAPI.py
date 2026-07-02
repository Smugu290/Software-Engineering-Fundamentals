from fastapi import FastAPI
from routes import router

app = FastAPI(title="Task API")
app.include_router(router)


@app.get("/")
def home():
    return {"message": "Hello AI Engineer"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("FastAPI:app", host="127.0.0.1", port=8000, reload=False)