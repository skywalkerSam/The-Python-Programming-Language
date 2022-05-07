"""
Developer: Sam Skywalker
Purpose: Learning
Date: 12022.05.06.00:46

"""


import PyPDF2
from matplotlib.pyplot import show

with open("./pdf_source/Project-ZERO.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
    # print(dir(reader))
    page_one = reader.getPage(1)
    page_one.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page_one)
    with open("./pdf_source/tilted_text.pdf", 'wb') as new_file:
        writer.write(new_file)






