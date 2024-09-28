from Functions.libs import *
from Functions.fetch_pages import fetch_page
from Functions.parse_resultas import parse_results
from variables import *
from fetch_Peak_Deaths_Report import fetch_peak_deaths_report
from fetch_Peak_Expedition_Report import fetch_peak_expedition_report
from fetch_Peak_Submit_Report import fetch_peak_submit_report
from Functions.check_file import check_file_age
from cleanning_Reports import clean_data

# ________________________________________________________________________________________________________________
# _____________________________________________   Fetching Reports   _____________________________________________
# ________________________________________________________________________________________________________________

# Définir la période pour laquelle nous voulons récupérer les données
start_date = datetime(1950, 1, 1)
end_date = datetime.now()
interval_days = 365  # Intervalle d'un an pour chaque requête

# Vérifier et récupérer les rapports si nécessaire
if check_file_age("Data_JSON/deaths_*.json"):
    print("____________________________________________________")
    print("                    Deaths Report                   ")
    print("____________________________________________________")
    deaths_file = fetch_peak_deaths_report(start_date, end_date, interval_days)
    print(f"Rapport de décès enregistré dans : {deaths_file}")
else:
    print("Le rapport de décès existe déjà et est à jour.")

if check_file_age("Data_JSON/expedition_*.json"):
    print("____________________________________________________")
    print("                    Expedition Report               ")
    print("____________________________________________________")
    expedition_file = fetch_peak_expedition_report(start_date, end_date, interval_days)
    print(f"Rapport d'expédition enregistré dans : {expedition_file}")
else:
    print("Le rapport d'expédition existe déjà et est à jour.")

if check_file_age("Data_JSON/submit_*.json"):
    print("____________________________________________________")
    print("                    Submit Report                   ")
    print("____________________________________________________")
    submit_file = fetch_peak_submit_report(start_date, end_date, interval_days)
    print(f"Rapport de soumission enregistré dans : {submit_file}")
else:
    print("Le rapport de soumission existe déjà et est à jour.")

# ________________________________________________________________________________________________________________
# ______________________________________________   Cleanning Data   ______________________________________________
# ________________________________________________________________________________________________________________

print("____________________________________________________")
print("                    Cleaning Data                    ")
print("____________________________________________________")

file_path = max(glob.glob("Data_JSON/deaths_*.json"), key=os.path.getctime)
field_titles = field_deaths_titles
word1 = dWord1
word2 = dWord2
output_path = "Data_JSON/cleaned_deaths.json"
clean_data(file_path, field_titles, word1, word2, output_path)

file_path = max(glob.glob("Data_JSON/submit_*.json"), key=os.path.getctime)
field_titles = field_submit_titles
word1 = sWord1
word2 = sWord2
output_path = "Data_JSON/cleaned_submit.json"
clean_data(file_path, field_titles, word1, word2, output_path)

#file_path = max(glob.glob("Data_JSON/expedition_*.json"), key=os.path.getctime) #Ne fonctionne pas car ne commence pas par EVER
#field_titles = field_expedition_titles
#word1 = eWord1
#word2 = eWord2
#output_path = "Data_JSON/cleaned_expedition.json"
#clean_data(file_path, field_titles, word1, word2, output_path)

