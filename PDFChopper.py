import logging
import os
from PyPDF2 import PdfReader, PdfWriter

logging.basicConfig(level=logging.DEBUG)


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
                writer.add_page(selected_content)

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

        if not os.path.isfile(input_pdf_path):
            raise FileNotFoundError(f"Input PDF file '{input_pdf_path}' does not exist.")

        total_pages = len(PdfReader(input_pdf_path).pages)
        remaining_pages = total_pages - start_page

        if remaining_pages <= 0:
            return

        end_page = start_page + min(pages_per_pdf, remaining_pages)
        output_pdf_path = split_pdf(input_pdf_path, start_page, end_page)

        if output_pdf_path is not None:
            next_start_page = end_page  # Start from the next page after the current chunk
            recursive_pdf_split(input_pdf_path, pages_per_pdf, next_start_page)

    except ValueError as ve:
        logging.error(f"Invalid input value: {str(ve)}")
    except FileNotFoundError as fe:
        logging.error(str(fe))
    except Exception as e:
        logging.error(f"Error occurred while recursively splitting PDF: {str(e)}")


# Example usage
input_pdf_path = 'pdfs/school.pdf'
pages_per_pdf = 55
recursive_pdf_split(input_pdf_path, pages_per_pdf)
