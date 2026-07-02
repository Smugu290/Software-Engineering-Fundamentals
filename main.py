from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as tasks_router

app = FastAPI(
    title="Task API",
    description="A simple task management API",
    version="1.0.0",
)

# Allow frontend apps to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(tasks_router)


@app.get("/")
def home():
    return {"message": "Task API is running successfully!"}
