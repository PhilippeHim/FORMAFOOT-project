import json
from datetime import timedelta
import os

# Utilisation du chemin absolu
with open("ressources/api object/api.json", 'r') as f:
    data = json.load(f)

# Définition de la classe Module
class Module:
    def __init__(self, data : dict):
        self.title: dict = data.get("module_titre", []) # Attribuer à l"attribut "title" de l"objet Module les données correspondant à la clé "module_titre" dans "data"
        self.chapitres: list[Chapitre]=self.get_chapitres(data)  # Appeler la méthode get_chapitres() pour initialiser l"attribut "chapitres"
    
    def get_chapitres(self, data: dict):
        chapitres: list = [] # Initialiser une liste vide pour stocker les objets Chapitre
        for chapitre_data in data["chapitres"]: # Parcourir les données correspondant à la clé "chapitres" dans "data"
            chapitre = Chapitre(chapitre_data) # Créer un objet de la classe Chapitre en utilisant les données spécifiques de ce chapitre
            chapitres.append (chapitre) # Ajouter cet objet à la liste "chapitres"
        return chapitres # Retourner la liste des objets Chapitre créés

# Définition de la classe Formation
class Formation:
    def __init__(self, data):
        self.titre: str = data["titre"]
        self.financable: bool = data["financeable"]
        self.prix: int = data["prix"]
        self.apports: str  = data["apports"]
        self.prerequis: tuple = self.getnombredocs(data)
        self.nombre_documents_par_type, self.duree_totale = self.getnombredocs(data)
        self.module: list[Module]=self.get_module(data)
    
    def get_module(self, data:dict):
        modules: list = []
        for module_data in data["structure"]:
            # Créer un objet Module en utilisant le titre du module et ses données spécifiques
            module = Module(module_data)
            modules.append (module)
        return modules

     # Définition de la méthode getnombredocs()
    def getnombredocs(self, data: dict):
        
        # Initialisation des variables
        nombre_documents_par_type: dict = {} # Initialisation d"une bibliothèque
        types_documents: list = [] # Initialiser la liste "type de documents"
        duree_totale = timedelta()# Initialiser la durée totale à zéro

        # Parcours de la structure pour récupérer les documents
        for structure in data["structure"]:
            for chapitre in structure["chapitres"]:
                for subchapitre in chapitre["subchapitre"]:
                    for document in subchapitre["documents"]:
                        types_documents.append(document["type"]) # Ajouter le type de document à l"ensemble
                        type_document = document["type"]

                        # Incrémenter le nombre de documents du type correspondant =>
                        if type_document in nombre_documents_par_type:
                            # ==> Dans le dictionnaire "nombre_documents_par_type", on recherche si le type existe déjà
                            # ==> Si oui, on l"incrémente de 1
                            nombre_documents_par_type[type_document] += 1
                        else: # Sinon, on initialise à la valeur liée au nouveau type avec 1
                            nombre_documents_par_type[type_document] = 1
                        
                        # Calcul de la durée totale
                        duree = document["duree"]
                        # Convertir la durée au format timedelta et l"ajouter à la durée totale
                        heures, minutes, secondes = map(int, duree.split(":"))
                    duree_totale += timedelta(hours=heures, minutes=minutes, seconds=secondes)
        return nombre_documents_par_type, duree_totale #, financable, prix, apports, prerequis


#Page 3: Descriptif de la Formation
# Afficher les modules
numero_module: int = 1
for module in data.get("structure", []):
    # Numérotation des modules
    module["numero_m"] = numero_module
    numero_module += 1   # Incrémenter le compteur de module
    print("Module :", module["numero_m"], "-",  module["module_titre"])
    
    # Afficher les chapitres dans les modules
    numero_chapitre: int = 1
    for chapitre in module.get("chapitres", []):
        # Numérotation des chapitres
        chapitre["numero_c"] = numero_chapitre
        numero_chapitre += 1# Incrémenter le compteur de chapitre
        print("Chapitre :", chapitre["numero_c"], "-", chapitre["chapitre_titre"])
        
        # Afficher les sous-chapitres dans les chapitres
        subchapitres = []
        numero_sous_chapitre = 1
        for subchapitre in chapitre.get("subchapitre", []):
             # Numérotation des sous-chapitres
            subchapitre["numero_sc"] = numero_sous_chapitre
            subchapitres.append(subchapitre)
            numero_sous_chapitre += 1# Incrémenter le compteur de sous-chapitres
            print("Sous-chapitre :", subchapitre["numero_sc"], "-", subchapitre["subchapitre_titre"])
            print("Nombre de Documents dans ce sous-chapitre :", len(subchapitre.get("documents", []))) #Afficher le nombre de documents dans les sous chapitres

class Subchapitre:
    def __init__(self, data:dict):
        self.titre = data["subchapitre_titre"]
        self.nombredoc = len(data.get("documents", []))

class Chapitre:
    def __init__(self, data:dict):
        self.titre = data["chapitre_titre"]
        self.subchapitre  = data.get("subchapitre_titre", [])

    def get_subchapitres(self, data):
        subchapitres: list = []
        for subchapitre_data in data["subchapitres"]:
            # Créer un objet Module en utilisant le titre du module et ses données spécifiques
            subchapitre = Subchapitre(subchapitre_data)
            subchapitres.append (subchapitre)
        return subchapitres

formation = Formation(data=data)

#print(formation.module[0].title)
