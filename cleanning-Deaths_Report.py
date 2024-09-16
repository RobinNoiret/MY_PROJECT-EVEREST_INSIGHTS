from Functions.libs import *

# Charger les données JSON existantes
with open('Data_JSON/deaths_2024-09-16_12-06-32.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Structure pour stocker les résultats nettoyés
cleaned_data = []

# Utiliser un ensemble pour détecter les doublons
seen_entries = set()

# Parcourir les données brutes
for record in raw_data:
    temp_entry = []

    for entry in record:
        if entry and "Death Count" not in entry and "Peak Deaths Report" not in entry:
            # Si on rencontre "EVER", c'est le début d'une nouvelle entrée
            if entry == "EVER":
                # Si temp_entry n'est pas vide, ajoutez-la aux résultats
                if temp_entry:
                    entry_tuple = tuple(temp_entry)
                    
                    # Ajouter l'entrée au résultat si elle n'est pas déjà vue
                    if entry_tuple not in seen_entries:
                        cleaned_data.append(temp_entry)
                        seen_entries.add(entry_tuple)
                    
                    temp_entry = []  # Réinitialisez temp_entry pour la nouvelle entrée
            
            # Ajouter l'entrée à temp_entry
            temp_entry.append(entry)

    # Ajoutez l'entrée finale si temp_entry n'est pas vide à la fin du record
    if temp_entry:
        entry_tuple = tuple(temp_entry)
        if entry_tuple not in seen_entries:
            cleaned_data.append(temp_entry)
            seen_entries.add(entry_tuple)

# Écrire les résultats dans un nouveau fichier JSON formaté
with open('Data_JSON/cleaned_deaths.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

print("Les résultats nettoyés ont été écrits dans 'cleaned_deaths.json'.")
