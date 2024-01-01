#Implement a basic web scraping program using a library like BeautifulSoup.
print ("\nWilson - Day 44 of #100DaysOfCode\n") 
print("\nImplement a basic web scraping program using a library like BeautifulSoup\n")

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print(f"failed to fetch the page. Status code: {response.status_code}")
