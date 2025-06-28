from database import Base, engine
from models import User, Transaction

print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Concluído.")