from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import model
import schema
from database import engine, SessionLocal

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/lists")
def create_list(list_item: schema.ListCreate, db: Session = Depends(get_db)):
    new_list = model.List(
        name=list_item.name,
        age=list_item.age,
        course=list_item.course
    )

    db.add(new_list)
    db.commit()
    db.refresh(new_list)

    return new_list

@app.get("/lists")
def get_lists(db: Session = Depends(get_db)):
    return db.query(model.List).all()