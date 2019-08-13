from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos=[] #FIXME define type

class ToDoItem(BaseModel):
    name: str = "Unknown"
    done: bool = False

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    #return {"item_id": item_id, "q": q}
    return todos[item_id]

@app.post("/items/")
async def create_item(item: ToDoItem):
    id: int = len(todos)
    todos.append(item)
    return id

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ToDoItem):
    return {"item_id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, item: ToDoItem):
    return {"item_id": item_id, "item": item}

