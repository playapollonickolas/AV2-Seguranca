from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Transaction
from schemas import TransactionCreate, TransactionUpdate, TransactionOut
from auth import get_current_user, get_db
from uuid import UUID

router = APIRouter()

@router.post("/transactions/", response_model=TransactionOut)
def create_transaction(tx: TransactionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_tx = Transaction(**tx.dict(), owner_id=user.id)
    db.add(new_tx)
    db.commit()
    db.refresh(new_tx)
    return new_tx

@router.get("/transactions/", response_model=list[TransactionOut])
def list_transactions(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Transaction).filter(Transaction.owner_id == user.id).all()

@router.get("/transactions/{id}", response_model=TransactionOut)
def get_transaction(id: UUID, db: Session = Depends(get_db), user=Depends(get_current_user)):
    tx = db.query(Transaction).filter(Transaction.id == id, Transaction.owner_id == user.id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return tx

@router.put("/transactions/{id}", response_model=TransactionOut)
def update_transaction(id: UUID, tx_data: TransactionUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    tx = db.query(Transaction).filter(Transaction.id == id, Transaction.owner_id == user.id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    for field, value in tx_data.dict().items():
        setattr(tx, field, value)
    db.commit()
    db.refresh(tx)
    return tx

@router.delete("/transactions/{id}")
def delete_transaction(id: UUID, db: Session = Depends(get_db), user=Depends(get_current_user)):
    tx = db.query(Transaction).filter(Transaction.id == id, Transaction.owner_id == user.id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    db.delete(tx)
    db.commit()
    return {"detail": "Transação excluída com sucesso"}
