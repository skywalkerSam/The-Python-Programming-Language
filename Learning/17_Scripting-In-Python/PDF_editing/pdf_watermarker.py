"""
Developer: Sam Skywalker
Purpose: Watermarking on PDFs
Date: 12022.05.06.03:25

"""

import PyPDF2


template = PyPDF2.PdfFileReader(open("Super.pdf", 'rb'))
watermark = PyPDF2.PdfFileReader(open("watermark.pdf", 'rb'))
output = PyPDF2.PdfFileWriter()


for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open("watermarked_Super.pdf", 'wb') as file:
        output.write(file)





# Just run the script...



