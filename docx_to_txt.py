import docx

def getText(filename):
    doc = docx.Document(filename)
    output_file_name = 'output.txt'
    fullText = []
    with open('./RAKE/output.txt','w') as text_file:
        for para in doc.paragraphs:
            text_file.write(para.text)
    return ' '.join(fullText)

def test():
    getText("/Users/pierce/Documents/Projects/Sandbox/charter1.docx")

test()

