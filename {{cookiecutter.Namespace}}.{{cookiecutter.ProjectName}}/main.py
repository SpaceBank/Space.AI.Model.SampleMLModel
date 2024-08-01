from fastapi import FastAPI, Body
import os
import uvicorn
from pydantic import BaseModel


path_base = os.environ.get('PATH_BASE')

class Item(BaseModel):
    data: str

app = FastAPI()

@app.get("/")
def hello():
    # Return a simple JSON response to indicate the app is working
    return {"Hello": "Space"}

@app.post("/echo")
async def echo(item: Item = Body(...)):
    # Check if data is present in the request body
    return {'data': item.data}

mounted_app = FastAPI()
mounted_app.mount(path_base, app)

if __name__ == "__main__":
    uvicorn.run("main:mounted_app", host="0.0.0.0", port=80, reload=True)
