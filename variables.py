from Functions.libs import datetime
#___________________________________

start_date = datetime(1920, 1, 1)
end_date = datetime(2024, 12, 31)
interval_days = 365  # Intervalle en jours

#____________________________________________________________________________________________________________
#                                           Fetch Deaths Report
#____________________________________________________________________________________________________________

# Endpoint of deaths report
deaths_url = "https://www.himalayandatabase.com/scripts/peakdead.php"

# Forms information
deaths_data = {
    'Peak_ID': 'EVER',     # Peak Everest
    'Season': '0',         # Toutes les saisons
    'Pk_Citz1': '',        # Pas de filtre de citoyenneté
    'Pk_Citz2': '',        # Pas de filtre de citoyenneté
    'Host': '0',           # Pas de filtre par pays hôte
    'Group': '0',          # Pas de filtre par groupe
    'Oxygen': '0',         # Pas de filtre sur l'usage d'oxygène
    'Order': '1'           # Ordre chronologique
}

# Death header
deaths_header = {
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
