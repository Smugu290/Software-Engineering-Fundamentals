from fastapi import APIRouter, HTTPException, status
from data.tasks import tasks, get_next_id
from schema import TaskCreate, Task, TaskUpdate

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


#  GET /api/tasks — Get all tasks
@router.get("/", response_model=list[Task])
def get_tasks():
    return tasks


#  POST /api/tasks — Add a new task
@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def add_task(task_data: TaskCreate):
    new_task = {
        "id": get_next_id(),
        "title": task_data.title,
        "completed": False,
    }
    tasks.append(new_task)
    return new_task


# DELETE /api/tasks/{task_id} — Delete a task
@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    # Find the task index
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(index)
            return {"message": "Task deleted", "data": deleted}

    # If we get here, task wasn't found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id {task_id} not found"
    )
