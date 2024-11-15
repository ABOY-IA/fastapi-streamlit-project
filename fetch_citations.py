import requests
from database import SessionLocal, Citation

Kaamelott_API_URL = "https://kaamelott.chaudie.re/api/all"

def fetch_and_store_citations():
    response = requests.get(Kaamelott_API_URL)
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == 1:
            citations = data.get("citation", [])
            db = SessionLocal()
            for item in citations:
                text = item.get("citation")
                if text:
                    exists = db.query(Citation).filter(Citation.text == text).first()
                    if not exists:
                        citation = Citation(text=text)
                        db.add(citation)
            db.commit()
            db.close()
            print(f"{len(citations)} citations ont été ajoutées à la base de données.")
        else:
            print("Erreur lors de la récupération des citations.")
    else:
        print(f"Erreur lors de la requête HTTP : {response.status_code}")

if __name__ == "__main__":
    fetch_and_store_citations()
