from Functions.libs import *
from variables import *

# Charger les données JSON existantes
file_path = expedition_path
with open(file_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Titres des champs
    #field_titles = field_deaths_titles
    field_titles = field_expedition_titles

# Structure pour stocker les résultats nettoyés
cleaned_data = []

# Utiliser un ensemble pour détecter les doublons
seen_entries = set()

# Variable pour stocker les valeurs temporaires
temp_entry = []

# Parcourir les données brutes
for record in raw_data:
    for entry in record:
        if entry and eWord1 not in entry and eWord2 not in entry:
            # Détecter le début d'un nouvel enregistrement
            if entry.startswith("EVER"):
                # Ajouter l'entrée précédente si elle est complète
                if len(temp_entry) == 11:
                    # Créer un dictionnaire avec les titres des champs
                    entry_dict = dict(zip(field_titles, temp_entry))
                    entry_tuple = tuple(entry_dict.items())  # Convertir en tuple pour la vérification des doublons
                    
                    # Ajouter l'entrée au résultat si elle n'est pas déjà vue
                    if entry_tuple not in seen_entries:
                        cleaned_data.append(entry_dict)
                        seen_entries.add(entry_tuple)
                
                # Réinitialiser pour le nouvel enregistrement
                temp_entry = [entry]
            else:
                temp_entry.append(entry)
    
    # Ajouter l'entrée finale après la fin de la boucle
    if len(temp_entry) == 11:
        entry_dict = dict(zip(field_titles, temp_entry))
        entry_tuple = tuple(entry_dict.items())  # Convertir en tuple pour la vérification des doublons
        
        if entry_tuple not in seen_entries:
            cleaned_data.append(entry_dict)
            seen_entries.add(entry_tuple)

# Écrire les résultats dans un nouveau fichier JSON formaté
with open('Data_JSON/cleaned_expedition.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

print("Les résultats nettoyés avec titres des champs ont été écrits dans 'cleaned_expedition.json'.")
