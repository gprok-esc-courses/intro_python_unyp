import requests
from bs4 import BeautifulSoup 

url = "https://www.unyp.cz/academic-programs/"
response = requests.get(url) 

html = response.text

soup = BeautifulSoup(html, 'html.parser')

h2 = soup.find_all('h2')

# for tag in h2:
#     print(tag.text)

elements = soup.find_all(class_='wp-block-getwid-accordion__header-title')
for element in elements:
    print(element.text)