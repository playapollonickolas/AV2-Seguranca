# API de Controle Financeiro Pessoal

Esta API permite que usuários organizem suas finanças pessoais com segurança, realizando cadastro, autenticação e controle de transações de entrada e saída. O sistema foi desenvolvido com foco em segurança, escalabilidade e preparo para ambiente de nuvem.

## Tecnologias Utilizadas

- FastAPI — Framework Web moderno e rápido para APIs.
- SQLAlchemy — ORM para acesso ao banco de dados.
- SQLite — Banco de dados local simples e leve.
- Python-Jose — Criação e validação de tokens JWT.
- Passlib + bcrypt — Criptografia de senhas.
- Python Dotenv — Gerenciamento de variáveis de ambiente.
- SlowAPI — Rate limiting contra ataques.
- Uvicorn — Servidor ASGI para rodar a aplicação.

## Como Executar Localmente

1. Clone o repositório:
   git clone https://github.com/seu-usuario/nome-do-repo.git
   cd nome-do-repo

2. Crie e ative um ambiente virtual:
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows

3. Instale as dependências:
   pip install -r requirements.txt

4. Inicie a aplicação:
   uvicorn main:app --reload

5. Acesse a documentação:
   http://127.0.0.1:8000/docs#/

## Estrutura de Segurança Implementada

- Autenticação com JWT.
- Autorização baseada no usuário autenticado.
- Criptografia de senhas com bcrypt.
- Proteção contra ataques com rate limiting (slowapi).
- Middleware CORS para controle de origens confiáveis.
- Variáveis sensíveis protegidas com .env.
- Logs de auditoria para monitoramento de login e atividades suspeitas.
