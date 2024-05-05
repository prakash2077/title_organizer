import os
import metadata_title

pdfs = os.listdir('PDFs')

for pdf in pdfs:
    title = metadata_title.read_title(f'PDFs/{pdf}')
    print(title)