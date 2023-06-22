import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import requests

GOOGLE_SEARCH_URL = 'https://www.google.com/search'
HEADERS = {
	'Accept' : '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}
google_search_results = []

with open("isins.txt", "r") as file:
	isin_codes = file.read().splitlines()
file.close()

for isin in isin_codes:
	parameters = {'q': isin}
	print(parameters)
	content = requests.get(GOOGLE_SEARCH_URL, headers=HEADERS, params=parameters).text
	sleep(randint(1, 5))
	soup = BeautifulSoup(content, 'html.parser')
	search = soup.find(id='search')
	first_link = search.find('a')['href'] if search.find('a') else "Not available in Google"

	tempdata = {
		'ISIN': isin,
		'First Link': first_link
	}
	google_search_results.append(tempdata)
df = pd.DataFrame(google_search_results)
print(df)
