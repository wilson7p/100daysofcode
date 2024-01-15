#Web Scraper
print ("\nWilson - Day 57 of #100DaysOfCode\n") 
print("\nWeb Scraper\n")

import requests
from bs4 import BeautifulSoup

def get_web_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"failed to retrieve the web content. Status code: {response.status_code}")
        return None

def extract_information(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headlines = soup.find_all('h2', class_='headline')
    return [headline.text.strip() for headline in headlines]

def display_information(information):
    for i, item in enumerate(information, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    target_url = "https://www.amazon.in/?" 
    web_content = get_web_content(target_url)

    if web_content:
        extracted_info = extract_information(web_content)
        display_information(extracted_info)
    else:
        print("web scraping failed.")
