from Functions.libs import *


def fetch_page(year_start, year_end, url, data, headers):
    data['Pk_Year1'] = year_start
    data['Pk_Year2'] = year_end
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Erreur : {response.status_code}")
        return None