from libs import *

# URL cible
url = "https://www.himalayandatabase.com/scripts/peakdead.php"

# Corps de la requête avec les paramètres extraits du formulaire
data = {
    'Peak_ID': 'EVER',     # Everest
    'Season': '0',         # Toutes les saisons
    'Pk_Citz1': '',        # Pas de filtre de citoyenneté
    'Pk_Citz2': '',        # Pas de filtre de citoyenneté
    'Host': '0',           # Pas de filtre par pays hôte
    'Group': '0',          # Pas de filtre par groupe
    'Oxygen': '0',         # Pas de filtre sur l'usage d'oxygène
    'Order': '1'           # Ordre chronologique
}

# En-têtes de la requête
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.himalayandatabase.com',
    'Origin': 'https://www.himalayandatabase.com',
    'Referer': 'https://www.himalayandatabase.com/Online/peakdead.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

# Intervalle de dates
start_date = datetime(1920, 1, 1)
end_date = datetime(2024, 12, 31)
interval_days = 365  # Intervalle en jours

def fetch_page(year_start, year_end):
    data['Pk_Year1'] = year_start
    data['Pk_Year2'] = year_end
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Erreur : {response.status_code}")
        return None

def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    table = soup.find('table')  # Adapter selon la structure du HTML
    if table:
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 0:
                result = [cell.get_text(strip=True) for cell in cells]
                results.append(result)
    else:
        print("Aucune table trouvée dans le HTML.")
    return results

# Liste pour stocker tous les résultats
all_results = []

# Boucle pour découper par dates
current_start_date = start_date
while current_start_date <= end_date:
    current_end_date = min(current_start_date + timedelta(days=interval_days - 1), end_date)
    year_start = current_start_date.year
    year_end = current_end_date.year
    
    print(f"Traitement de la période de {current_start_date} à {current_end_date}")
    html = fetch_page(year_start, year_end)
    if html:
        results = parse_results(html)
        if results:
            all_results.extend(results)
    
    # Passer à la période suivante
    current_start_date = current_end_date + timedelta(days=1)

# Écrire les résultats dans un fichier JSON
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=4)

print("Les résultats ont été écrits dans 'results.json'.")
