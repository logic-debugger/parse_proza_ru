import requests
from bs4 import BeautifulSoup

url = input('Силка на статті НАПРИКЛАД-https://proza.ru/avtor/nadezda8211 ::: ')
r = requests.get(url)

soup = BeautifulSoup(r.text)

articles = soup.find_all('a', {'class': 'poemlink'})

for article in articles:
    article_url = 'https://proza.ru/' + article.get('href')
    article_r = requests.get(article_url)
    article_soup = BeautifulSoup(article_r.text)

    article_file = open(article_soup.find('h1').text + '.html', 'a')
    article_file.write('<head><title>' + article_soup.find('h1').text + '</title></head><body style="font-size: 21px;">')
    article_file.write(str(article_soup.find('div', {'class': 'text'})))
    article_file.write('</body>')
    article_file.close

    print(article_url)
    print(article_soup.find('h1'))
    print("Успішно\n")
