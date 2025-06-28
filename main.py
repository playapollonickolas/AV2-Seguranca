from fastapi import FastAPI
from database import Base, engine
from auth import router as auth_router
from transactions import router as transactions_router
from reports import router as reports_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(transactions_router)
app.include_router(reports_router)


@app.get("/")
def root():
    return {"message": "API de Controle Financeiro ativa!"}



origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)


#Limitador
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi import Request
from fastapi.responses import JSONResponse

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)