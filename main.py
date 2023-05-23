from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session

from database import engine,base,session
import schema
import model

base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    sus = session()
    try:
        yield sus
    finally:
        sus.close()

def comments():
# ------------------------------------------------------------------------------------

# fakedb = {
#     1: {  "title" : "Blog_1",
#             "content" : "Lorem Ipsum" },
#     2: {  "title" : "Blog_2",
#             "content" : "Lorem Ipsum" },
#     3: {  "title" : "Blog_3",
#             "content" : "Lorem Ipsum" }        
# }

# @app.get("/")
# def get_all_items(sus: Session = Depends(get_session)):
#     return fakedb

# @app.get("/{id}")
# def get_single_item(id:int):
#     return fakedb[id]

# @app.post("/")
# def add_item(title:str, content:str):
#     temp_id = len(fakedb.keys()) + 1
#     fakedb[temp_id] = {"title" : title, "content" : content}
#     return "Data Inserted Succesfully !!"

# @app.post("/")
# def add_item(item : schema.struct_item):
#     temp_id = len(fakedb.keys()) + 1
#     fakedb[temp_id] = {"title" : item.title, "content" : item.content, }
#     return "Data Inserted Succesfully !!"

# @app.put("/{id}")
# def update_item(id:int, item : schema.struct_item):
#     fakedb[id]['title'] = item.title
#     fakedb[id]['content'] = item.content
#     return "Data Updated Successfully !!"

# @app.delete("/{id}")
# def delete_item(id:int):
#     del fakedb[id]
#     return "Data Deleted Successfully !!"

# ------------------------------------------------------------------------------------

# Explanation of Shchema.py 

# pydantic is used to create a structure to reduce complexity which might arise while passing multiple arguments
# instead of passing multiple arguments in function definition, we create a class using pydantic basemodel
# create object of it in function definition

# ------------------------------------------------------------------------------------

# Explanation of database.py

# Creating the mysql connection
# Creating declarative base
# Creating session

    return "Notes"

# -------------------------------- GET ALL ITEMS ------------------------------------------

@app.get("/")
def get_all_items(sus: Session = Depends(get_session)):
    x = sus.query(model.item).all()
    return x

# -------------------------------- GET SINGLE ITEM BY ID ----------------------------------

@app.get("/{id}")
def get_single_item(id: int, sus : Session = Depends(get_session)):
    x = sus.query(model.item).get(id)
    return x

# -------------------------------- INSERT AN ITEM -----------------------------------------

@app.post("/")
def add_item(item : schema.struct_item, sus: Session = Depends(get_session)):

    x = model.item(title = item.title, content = item.content)

    sus.add(x) 
    sus.commit()
    sus.refresh(x)

    return x

# -------------------------------- UPDATE AN ITEM ----------------------------------------

@app.put("/{id}")
def update_item(id: int, item: schema.struct_item , sus : Session = Depends(get_session)):

    x = sus.query(model.item).get(id)
    x.title = item.title
    x.content = item.content
    sus.commit()

    return x

# -------------------------------- DELETE AN ITEM ----------------------------------------

@app.delete("/{id}")
def delete_item(id : int, sus : Session = Depends(get_session)):
    x = sus.query(model.item).get(id)
    sus.delete(x)
    sus.commit()
    session.close()
    return "Entry Deleted Successfully !!"
