from typing import Union
import uvicorn
import requests
import json
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7.00 AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 7.00 AM."
    }
]

class ToDoList:
    ID = 1

    def __init__(self, name):
        self.__name = name
        self.__tasks = []

    def get_task(self):
        return self.__tasks

    def add_task(self, todo):
        id = ToDoList.ID
        todo["id"] = id
        self.__tasks.append(todo)
        ToDoList.ID += 1
        return id
    
    def modify_task(self, id, body):
        for todo in self.__tasks:
            if (int(todo["id"])) == id:
                todo["activity"] = body["activity"]
                return {
                    "data": f"Todo with id {id} has been updated"
                }
        return {
            "data": f"Todo with id {id} is not found!"
        }
    
    def delete_task(self, id):
        for todo in self.__tasks:
            if int(todo["id"]) == id:
                self.__tasks.remove(todo)
                return {
                    "data": f"Todo with id {id} has been deleted"
                }
        return {
            "data": f"Todo with id {id} was not found!"
        }
    
my_list = ToDoList("My")

@app.get("/")
async def read_root():
    html_path = Path("static/index.html")
    return FileResponse(html_path)

@app.get("/todo", tags=['Todos'])
async def get_todos() -> dict:
    return {"Data": my_list.get_task()}

@app.post("/todo", tags=["Todos"])
async def add_todo(task: dict) -> dict:
    id = my_list.add_task(task)
    todo = "A Todo "+str(id)+ " is added!"
    return {
        "data": todo
    }

@app.put("/todo/{id}", tags=["Todos"])
async def update_todo(id: int, body: dict) -> dict:
    return my_list.modify_task(id, body)

@app.delete("/todo/{id}", tags=["Todos"])
async def delete_todo(id: int) -> dict:
    return my_list.delete_task(id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

# act = {"id": "3", "Activity": "Play football"}
# r = requests.post("http://127.0.0.1:8000/todo", data=json.dumps(act))
# print(r.json())

# act = {"id": "3", "Activity": "Play games"}
# r = requests.put("http://127.0.0.1:8000/todo/3", data=json.dumps(act))
# print(r.json())

# r = requests.get("http://127.0.0.1:8000/todo")
# print(r.json())

# r = requests.delete("http://127.0.0.1:8000/todo/3")
# print(r.json())