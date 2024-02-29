import json

# Ouvrir le fichier JSON en mode lecture
with open('/Users/philippehim/Library/Mobile Documents/com~apple~CloudDocs/IA SCHOOL/04_DEV/Projet DEV GEMA/PythonDev/FORMAFOOT/ressources/api object/api.json', 'r') as f:
    donnees = json.load(f)  # Charger les données JSON dans un objet Python

# fonction récupération de données dans le fichier json
def getnombredocs():
    # nombre_documents = 0
    nombre_documents_par_type = {}
    types_documents = []
    # Parcours de la structure pour récupérer les documents
    for structure in donnees['structure']:
        for chapitre in structure['chapitres']:
            for subchapitre in chapitre['subchapitre']:
                for document in subchapitre['documents']:
                    # Ajouter le type de document à l'ensemble
                    types_documents.append(document['type'])
                    #Incrémenter le compteur de documents
                 
                    #Incrémenter le nombre de documents du type correspondant
                    type_document = document["type"]
                    # Incrémenter le nombre de documents du type correspondant =>
                    # ==> Dans le dictionnaire "nombre_documents_par_type", on recherche si le type existe déjà
                    # ==> Si oui, on l'incrémente de 1
                    if type_document in nombre_documents_par_type:
                        nombre_documents_par_type[type_document] += 1
                    # Sinon, on initialise à la valeur liée au nouveau type avec 1
                    else:
                        nombre_documents_par_type[type_document] = 1
    return (nombre_documents_par_type)

types_documents = getnombredocs()

for type_document, nombre in types_documents.items():
    print(f"Type de document : {type_document}, Nombre de documents : {nombre}")
