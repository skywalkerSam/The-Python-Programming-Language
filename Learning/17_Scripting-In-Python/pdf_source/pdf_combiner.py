"""
Developer: Sam Skywalker
Purpose: PDF Combiner 
Date: 12022.05.06.02:48

"""

import sys
import PyPDF2


pdf_files = sys.argv[1:]


def pdf_combiner(files):
    merger = PyPDF2.PdfFileMerger()
    for pdf in files:
        # print(pdf)
        merger.append(pdf)
        print("\n\t PDF Merge Successful :) \n")
    merger.write("./Super.pdf")



pdf_combiner(pdf_files)



"""
# Notes;

File Names: Getting_Started_With_AI_WP_30.05.19.pdf Project-CortanaAI.pdf Project-ZERO.pdf Ubuntu_Server_CLI_pro_tips_2020-04.pdf

Command Used: .\pdf_combiner.py Getting_Started_With_AI_WP_30.05.19.pdf Project-CortanaAI.pdf Project-ZERO.pdf Ubuntu_Server_CLI_pro_tips_2020-04.pdf

"""


