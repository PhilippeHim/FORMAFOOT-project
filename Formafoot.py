import json
import os

# Ouvrir le fichier JSON en mode lecture
with open('/Users/philippehim/Library/Mobile Documents/com~apple~CloudDocs/IA SCHOOL/04_DEV/Projet DEV GEMA/PythonDev/FORMAFOOT/ressources/api object/api.json', 'r') as f:
    donnees = json.load(f)  # Charger les données JSON dans un objet Python

# data = import_form_json (os.path.abspath("ressource/api object/api.json"))

""" # *Page 1**
# - **Titre et Description de la Formation** 
titreformation = donnees["titre"]

# **Page 2**
# - **Informations Générales** :

financeable = donnees["financeable"]
#   - Prix
prix = donnees["prix"]
prix1 = donnees.get["prix", 0]
#   - Apports
apports = donnees["apports"]
#   - Prérequis
prerequis = donnees["prerequis"]
#   - Durée totale
dureemod1chap1 = donnees ['structure'][0]['chapitres'][0]['subchapitre'][0]['documents'][0]["duree"]
dureemod1chap2 = donnees ['structure'][0]['chapitres'][1]['subchapitre'][0]['documents'][0]["duree"]
dureemod1chap12 = donnees ['structure'][0]['chapitres'][1]['subchapitre'][1]['documents'][0]["duree"]
dureemod2chap2 = donnees ['structure'][1]['chapitres'][0]['subchapitre'][0]['documents'][0]["duree"]
#   - Nombre de documents types (vidéo, PDF, etc.)
docn1 = donnees ['structure'][0]['chapitres'][0]['subchapitre'][0]['documents'][0]["type"]
docn2 = donnees ['structure'][0]['chapitres'][1]['subchapitre'][0]['documents'][0]["type"]
docn3 = donnees ['structure'][0]['chapitres'][1]['subchapitre'][1]['documents'][0]["type"]
docn4 = donnees ['structure'][1]['chapitres'][0]['subchapitre'][0]['documents'][0]["type"]

# Modules
module1 = donnees ['structure'][0]["module_titre"]
module2 = donnees ['structure'][1]["module_titre"]

# Chapitres dans les modules
chap1mod1 = donnees ['structure'][0]['chapitres'][0]["chapitre_titre"]
chap2mod1 = donnees ['structure'][0]['chapitres'][1]["chapitre_titre"]
chap1mod2 = donnees ['structure'][1]['chapitres'][0]["chapitre_titre"]

# Sous-chapitres dans les chapitres
ss1chap1mod1 = donnees ['structure'][0]['chapitres'][0]['subchapitre'][0]['documents'][0]['type']
ss1chap1mod1 = donnees ['structure'][0]['chapitres'][1]['subchapitre'][0]['documents'][0]['type']
ss1chap1mod1 = donnees ['structure'][0]['chapitres'][1]['subchapitre'][1]['documents'][0]['type']
ss1chap1mod1 = donnees ['structure'][1]['chapitres'][0]['subchapitre'][0]['documents'][0]['type']

# Nombre de Documents dans les sous-chapitres

print(titreformation)
print(financeable)
print(prix)
print(apports)
print(prerequis)
print(dureemod1chap1)
print(dureemod1chap2)
print(dureemod1chap12)
print(dureemod2chap2)
print(docn1)
print(docn2)
print(docn3)
print(docn4)
print(module1)
print(module2)
print(chap1mod1)
print(chap2mod1)
print(chap1mod2) """

# Initialisation du compteur de documents
# types_documents = []

# nombre_documents_par_type = {}

# fonction récupération de données dans le fichier json
def getnombredocs():
    nombre_documents = 0
    nombre_documents_par_type = {}
    types_documents = []
    #global nombre_documents
    #global nombre_documents_par_type
    # Parcours de la structure pour récupérer les documents
    for structure in donnees['structure']:
        for chapitre in structure['chapitres']:
            for subchapitre in chapitre['subchapitre']:
                for document in subchapitre['documents']:
                    # Ajouter le type de document à l'ensemble
                    types_documents.append(document['type'])
                    #Incrémenter le compteur de documents
                    nombre_documents += 1
                    print(nombre_documents)
                    #Incrémenter le nombre de documents du type correspondant
                    type_document = document["type"]
                    # Incrémenter le nombre de documents du type correspondant
                    if type_document in nombre_documents_par_type:
                        nombre_documents_par_type[type_document] += 1
                    else:
                        nombre_documents_par_type[type_document] = 1


    # Supprimer les doublons en convertissant la liste en ensemble puis en la reconvertissant en liste
    return (nombre_documents, nombre_documents_par_type)

nombre_documents, types_documents = getnombredocs()

print(nombre_documents)

for type_document, nombre in types_documents.items():
    print(f"Type de document : {type_document}, Nombre de documents : {nombre}")

#types_documents = list(set(types_documents))


# Affichage des types de documents
#print("Types de documents présents :", types_documents)

# Affichage du nombre total de documents
#print("Nombre total de documents :", nombre_documents)

# utiliser split et map
""""
# On vérifie le type d'une chaine
print(type(id_structure))

class Personne:
    def __init__(id):
        self.nom = nom
        self.age = age
        self.ville = ville

    def __str__(self):
        return f"Nom: {self.nom}, Age: {self.age}, Ville: {self.ville}"

# Charger les données du fichier JSON
with open('donnees.json', 'r') as f:
    donnees = json.load(f)

# Créer des objets Personne à partir des données JSON
personnes = []
for personne_json in donnees:
    personne = Personne(personne_json['nom'], personne_json['age'], personne_json['ville'])
    personnes.append(personne)

# Afficher les objets Personne créés
for personne in personnes:
    print(personne)"""
