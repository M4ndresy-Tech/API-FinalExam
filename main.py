from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional,List
app = FastAPI()
@app.get("/health")
def health():
    return "Ok"

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

phones_db: List[Phone] = []

@app.post("/phones", status_code=201)
def create_phone(phone: Phone):
    phones_db.append(phone)
    return phone

@app.get("/phones", response_model=List[Phone])
def get_phones():
    return phones_db







