from pydantic import BaseModel, Field
from typing import Optional


# Shape of data the client sends when creating a task
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200,
                       description="Task title (required)")


# Shape of data the client sends when updating a task
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    completed: Optional[bool] = None


# Shape of data the API returns
class Task(BaseModel):
    id: int
    title: str
    completed: bool
