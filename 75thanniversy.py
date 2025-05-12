import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/NBA_75th_Anniversary_Team"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find("table", class_="wikitable sortable plainrowheaders")

    if table:
        headers = [th.text.strip() for th in table.find_all("th")]
        
        data = []
        for row in table.find_all("tr")[1:]:  # Skip the header row
            cells = [td.text.strip() for td in row.find_all(["td", "th"])]
            if cells:
                data.append(cells)

        with open("75thteam.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(headers)  # Write only the headers
            writer.writerows(data)    # Write the actual data

        print("Successful")
    else:
        print("Table not found. The page structure may have changed.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")