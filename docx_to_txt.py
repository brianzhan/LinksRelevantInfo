import docx
from bs4 import BeautifulSoup
import requests
import os

class docx_to_txt:
	def __init__(self, filePath):
		self.name = filePath

	def convertDocx(self):
	    doc = docx.Document(self.name)
	    output_file_name = 'output.txt'
	    fullText = []
	    with open('./RAKE/output.txt','w') as text_file:
	        for para in doc.paragraphs:
	            text_file.write(para.text)
	    return ' '.join(fullText)

class html_to_txt:
	def __init__(self, url):
		self.name = url

	def convertUrl(self):
		page = requests.get(self.name)
		soup = BeautifulSoup(page.content, 'html.parser')
		print(soup.prettify())
		soup_string = str(soup.text)
		text_file = open("./RAKE/OutputHTML.txt","w")
		text_file.write(soup_string)
		text_file.close()


## Example
x = docx_to_txt("/Users/brianzhan/Documents/charter1.docx")
x.convertDocx()

x = html_to_txt("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
x.convertUrl()

# x = rake_classify("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# x.classify()
