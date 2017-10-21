import rake
import operator

rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 1)

with open('test.txt', 'r') as myfile:
    text = myfile.read().replace('\n', '')

keywords = rake_object.run(text)
