from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from loguru import logger
import uvicorn
import requests

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message:", "Hello WORLD"}


@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/users/me", summary="testheader_example")

async def get_users():
    """
    Testing schwager schema
    :return:
    """
    return {"user_id": "The current user"}


@app.get("/users/{user_id}")
async def read_item(user_id: str, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}

@app.get("/get_info/")
async def get_info():
    reg = requests.get('https://clinicaltrials.gov/api/v2/studies')
    return reg.json()

#@app.get("/page_code")
#async def get_page_code():
    #x = requests.get('https://clinicaltrials.gov/api/v2/studies')
    #reg = x.content
    #reg = json.loads(x.content)
    #json_reg = json.dumps(reg, sort_keys=True, indent=4)
    #return bytes(json_reg,'UTF-8')
    # reg = requests.get('https://clinicaltrials.gov/')
    # print(reg.status_code)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=False,
                log_level="debug", workers=1)
                #limit_concurrency=1, limit_max_requests=1)
