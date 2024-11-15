from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration de la base de données
DATABASE_URL = "sqlite:///./citations.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modèle de la table des citations
class Citation(Base):
    __tablename__ = "citations"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)

# Créer les tables
Base.metadata.create_all(bind=engine)
