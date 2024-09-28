from Functions.libs import *
from Functions.fetch_pages import fetch_page
from Functions.parse_resultas import parse_results
from variables import *

def fetch_peak_deaths_report(start_date, end_date, interval_days):
    # Variables for Deaths report query
    url = deaths_url
    data = deaths_data
    headers = deaths_header

    # Liste pour stocker tous les résultats
    all_results = []

    # Boucle pour découper par dates
    current_start_date = start_date
    while current_start_date <= end_date:
        current_end_date = min(current_start_date + timedelta(days=interval_days - 1), end_date)
        year_start = current_start_date.year
        year_end = current_end_date.year
        
        print(f"Traitement de la période de {current_start_date} à {current_end_date}")
        html = fetch_page(year_start, year_end, url, data, headers)
        if html:
            results = parse_results(html)
            if results:
                all_results.extend(results)
        
        # Passer à la période suivante
        current_start_date = current_end_date + timedelta(days=1)

    if not os.path.exists('Data_JSON'):
        os.makedirs('Data_JSON')

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'Data_JSON/deaths_{timestamp}.json'

    # Écrire les résultats dans un fichier JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)

    print("Les résultats ont été écrits dans 'results.json'.")
    return filename
