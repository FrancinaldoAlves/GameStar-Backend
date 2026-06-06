from models import db
from sqlalchemy.orm import sessionmaker


def pegar_Sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close() 