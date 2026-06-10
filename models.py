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
    url_jogo = Column("url_jogo", String)
    nota_media = Column("nota_media", Float, default=0)
    
    
    def __init__(self, titulo, descricao, data_lancamento, url_jogo, nota_media):
        self.titulo = titulo 
        self.descricao = descricao
        self.data_lancamento = data_lancamento
        self.url_jogo = url_jogo
        self.nota_media = nota_media

class Noticia(Base):
    __tablename__ = "noticias"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    url_noticia = Column("url_noticias", String)
    descricao_noticia = Column("descricao", String)

    def __init__(self, url_noticia, descricao_noticia):
        self.url_noticia = url_noticia
        self.descricao_noticia = descricao_noticia

class Review(Base):

    __tablename__ = "reviews"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    jogo_id = Column(Integer, ForeignKey("jogos.id"))
    nota = Column("nota", Float)
    data_finalizacao = Column("data_finalizacao", Date)
    descricao = Column("descricao", String)
    finalizado = Column("finalizado", Boolean, default=False)
    dropado = Column("dropado", Boolean, default=False)

    def __init__(self, usuario_id, jogo_id, nota, data_finalizacao, descricao, finalizado, dropado):
        self.usuario_id = usuario_id
        self.jogo_id = jogo_id
        self.nota = nota
        self.data_finalizacao = data_finalizacao
        self.descricao = descricao
        self.finalizado = finalizado
        self.dropado = dropado

class Favorito(Base):

    __tablename__ = "favoritos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    jogo_id = Column(Integer, ForeignKey("jogos.id"))

    def __init__(self, usuario_id, jogo_id):
        self.usuario_id = usuario_id
        self.jogo_id = jogo_id

Base.metadata.create_all(db)
# python models.py executar no terminal para aparecer o arquivo no vs code
