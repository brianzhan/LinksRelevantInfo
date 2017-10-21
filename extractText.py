# from bs4 import BeautifulSoup
# import urllib
# r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
# soup = BeautifulSoup(r)
# print type(soup)


from bs4 import BeautifulSoup
import requests


page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
