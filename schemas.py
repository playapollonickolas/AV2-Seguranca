from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
        

class TransactionCreate(BaseModel):
    title: str
    description: str | None = None
    amount: float
    type: str  # "income" ou "expense"
    category: str

class TransactionOut(TransactionCreate):
    id: str
    created_at: datetime
    updated_at: datetime
    owner_id: str

    class Config:
        orm_mode = True
        

class ReportSummary(BaseModel):
    total_income: float
    total_expense: float
    balance: float

