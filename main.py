from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import random
from database import SessionLocal, Citation

app = FastAPI()

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root(db: Session = Depends(get_db)):
    citations = db.query(Citation).all()
    if not citations:
        raise HTTPException(status_code=404, detail="Aucune citation trouvée")
    return {"citation": random.choice(citations).text}

@app.get("/citations")
async def get_citations(db: Session = Depends(get_db)):
    citations = db.query(Citation).all()
    return {"citations": [citation.text for citation in citations]}

@app.get("/citations/{id}")
async def get_citation(id: int, db: Session = Depends(get_db)):
    citation = db.query(Citation).filter(Citation.id == id).first()
    if not citation:
        raise HTTPException(status_code=404, detail="Citation non trouvée")
    return {"citation": citation.text}

@app.post("/add_citation")
async def add_citation(new_citation: str, db: Session = Depends(get_db)):
    if new_citation:
        citation = Citation(text=new_citation)
        db.add(citation)
        db.commit()
        db.refresh(citation)
        return {"message": "Citation ajoutée avec succès!", "id": citation.id}
    raise HTTPException(status_code=400, detail="Citation invalide")