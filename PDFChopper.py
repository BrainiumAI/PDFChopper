
import logging
import os
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

logging.basicConfig(level=logging.DEBUG)

"""
Takes a pdf path and splits it based on size 
TODO: cmd prompt args vs prompt
"""

print("Chop it up!")

test_file = "./pdfs/100.pdf"
logging.debug(f'name of test file: {test_file}')


def split_pdf(input_pdf_path, start_page=0, end_page=-1):
    try:
        if not os.path.isfile(input_pdf_path):
            raise FileNotFoundError(f"Input PDF file '{input_pdf_path}' does not exist.")
        
        with open(input_pdf_path, 'rb') as input_pdf_file:
            reader = PdfReader(input_pdf_file)
            total_pages = len(reader.pages)

            if end_page == -1 or end_page > total_pages:
                end_page = total_pages

            writer = PdfWriter()

            for page_num in range(start_page, end_page):
                selected_content = reader.pages[page_num]
                logging.debug(f'Page number: {page_num}')
                writer.add_page(selected_content)  # TODO: Add the appropriate page content

            output_pdf_path = f'output_{start_page}_{end_page}.pdf'
            with open(output_pdf_path, 'wb') as output_pdf_file:
                writer.write(output_pdf_file)

            return output_pdf_path
    
    except Exception as e:
        logging.error(f"Error occurred while splitting PDF: {str(e)}")
        return None

def recursive_pdf_split(input_pdf_path, pages_per_pdf, start_page=0):
    try:
        if pages_per_pdf <= 0:
            raise ValueError("Number of pages per PDF should be greater than zero.")
        
        if start_page < 0:
            raise ValueError("Start page should be a non-negative integer.")
        
        total_pages = len(PdfReader(input_pdf_path).pages)
        
        if start_page >= total_pages:
            return
        
        end_page = start_page + pages_per_pdf
        output_pdf_path = split_pdf(input_pdf_path, start_page, end_page)
        
        if output_pdf_path is not None:
            recursive_pdf_split(output_pdf_path, pages_per_pdf, end_page)
    
    except Exception as e:
        logging.error(f"Error occurred while recursively splitting PDF: {str(e)}")

# Example usage
input_pdf_path = 'pdfs/school.pdf'
pages_per_pdf = 55
recursive_pdf_split(input_pdf_path, pages_per_pdf)