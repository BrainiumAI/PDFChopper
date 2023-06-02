def chop_pdf_by_pages(
        path_to_pdf='pdfs/school.pdf', pages_per_pdf=get_file_length(pdf_path='pdfs/school.pdf'),
        start_page=0, end_page=-1, output_filename='outputted_file.pdf'):

    logging.debug(f'initialized with parameters: path: {path_to_pdf} \n'
                  f'start_page: {start_page} and end_page: {end_page}.\n'
                  f'documents will be split into {pages_per_pdf} pages each from selected range')

    with open(path_to_pdf, 'rb') as f:
        reader = PdfReader(f)
        writer = PdfWriter()

        if end_page == -1:
            end_page = len(reader.pages)

        for page_num in range(start_page, end_page):
            selected_content = reader.pages[page_num]
            logging.debug(f'page number: {page_num}')
            text = selected_content.extract_text()
            logging.debug(f'{text.__sizeof__}')
            writer.add_page(text)  # TODO: not just text

        with open(output_filename, 'wb') as output:
            writer.write(output)

        filename_tail = output_filename[-1]
        logging.debug(f'{filename_tail} is the end')
        if filename_tail.isalpha():
            next_filename = output_filename + '_pdf_chopper_part_0'
        elif filename_tail.isnumeric():
            next_tail = str(int(filename_tail) + 1)
            next_filename = output_filename[:-1] + next_tail
        else:
            next_filename = output_filename + '_pdf_chopper_part_0'

        chop_pdf_by_pages(start_page=end_page, output_filename=next_filename)




# import logging
# import os
# import PyPDF2
# from PyPDF2 import PdfReader, PdfWriter

# logging.basicConfig(level=logging.DEBUG)

# """
# Takes a pdf path and splits it based on size 
# TODO: cmd prompt args vs prompt
# """

# print("Chop it up!")

# test_file = "./pdfs/100.pdf"
# logging.debug(f'name of test file: {test_file}')


# def get_pdf_metadata(pdf_path):
#     with open(pdf_path, 'rb') as pdf:
#         reader = PdfReader(pdf)
#         metadata = reader.metadata
#         logging.debug(f'{repr(metadata)} is the metadata')
#         logging.debug(f'Producer: {metadata.producer}, \n Author: {repr(metadata.author)}, Title: {repr(metadata.title)}')
#         return metadata


# get_pdf_metadata('pdfs/school.pdf')


# def get_file_length(pdf_path):
#     return len(PdfReader(pdf_path).pages)


# logging.debug(f"{get_file_length('pdfs/school.pdf')} pages detected")

# def chop_pdf_by_pages(
#         path_to_pdf='pdfs/school.pdf', pages_per_pdf: None,start_page=0, end_page=-1, output_filename='outputted_file.pdf'):

#     """
#     TODO: fix double reference, apply dcorator? 
#     TODO: fix oputput filename to be able to creat emultiple files
#     A chops document (whole or range) into pieces

    

# #         #     current_page_content = current_page.extract_text()
# #         #     results.append(current_page_content)
# #         #     writer.add_page(current_page)
# #         #     logging.debug(f'writer: {writer}, results: {results}')

# #         #     with open(output_pdf_name, 'wb') as output_pdf:
# #         #         writer.write(output_pdf)



#     """

#     logging.debug(f'initialized with parameters: path: {path_to_pdf} \n'
#                   f'start_page: {start_page} and end_page: {end_page} . \n'
#                   f'documents will be split into {pages_per_pdf} pages each from selected range')
    
#     with open(path_to_pdf, 'rb') as f:
#         reader = PdfReader(f)
#         writer = PdfWriter()
#         for page_num in range(start_page, end_page):
#             selected_content = reader.pages[page_num]
#             logging.debug(f'page number: {page_num}')
#             text = selected_content.extract_text()
#             logging.debug(f'{text.__sizeof__}')
#             writer.add_page(text)  #  TODO:  not just text
            
#         with open(output_filename, 'wb') as output:
#             writer.write(output)

        
#         filename_tail = output_filename[-1]
#         logging.debug(f'{filename_tail} is the end')
#         if filename_tail.isalpha():
#             next_filename = output_filename + '_pdf_chopper_part_0'
#         elif filename_tail.isalnum():
#             next_tail = str(int(filename_tail) + 1)
#             next_filename = output_filename + next_tail

#         chop_pdf_by_pages(start_page=end_page+1, output_filename=next_filename)

# chop_pdf_by_pages()

            

# #         # try:
# #         #     next_file_ending = int(output_filename[-1]) + 1
# #         #     next_filename = output_filename + f' pdf_chopper- {output_filename} part {str(next_file_ending) '}

        

# #         chop_pdf_by_pages(start_page=end_page, pages_per_pdf=pages_per_pdf)

        

        
            



# # chop_pdf_by_pages(pages_per_pdf=5)





# # # def read_pdf_content(path_to_pdf, start_page=0, end_page=-1):
# # #     """
# # #     returns the text content of the pdf within the bounds set
# # #     default is all
# # #     """
# # #     with open(path_to_pdf, 'rb') as pdf:
# # #         reader = PdfReader(pdf)
# # #         results = []
# # #         for page_num in range(0, len(reader.pages)):
# # #             selected_page = reader.pages[page_num]
# # #             text = selected_page.extract_text()
# # #             # if text:
# # #                 # logging.debug(f'text found on page {page_num}')
# # #             results.append(text)

# # #         return ' '.join(results)


# # # def chop_pdf_by_pages(
# # #         path_to_pdf, pages, start_page=0, output_pdf_name="Chopped_PDF"
# # #         ): 
   
# # #     """
# # #     takes a pdf and chops it into the desired number of pages
# # #     returning the new chopped-up pdfs  
# # #     """

# # #     end_page_number = start_page + pages

# # #     logging.debug(
# # #         f'{path_to_pdf} is the path; extract pages {start_page} - {end_page_number}, \n{output_pdf_name}: name')
    
# # #     print('hi')
    
# # # read_pdf_content('pdfs/100.pdf')
# # # chop_pdf_by_pages('pdfs/100.pdf', 3)








    
# # #     #     #  TODO: previous work is commented below, think need a function and can use recursion to call itself from the previous end point
# # #     # with open(path_to_pdf, 'wb') as f:
# # #     #     reader = PdfReader(f)


# # #         # writer = PdfWriter()
# # #         # results = []
# # #         # for page_num in range(start_page, end_page_number):
# # #         #     current_page = reader.pages[page_num]

# # #         #     # TODO: fix, this just chops to page num need to keep going in chunks
# # #         #     """
# # #         #     add the chunks to the writer until its full, then reset the end_page_number again but continuing from where it left off. 
# # #         #     recursion?

# # #         #     """

# # #         #     current_page_content = current_page.extract_text()
# # #         #     results.append(current_page_content)
# # #         #     writer.add_page(current_page)
# # #         #     logging.debug(f'writer: {writer}, results: {results}')

# # #         #     with open(output_pdf_name, 'wb') as output_pdf:
# # #         #         writer.write(output_pdf)
