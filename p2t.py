import argparse
import pathlib
import pdf2image
import pdf2image.exceptions
import pytesseract

parser = argparse.ArgumentParser(description='Generates an image file for each \
page of a PDF in the img subdirectory')
parser.add_argument('pdf_file', help='PDF to be converted to images')
cl_args = parser.parse_args()

# example: /Users/benjaminlis/history-lab/test-pdfs/pdb_19610622.pdf'
# TODO - if needed
# 1. check if file exists
# 2. check if pdf is provided

full_pdf_filename = cl_args.pdf_file
filename = pathlib.Path(full_pdf_filename).stem

pages = pdf2image.convert_from_path(full_pdf_filename)
print(f'pages: {len(pages)}')

# print(pytesseract.image_to_string(Image.open("sessionlawsresol1955nort_0057.jpg"), lang="eng"))

n = 1
for p in pages:
    t = pytesseract.image_to_string(p)
    print(f'page {n}:')
    print(t)
    x = input('Hit "return" to continue')
    n += 1
