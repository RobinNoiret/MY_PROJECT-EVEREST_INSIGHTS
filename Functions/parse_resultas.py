from Functions.libs import BeautifulSoup

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