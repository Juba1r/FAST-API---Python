from fastapi import FastAPI

app=FastAPI()

@app.get("/first")
def index (): 
    return "hello world"


@app.get("/item/{item_id}")
def index(item_id:int):
    return {"item_id": item_id}


@app.get("/item/")
def index(q:int=0):
    return {"product is" : q}