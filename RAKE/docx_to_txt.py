import docx
from bs4 import BeautifulSoup
import requests
import os
import rake
import operator

class docx_to_txt:
	def __init__(self, filePath):
		self.name = filePath

	def convertDocx(self):
	    doc = docx.Document(self.name)
	    output_file_name = 'output.txt'
	    fullText = []
	    with open('./output.txt','w') as text_file:
	        for para in doc.paragraphs:
	            text_file.write(para.text)
	    return ' '.join(fullText)

class html_to_txt:
	def __init__(self, url):
		self.name = url

	def convertUrl(self):
		page = requests.get(self.name)
		soup = BeautifulSoup(page.content, 'html.parser')
		# print(soup.prettify())
		soup_string = str(soup.text)
		text_file = open("./OutputHTML.txt","w")
		text_file.write(soup_string)
		text_file.close()


class rake_classify:
	def __init__(self, filePath):
		self.name = filePath

	def extractKeywords(self):
		with open(self.name, 'r') as myfile:
			text = myfile.read().replace('\n', '')
		# print "text is  ", text

		#using constraint where each keyword appears in text at least twice
		rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 2)
		keywords = rake_object.run(text)
		print("keywords1 are ", keywords)

		#using constraint where each keyword appears in text at least three times
		rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 3)
		keywords = rake_object.run(text)
		print("keywords2 are ", keywords)


## Example
x = docx_to_txt("/Users/brianzhan/Documents/charter1.docx")
x.convertDocx()

x = html_to_txt("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
x.convertUrl()

#output is the output file
x = rake_classify("output.txt")
x.extractKeywords()
