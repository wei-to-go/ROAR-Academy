import os
import PyPDF2

path = os.path.dirname(os.path.abspath(__file__))

file_handle = open(path + '/' + 'Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(file_handle)
page_number = pdfReader.numPages 

frequency_table = {}

for i in range(page_number):
    page_object = pdfReader.getPage(i) 
    page_text__ = page_object.extractText()   
    page_text_ = page_text__.replace("Sense and Sensibility by Jane Austen","")
    page_text = page_text_.replace("Full Text Archive","")
    for word in page_text.split():
        if not word[-1].isalpha():
            word = word[:-1]
            if word.isalpha() and word!='CHAPTER' and word!='TCPDF':
                word = word.lower()
                if word not in frequency_table:
                    frequency_table[word] = 1
                else:
                    frequency_table[word] += 1

print(frequency_table)