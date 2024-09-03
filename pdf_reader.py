# python program to read from files on system
# pdf_reader.py

import pdfplumber

def print_pdf_text(pdf_path):
    """
    Extracts and prints the text from each page of the specified PDF file.
    
    :param pdf_path: Path to the PDF file.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages):
                text = page.extract_text()
                print(f"--- Page {page_number + 1} ---")
                print(text)
                print("\n" + "-"*40 + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")