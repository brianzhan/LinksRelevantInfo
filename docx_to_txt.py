import docx


def getText(filename):
    doc = docx.Document(filename)
    output_file_name = filename[:-4]+'_docx_as_text.txt'
    fullText = []
    text_file = open(output_file_name,"w")
    for para in doc.paragraphs:
        text_file.write(para.text)
    return '\n'.join(fullText)
