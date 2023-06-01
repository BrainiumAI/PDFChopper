
import os
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

"""
Takes a pdf path and splits it based on size 
TODO: cmd prompt args vs prompt
"""

print("Chop it up!")

test_file = "./pdfs/100.pdf"

def read_pdf_content(path_to_pdf):
    with open(path_to_pdf, 'rb') as pdf:
        reader = PdfReader(pdf)
        results = []
        for page_num in range(0, len(reader.pages)):
            selected_content = reader.pages[page_num]
            results.append(selected_content)

    return ' '.join(results)


def chop_pdf_by_size(desired_size_in_mb):
    pass


def chop_pdf_by_pages(desired_page_range):
    pass
