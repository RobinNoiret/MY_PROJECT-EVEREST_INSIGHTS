import json
import matplotlib.pyplot as plt
from collections import Counter

# Charger les données JSON nettoyées
with open('Data_JSON/cleaned_deaths.json', 'r', encoding='utf-8') as f:
    cleaned_data = json.load(f)

# Compter les occurrences des nationalités
nationalities = [record["Citizenship"] for record in cleaned_data if "Citizenship" in record]
nationality_counts = Counter(nationalities)

# Afficher le résultat des comptes
print(nationality_counts)

# Extraire les nationalités et leurs fréquences
labels, values = zip(*nationality_counts.items())

# Créer un graphique à barres
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='skyblue')

# Ajouter des labels et un titre
plt.xlabel('Nationalités')
plt.ylabel('Nombre de décès')
plt.title('Répartition des nationalités dans les décès sur l\'Everest')

# Rotation des labels pour une meilleure lisibilité
plt.xticks(rotation=90)

# Afficher le graphique
plt.tight_layout()
plt.show()
