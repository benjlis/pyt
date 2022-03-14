import argparse
import pathlib
import pdf2image
import pdf2image.exceptions

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

n = 1
for p in pages:
    p.save(f'img/{filename}-{n}.png', 'PNG')
    n += 1
