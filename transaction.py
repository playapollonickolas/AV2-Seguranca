from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from datetime import datetime
from database import Base
from uuid import uuid4

def generate_uuid():
    return str(uuid4())

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=generate_uuid)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # "income" ou "expense"
    category = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    owner_id = Column(String, ForeignKey("users.id"), nullable=False)
