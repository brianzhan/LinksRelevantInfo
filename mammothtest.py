import mammoth

with open("charter1.docx","rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value
    messages = result.messages
    print messages
    print html

def get_html_from_doc(docx_path, output_filename):
    with open(docx_path,"rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value
        messages = result.messages
        if length(messages)>0:
            print messages
            return 0
        return html