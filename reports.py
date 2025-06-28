from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth import get_current_user, get_db
from models import Transaction
from schemas import ReportSummary

router = APIRouter()

@router.get("/reports/summary", response_model=ReportSummary)
def get_summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    transactions = db.query(Transaction).filter(Transaction.owner_id == user.id).all()

    total_income = sum(t.amount for t in transactions if t.type == "income")
    total_expense = sum(abs(t.amount) for t in transactions if t.type == "expense")
    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }
