from database import SessionLocal, Citation

def count_citations():
    db = SessionLocal()
    count = db.query(Citation).count()
    db.close()
    return count

if __name__ == "__main__":
    total_citations = count_citations()
    print(f"Le nombre total de citations dans la base de données est : {total_citations}")
