# Google Search with ISIN Codes
```
This Python script performs a Google search using a list of ISIN codes and retrieves the first search result link for each ISIN. 
It utilizes the requests library to send HTTP requests to Google's search engine and the BeautifulSoup library for parsing the HTML content.
```
## Prerequisites
Make sure you have the following libraries installed:

pandas
bs4 (BeautifulSoup)
You can install these dependencies using pip:
```
pip install pandas beautifulsoup4
```
## Usage
Prepare the ISIN codes:

Create a text file named isins.txt in the same directory as the script.
Put each ISIN code on a separate line.
Run the script:

Execute the Python script using an environment that has the required dependencies installed.
The script will read the ISIN codes from isins.txt, perform a Google search for each code, and retrieve the first search result link.
The results will be displayed in a Pandas DataFrame.

## Customization
You can modify the headers dictionary in the script to change the user-agent and other headers sent with the requests.
Adjust the sleep time (randint(1, 5)) to introduce a delay between requests to avoid being blocked by Google.



