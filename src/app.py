from fastapi import FastAPI

app = FastAPI()


@app.get("/get_model_1")
async def get_model_1(messsage: str):
    return {"message": messsage}

@app.get("/get_model_2")
async def get_model_2():
    return {"message": "Hello World"}

@app.get("/get_model_3")
async def get_model_3():
    return {"message": "Hello World"}

@app.get("/get_model_4")
async def get_model_4():
    return {"message": "Hello World"}