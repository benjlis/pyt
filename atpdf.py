import argparse
import pathlib
import pdf2image
import pdf2image.exceptions
import pytesseract
import PyPDF2
import io

parser = argparse.ArgumentParser(description='Generates an image file for each \
page of a PDF in the img subdirectory')
parser.add_argument('pdf_file', help='PDF to be converted to images')
cl_args = parser.parse_args()

# example: /Users/benjaminlis/history-lab/test-pdfs/pdb_19610622.pdf'
# TODO - if needed
# 1. check if file exists
# 2. check if pdf is provided

full_pdf_fname = cl_args.pdf_file
pdfta_fname = pathlib.Path(full_pdf_fname).stem + '_ta.pdf'

print(f'Converting {full_pdf_fname} to images')
pages = pdf2image.convert_from_path(full_pdf_fname)
print(f'pages: {len(pages)}')
# custom_psm_config = r'--psm 1'
merger = PyPDF2.PdfFileMerger()
n = 1
for p in pages:
    print(f'processing page {n}')
    p.save('tmp.tif', 'TIFF', quality=100, dpi=(300, 300))
    result = pytesseract.image_to_pdf_or_hocr('tmp.tif', extension='pdf')
    pdf_mem = io.BytesIO(result)
    merger.append(pdf_mem)
    n += 1
merger.write(pdfta_fname)
merger.close()
print(f'PDF with text embedded: {pdfta_fname}')
