from database import SessionLocal, Citation

# Liste de citations par défaut
default_citations = [
    "La vie est ce qui se passe pendant que vous êtes occupé à faire d'autres projets. - John Lennon",
    "Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme. - Winston Churchill",
    "La meilleure façon de prédire l'avenir, c'est de le créer. - Peter Drucker",
    "L'imagination est plus importante que la connaissance. - Albert Einstein",
    "Je rêve d'un jour où l'égoïsme ne régnera plus dans les  sciences, où on s'associera pour étudier, au lieu d'envoyer aux académiciens des plis cachetés, on s'empressera de publier ses moindres observations pour peu qu'elles soient nouvelles, et on ajoutera 'je ne sais pas le reste'. - Évariste Galois"
]

# Ajouter les citations dans la base de données
def initialize_database():
    db = SessionLocal()
    for text in default_citations:
        citation = Citation(text=text)
        db.add(citation)
    db.commit()
    db.close()

if __name__ == "__main__":
    initialize_database()
