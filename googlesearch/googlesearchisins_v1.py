import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import requests

url = 'https://www.google.com/search'
headers = {
	'Accept' : '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}
googlesearch = []

file = open("./isins.txt")
lines = file.read().splitlines()
file.close()

for isin in lines:
	parameters = {'q': isin}
	print(parameters)
	content = requests.get(url, headers=headers, params=parameters).text
	sleep(randint(1, 5))
	soup = BeautifulSoup(content, 'html.parser')
	search = soup.find(id='search')
	try:
		first_link = search.find('a')['href']
	except TypeError:
		first_link = "Not available in Google"

	tempdata = {
		'ISIN': isin,
		'First Link': first_link
	}
	googlesearch.append(tempdata)
df = pd.DataFrame.from_dict(googlesearch)
print(df)
