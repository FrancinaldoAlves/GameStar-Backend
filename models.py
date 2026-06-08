from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String )
    descricao = Column("descricao", String)
    data_lancamento = Column("data_lancamento", Date)
    nota = Column("nota", Float, default=0)
    url_jogo = Column("url_jogo", String)
    
    
    def __init__(self, titulo, descricao, data_lancamento, nota, url_jogo):
        self.titulo = titulo 
        self.descricao = descricao
        self.data_lancamento = data_lancamento
        self.nota = nota
        self.url_jogo = url_jogo

class Noticia(Base):
    __tablename__ = "noticias"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    url_noticia = Column("url_noticias", String)
    descricao_noticia = Column("descricao", String)

    def __init__(self, url_noticia, descricao_noticia):
        self.url_noticia = url_noticia
        self.descricao_noticia = descricao_noticia

Base.metadata.create_all(db)
# python models.py executar no terminal para aparecer o arquivo no vs code
