import json
from datetime import timedelta

# Ouvrir le fichier JSON en mode lecture
with open('/Users/philippehim/Library/Mobile Documents/com~apple~CloudDocs/IA SCHOOL/04_DEV/Projet DEV GEMA/PythonDev/FORMAFOOT/ressources/api object/api.json', 'r') as f:
    donnees = json.load(f)  # Charger les données JSON dans un objet Python


class Formation:
    def __init__(self, data):
        self.titre = data["titre"]
        self.financable = data["financeable"]
        self.prix = data["prix"]
        self.apports = data["apports"]
        self.prerequis = self.getnombredocs(data)
        self.nombre_documents_par_type, self.duree_totale, = self.getnombredocs(data)
        self.chapitres = self.get_chapitres(data)
        self.subchapitres = self.get_subchapitres (data)

    def getnombredocs(self, data):
        nombre_documents_par_type: dict = {} # Initialisation d'une bibliothèque
        types_documents = []
        # Initialiser la durée totale à zéro
        duree_totale = timedelta()
        # Parcours de la structure pour récupérer les documents
        for structure in donnees["structure"]:
            for chapitre in structure["chapitres"]:
                for subchapitre in chapitre["subchapitre"]:
                    for document in subchapitre["documents"]:
                        # Ajouter le type de document à l'ensemble
                        types_documents.append(document["type"])
                        #Incrémenter le compteur de documents
                        type_document = document["type"]
                        # Incrémenter le nombre de documents du type correspondant =>
                        # ==> Dans le dictionnaire "nombre_documents_par_type", on recherche si le type existe déjà
                        # ==> Si oui, on l'incrémente de 1
                        if type_document in nombre_documents_par_type:
                            nombre_documents_par_type[type_document] += 1
                        # Sinon, on initialise à la valeur liée au nouveau type avec 1
                        else:
                            nombre_documents_par_type[type_document] = 1
                        duree = document["duree"]
                        # Convertir la durée au format timedelta et l'ajouter à la durée totale
                        heures, minutes, secondes = map(int, duree.split(":"))
                    duree_totale += timedelta(hours=heures, minutes=minutes, seconds=secondes)
        return nombre_documents_par_type, duree_totale #, financable, prix, apports, prerequis

    def get_chapitres(self, data) -> list:
            chapitres = []
            for structure in donnees["structure"]:
                for chapitre in structure["chapitres"]:
                    chapitres.append(chapitre)
            return chapitres

    def get_subchapitres(self, data):
            subchapitres = []
            for structure in donnees["structure"]:
                for chapitre in structure["chapitres"]:
                    for subchapitre in chapitre["subchapitre"]:
                        subchapitres.append(subchapitre)
            return subchapitres


formation = Formation(data = donnees)

print(formation.titre)
print(formation.financable)
print(formation.prix)
print(formation.apports)
print(formation.prerequis)
print(formation.duree_totale)
print(formation.nombre_documents_par_type)

print("Titre de la formation :", formation.titre)
print("Chapitres de la formation :", formation.chapitres[0])
#print("Sous chapitres de la formation :", formation.subchapitres)
