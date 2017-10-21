# from bs4 import BeautifulSoup
# import urllib
# r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
# soup = BeautifulSoup(r)
# print type(soup)


from bs4 import BeautifulSoup
import requests
import os

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
# <<<<<<< HEAD
print(soup.prettify())
soup_string = str(soup.text)
text_file = open("Output.txt","w")
text_file.write(soup_string)
text_file.close()
# =======
# # print soup.find_all("div")
# print(soup.text)
# >>>>>>> e95d66dabbf3a0a37bc7792eb038c45dcda5be0d
