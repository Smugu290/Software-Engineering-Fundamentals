# In-memory task storage (replace with database later)
tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build an API", "completed": False},
]

next_id = 3


def get_next_id() -> int:
    global next_id
    current = next_id
    next_id += 1
    return current
