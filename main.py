from fastapi import FastAPI, requests,Header
from pydantic import BaseModel
from typing import Optional,List
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import Response
from datetime import date
app = FastAPI()
@app.get("/ping")
def show_pong():
    return Response(content="Pong",status_code=200,media_type="text")








