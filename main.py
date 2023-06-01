import argparse


def get_directory():
    """
    temporary(?) hack to get system agnostic path for the pdf file
    """
    directory = input("Enter the full file directory path for the pdf file: ")
    return str(directory)


selected_directory = get_directory()
print("Selected directory: ", selected_directory)


def main():
    """
    pdf_chopper - Split PDF Files
    Kindle would not accept some .PDF files due to size constraints,
    so this simple program aims to split PDF files based on desired:

    ### CHOPPER ###
    Page count
    File Size

    ### STICHER ###
    Merge PDFS (perhaps back together again)
    """

    # Create an argument parser
    parser = argparse.ArgumentParser(description='PDF Chopper')
    
    # Add arguments for user choice
    parser.add_argument(
        '--split-by', choices=['size', 'pages'],
        default='size', help='Specify whether to split by "size" or "pages"')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    if args.split_by == 'size':
        # Split PDF files based on size
        desired_size_mb = float(input('Enter the desired size (in MB) for each chopped PDF:'))
        # Call the function to split by size
        
    elif args.split_by == 'page':
        # Split PDF files based on page numbers
        start_page = int(input('Enter the starting page: '))
        stop_page = int(input('Enter the ending page: '))
        


if __name__ == '__main__':
    main()
