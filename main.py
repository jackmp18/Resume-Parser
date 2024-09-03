# main.py

from pdf_reader import print_pdf_text

def main():
    # Prompt the user for the path to the PDF file
    pdf_path = input("Please enter the path to your PDF file: ")
    
    # Call the function to print the PDF text
    print_pdf_text(pdf_path)

if __name__ == "__main__":
    main()
