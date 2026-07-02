
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

fake_tasks_db: List[Task] = [
    Task(id=1, title="Learn FastAPI", description="Read the docs", completed=False),
    Task(id=2, title="Build an API", description="Create routes", completed=True),
]

@app.get("/", tags=["health"])
def read_root() -> dict:
    return {"message": "FastAPI is running"}

@app.get("/tasks", response_model=List[Task], tags=["tasks"])
def list_tasks() -> List[Task]:
    return fake_tasks_db

@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: int) -> Task:
    for task in fake_tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task, status_code=201, tags=["tasks"])
def create_task(task: Task) -> Task:
    if any(existing.id == task.id for existing in fake_tasks_db):
        raise HTTPException(status_code=400, detail="Task with this id already exists")
    fake_tasks_db.append(task)
    return task

