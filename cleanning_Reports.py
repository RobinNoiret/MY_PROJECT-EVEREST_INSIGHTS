from Functions.libs import *
from variables import *

def clean_data(file_path, field_titles, word1, word2, output_path):
    # Charger les données JSON existantes
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    # Structure pour stocker les résultats nettoyés
    cleaned_data = []

    # Utiliser un ensemble pour détecter les doublons
    seen_entries = set()

    # Variable pour stocker les valeurs temporaires
    temp_entry = []

    # Parcourir les données brutes
    for record in raw_data:
        for entry in record:
            if entry and word1 not in entry and word2 not in entry:
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

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)            

    return cleaned_data