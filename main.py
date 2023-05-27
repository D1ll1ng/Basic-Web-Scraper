import requests
from bs4 import BeautifulSoup

def get_article_name():
    url = 'https://sport.tv2.dk/badminton/2023-05-27-talent-ramt-af-ubaerlig-skade-det-skete-ikke-det-der'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    article_name = soup.find_all('h1')[-1].text.strip()

    print(article_name)

    return article_name

get_article_name()