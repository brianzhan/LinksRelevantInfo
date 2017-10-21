import rake
import operator

#have the text in the document "test.txt"
with open('output.txt', 'r') as myfile:
    text = myfile.read().replace('\n', '')

#using constraint where each keyword appears in text at least twice
rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 2)
keywords = rake_object.run(text)
print(keywords)

#using constraint where each keyword appears in text at least three times
rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 3)
keywords = rake_object.run(text)
print(keywords)
