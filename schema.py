from pydantic import BaseModel

class ListCreate(BaseModel):
    name: str
    age: int
    course: str

class List(ListCreate):
    id: int

    class Config:
        from_attributes = True