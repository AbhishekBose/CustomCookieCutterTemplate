from typing import Optional

from fastapi import FastAPI

app = FastAPI()

'''
Dummy api which returns a simple message when invoked
'''
@app.get("/")
def read_root():
    return {"msg": "Hello World"}

